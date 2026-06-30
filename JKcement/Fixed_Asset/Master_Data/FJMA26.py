# Fixed_Asset/Master_Data/FJMA26.py
import pandas as pd
import os

CONFIG = {
    "id": "FJMA26",
    "name": "Changes to Useful Life of Asset",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Useful Life Changed After Capitalization",
            "cards": [
                {"id": "k1", "label": "Assets with Useful Life Changes", "agg": "unique", "source": "asset_number"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Asset Classes Impacted", "agg": "unique", "source": "asset_class"},
                {"id": "k4", "label": "Users Making Changes", "agg": "unique", "source": "change_user"},
                {"id": "k5", "label": "Total Assets Impacted", "agg": "unique", "source": "asset_number"},
                {"id": "k6", "label": "Average Useful Life Change (Years)", "agg": "avg", "source": "life_change"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Asset Class", "source": "asset_class", "all_label": "All Classes"},
                {"id": "f3", "label": "Asset Category", "source": "asset_category", "all_label": "All Categories"},
                {"id": "f4", "label": "Manufacturer of Asset", "source": "manufacturer", "all_label": "All Manufacturers"},
                {"id": "f5", "label": "User Name for Change Doc", "source": "change_user", "all_label": "All Users"},
                {"id": "f6", "label": "Name of Person Changed", "source": "person_changed", "all_label": "All Modifiers"},
                {"id": "f7", "label": "Name of Person Created", "source": "person_created", "all_label": "All Creators"},
                {"id": "f8", "label": "Main Asset Number", "source": "asset_number", "all_label": "All Assets"},
                {"id": "f9", "label": "Asset Type Name", "source": "asset_type_name", "all_label": "All Asset Types"},
                {"id": "f10", "label": "Asset Description", "source": "asset_desc", "all_label": "All Descriptions"},
                {"id": "f11", "label": "Creation Date of Change Doc", "source": "change_doc_date", "all_label": "All Dates"},
                {"id": "f12", "label": "Changed On", "source": "changed_on", "all_label": "All Change Dates"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "asset_class",
                    "y": "asset_number",
                    "agg": "count",
                    "title": "Asset Class-wise Useful Life Changes"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "change_user",
                    "y": "change_doc_num",
                    "agg": "count",
                    "top_n": 10,
                    "title": "User-wise Useful Life Changes"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "company_code",
                    "y": "asset_number",
                    "agg": "count",
                    "title": "Company-wise Impact Analysis"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "change_doc_date",
                    "y": "change_doc_num",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Trend of Useful Life Changes"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "asset_type_name",
                    "y": "asset_number",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Asset Type-wise Change Analysis"
                }
            ]
        }
    ],
    "columns": {
        "company_code": ["Company Code"],
        "asset_class": ["Asset Class"],
        "asset_category": ["Asset Category"],
        "manufacturer": ["Manufacturer of asset"],
        "change_user": ["User name of person for change document"],
        "person_changed": ["Name of Person Changed Object"],
        "person_created": ["Name of Person who Created the Object"],
        "asset_number": ["Main Asset Number"],
        "asset_type_name": ["Asset type name"],
        "asset_desc": ["Asset description"],
        "change_doc_date": ["Creation date of the change document"],
        "changed_on": ["Changed on"],
        "change_doc_num": ["Document change number"],
        "life_change": ["Useful Life Change"],
        "date": ["Creation date of the change document"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Master_Data"
    }

def get_data(exc_id):
    paths = [
        rf"D:\off\JKC Dashboard\output\FJMA26_Exception{int(exc_id):02}.csv",
        rf"data_files/FJMA26_Exception{int(exc_id):02}.csv"
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
        "Asset purchase order date": "Asset purchase order date",
        "Account Number Vendor": "Account Number Vendor",
        "Manufacturer of asset": "Manufacturer of asset",
        "Asset type name": "Asset type name",
        "Asset description": "Asset description",
        "Table Name": "Table Name",
        "Field Name": "Field Name",
        "Object class": "Object class",
        "Object value": "Object value",
        "New contents of changed field": "New contents of changed field",
        "Old contents of changed field": "Old contents of changed field",
        "Asset capitalization date": "Asset capitalization date",
        "Creation date of the change document": "Creation date of the change document",
        "Exception": "Exception"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = ""
            
    # Calculate life change = New - Old
    life_changes = []
    for idx, row in df.iterrows():
        new_val = str(row.get("New contents of changed field", "")).strip()
        old_val = str(row.get("Old contents of changed field", "")).strip()
        try:
            n_num = float(new_val) if new_val else 0.0
            o_num = float(old_val) if old_val else 0.0
            life_changes.append(n_num - o_num)
        except Exception:
            life_changes.append(0.0)
            
    df["Useful Life Change"] = life_changes
    
    return df.fillna('')
