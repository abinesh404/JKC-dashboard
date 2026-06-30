# Fixed_Asset/ITAC/FJIT24.py
import pandas as pd
import os

CONFIG = {
    "id": "FJIT24",
    "name": "Asset Capitalisation Date as per Masters vs Asset Capitalisation Entry Date",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Asset Capitalisation Date as per Masters vs Asset Capitalisation Entry Date",
            "cards": [
                {"id": "k1", "label": "Capitalization Date Mismatch Cases", "agg": "unique", "source": "asset_number"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Asset Classes Impacted", "agg": "unique", "source": "asset_class"},
                {"id": "k4", "label": "Total Asset Value Impacted", "agg": "total_value", "source": "current_book_value", "format": "currency"},
                {"id": "k5", "label": "Average Capitalization Delay (Days)", "agg": "avg", "source": "delay_days"},
                {"id": "k6", "label": "Assets with Depreciation Impact", "agg": "unique", "source": "depr_impact_asset_id"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Company Name", "source": "company_name", "all_label": "All Company Names"},
                {"id": "f3", "label": "Country", "source": "country", "all_label": "All Countries"},
                {"id": "f4", "label": "City", "source": "city", "all_label": "All Cities"},
                {"id": "f5", "label": "Currency", "source": "currency", "all_label": "All Currencies"},
                {"id": "f6", "label": "Asset Class", "source": "asset_class", "all_label": "All Classes"},
                {"id": "f7", "label": "Asset Number", "source": "asset_number", "all_label": "All Assets"},
                {"id": "f8", "label": "Sub Number", "source": "sub_number", "all_label": "All Sub Numbers"},
                {"id": "f9", "label": "Asset Description", "source": "asset_desc", "all_label": "All Descriptions"},
                {"id": "f10", "label": "Account Determination Key", "source": "acct_key", "all_label": "All Keys"},
                {"id": "f11", "label": "Plant Code", "source": "plant_code", "all_label": "All Plants"},
                {"id": "f12", "label": "Plant Description", "source": "plant_desc", "all_label": "All Plant Descriptions"},
                {"id": "f13", "label": "Location", "source": "location", "all_label": "All Locations"},
                {"id": "f14", "label": "Business Area", "source": "business_area", "all_label": "All Areas"},
                {"id": "f15", "label": "Cost Center", "source": "cost_center", "all_label": "All Cost Centers"},
                {"id": "f16", "label": "Responsible Employee", "source": "resp_employee", "all_label": "All Employees"},
                {"id": "f17", "label": "Created By", "source": "created_by", "all_label": "All Creators"},
                {"id": "f18", "label": "Changed By", "source": "changed_by", "all_label": "All Modifiers"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "company_name",
                    "y": "asset_number",
                    "agg": "count",
                    "title": "Company-wise Capitalization Mismatch Cases"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "asset_class",
                    "y": "acquisition_value",
                    "agg": "sum",
                    "title": "Asset Class-wise Impact Analysis"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "entry_date",
                    "y": "delay_days",
                    "agg": "avg",
                    "time_group": "month",
                    "title": "Capitalization Delay Trend"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "plant_desc",
                    "y": "current_book_value",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Plant-wise Asset Value Exposure"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "resp_employee",
                    "y": "asset_number",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Responsible Employee Analysis"
                }
            ]
        }
    ],
    "columns": {
        "company_code": ["Company Code"],
        "company_name": ["Company Name"],
        "country": ["Country"],
        "city": ["City"],
        "currency": ["Currency"],
        "asset_class": ["Asset Class"],
        "asset_number": ["Asset Number"],
        "sub_number": ["Sub Number"],
        "asset_desc": ["Asset Description"],
        "acct_key": ["Account Determination Key"],
        "plant_code": ["Plant Code"],
        "plant_desc": ["Plant Description"],
        "location": ["Location"],
        "business_area": ["Business Area"],
        "cost_center": ["Cost Center"],
        "resp_employee": ["Responsible Employee"],
        "created_by": ["Created By"],
        "changed_by": ["Changed By"],
        "acquisition_value": ["Acquisition Value"],
        "current_book_value": ["Current Book Value"],
        "entry_date": ["Capitalisation Entry Date"],
        "date": ["Capitalisation Entry Date"],
        # Helpers
        "delay_days": ["Delay Days"],
        "depr_impact_asset_id": ["Depr Impact Asset ID"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "ITAC"
    }

def get_data(exc_id):
    paths = [
        rf"D:\off\JKC Dashboard\output\FJIT24_Exception{int(exc_id):02}.csv",
        rf"data_files/FJIT24_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to standard schema
    rename_map = {
        "Company Code": "Company Code",
        "Company Name": "Company Name",
        "City": "City",
        "Currency": "Currency",
        "Plant Description": "Plant Description",
        "Country": "Country",
        "Language": "Language",
        "Plant Code": "Plant Code",
        "Location": "Location",
        "Asset Number": "Asset Number",
        "Sub Number": "Sub Number",
        "Asset Class": "Asset Class",
        "Asset Retirement Number": "Asset Retirement Number",
        "Created By": "Created By",
        "Created Date": "Created Date",
        "Changed By": "Changed By",
        "Changed On": "Changed On",
        "Account Determination Key": "Account Determination Key",
        "Deactivation Indicator": "Deactivation Indicator",
        "Original Asset No. / Asset Super No.": "Original Asset No. / Asset Super No.",
        "Asset Description": "Asset Description",
        "Business Area": "Business Area",
        "Cost Center": "Cost Center",
        "Responsible Employee": "Responsible Employee",
        "Depreciation Area Key": "Depreciation Area Key",
        "Ordinary Depreciation Start Date": "Ordinary Depreciation Start Date",
        "Depreciation key": "Depreciation key",
        "Useful Life (in years)": "Useful Life (in years)",
        "Scrap Value": "Scrap Value",
        "Cumulative Acquisition Value": "Cumulative Acquisition Value",
        "Accumulated Depreciation": "Accumulated Depreciation",
        "Asset Value (Current Year)": "Asset Value (Current Year)",
        "Acquisition Value": "Acquisition Value",
        "Master Capitalisation Date": "Master Capitalisation Date",
        "Capitalisation Entry Date": "Capitalisation Entry Date",
        "Current Book Value": "Current Book Value"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = 0.0 if "Value" in col or "value" in col or "Depreciation" in col or "Scrap" in col else ""
            
    # Parse numbers to float
    for c in ["Acquisition Value", "Current Book Value"]:
        df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0.0)
        
    # Calculate Delay Days (Capitalisation Entry Date - Master Capitalisation Date) and Depreciation Impact
    delay_days = []
    depr_impact_assets = []
    
    for idx, row in df.iterrows():
        entry_dt = str(row.get("Capitalisation Entry Date", "")).strip()
        master_dt = str(row.get("Master Capitalisation Date", "")).strip()
        asset_num = str(row.get("Asset Number", "")).strip()
        
        try:
            e_val = pd.to_datetime(entry_dt, errors='coerce')
            m_val = pd.to_datetime(master_dt, errors='coerce')
            
            if pd.notna(e_val) and pd.notna(m_val):
                diff = (e_val - m_val).days
                delay_days.append(float(max(0, diff)))
                
                # Depreciation Impact if Entry Date > Master Date
                if e_val > m_val:
                    depr_impact_assets.append(asset_num)
                else:
                    depr_impact_assets.append("")
            else:
                delay_days.append(0.0)
                depr_impact_assets.append("")
        except Exception:
            delay_days.append(0.0)
            depr_impact_assets.append("")
            
    df["Delay Days"] = delay_days
    df["Depr Impact Asset ID"] = depr_impact_assets
    
    return df.fillna('')
