# Fixed_Asset/Capitalization/FJCA23.py
import pandas as pd
import os

CONFIG = {
    "id": "FJCA23",
    "name": "Delay in Capitalisation (Changes to the Date)",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Assets Where Change in Capitalization Date is Made",
            "cards": [
                {"id": "k1", "label": "Assets with Cap Date Changes", "agg": "unique", "source": "main_asset_number"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Users Making Changes", "agg": "unique", "source": "user_change"},
                {"id": "k4", "label": "Vendors Impacted", "agg": "unique", "source": "vendor"},
                {"id": "k5", "label": "Asset Classes Impacted", "agg": "unique", "source": "asset_class"},
                {"id": "k6", "label": "Average Cap Delay (Days)", "agg": "avg", "source": "delay_days"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Asset Class", "source": "asset_class", "all_label": "All Asset Classes"},
                {"id": "f3", "label": "User", "source": "user_change", "all_label": "All Users"},
                {"id": "f4", "label": "Asset Category", "source": "asset_category", "all_label": "All Categories"},
                {"id": "f5", "label": "Manufacturer", "source": "manufacturer", "all_label": "All Manufacturers"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "asset_class",
                    "agg": "count",
                    "title": "Asset Class-wise Capitalization Changes"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "user_change",
                    "agg": "count",
                    "top_n": 10,
                    "title": "User-wise Capitalization Date Changes"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "company_name",
                    "agg": "count",
                    "title": "Company-wise Impact Analysis"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "change_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Trend of Capitalization Date Changes"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "field_name",
                    "agg": "count",
                    "title": "Changed Field Analysis"
                }
            ]
        }
    ],
    "columns": {
        "company_code": ["Company Code"],
        "asset_class": ["Asset Class"],
        "user_change": ["User name of person for change document"],
        "asset_category": ["Asset Category"],
        "manufacturer": ["Manufacturer of asset"],
        "main_asset_number": ["Main Asset Number"],
        "vendor": ["Account Number Vendor"],
        "delay_days": ["Delay Days"],
        "company_name": ["Name of Company"],
        "change_date": ["Creation date of the change document"],
        "field_name": ["Field Name"],
        "date": ["Creation date of the change document"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Capitalization"
    }

def get_data(exc_id):
    paths = [
        rf"D:\off\JKC Dashboard\output\FJCA23_Exception{int(exc_id):02}.csv",
        rf"data_files/FJCA23_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to standard schema
    rename_map = {
        "Main Asset Number": "Main Asset Number",
        "Asset Class": "Asset Class",
        "Asset types": "Asset types",
        "Document change number": "Document change number",
        "User name of person for change document": "User name of person for change document",
        "Creation date of the change document": "Creation date of the change document",
        "Time changed": "Time changed",
        "Transaction in which a change was made": "Transaction in which a change was made",
        "Planned change number": "Planned change number",
        "Application object change type": "Application object change type",
        "Changed table record key": "Changed table record key",
        "Change Type": "Change Type",
        "Company Code": "Company Code",
        "Name of Person who Created the Object": "Name of Person who Created the Object",
        "Date on Which Record Was Created": "Date on Which Record Was Created",
        "Name of Person Changed Object": "Name of Person Changed Object",
        "Changed on": "Changed on",
        "Asset Category": "Asset Category",
        "Asset capitalization date": "Asset capitalization date",
        "Asset purchase order date": "Asset purchase order date",
        "Account Number Vendor": "Account Number Vendor",
        "Name of Company": "Name of Company",
        "City": "City",
        "Currency Key": "Currency Key",
        "Manufacturer of asset": "Manufacturer of asset",
        "Asset type name": "Asset type name",
        "Asset description": "Asset description",
        "Table Name": "Table Name",
        "Field Name": "Field Name",
        "Object class": "Object class",
        "Object value": "Object value",
        "New contents of changed field": "New contents of changed field",
        "Old contents of changed field": "Old contents of changed field",
        "Exception": "Exception"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = ""
            
    # Calculate Delay Days (Asset capitalization date - Asset purchase order date)
    delay_days = []
    for idx, row in df.iterrows():
        cap_dt = str(row.get("Asset capitalization date", "")).strip()
        po_dt = str(row.get("Asset purchase order date", "")).strip()
        
        try:
            c_val = pd.to_datetime(cap_dt, errors='coerce')
            p_val = pd.to_datetime(po_dt, errors='coerce')
            
            if pd.notna(c_val) and pd.notna(p_val):
                diff = (c_val - p_val).days
                delay_days.append(float(max(0, diff)))
            else:
                delay_days.append(0.0)
        except Exception:
            delay_days.append(0.0)
            
    df["Delay Days"] = delay_days
    
    return df.fillna('')
