# Fixed_Asset/Depreciation/FJDE28.py
import pandas as pd
import os

CONFIG = {
    "id": "FJDE28",
    "name": "No Depreciation Against In-Use Asset with Salvage Value Greater Than 5%",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Instances Where Scrap Value is Greater Than 5% of Acquisition Value",
            "cards": [
                {"id": "k1", "label": "Assets with Salvage Value > 5%", "agg": "unique", "source": "asset_number"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Asset Classes Impacted", "agg": "unique", "source": "asset_class"},
                {"id": "k4", "label": "Total Acquisition Value", "agg": "total_value", "source": "acquisition_value", "format": "currency"},
                {"id": "k5", "label": "Total Salvage Value", "agg": "total_value", "source": "salvage_value", "format": "currency"},
                {"id": "k6", "label": "Average Salvage Value %", "agg": "avg", "source": "salvage_percent"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant Code", "source": "plant_code", "all_label": "All Plants"},
                {"id": "f3", "label": "Asset Class", "source": "asset_class", "all_label": "All Classes"},
                {"id": "f4", "label": "Asset Number", "source": "asset_number", "all_label": "All Assets"},
                {"id": "f5", "label": "Cost Center", "source": "cost_center", "all_label": "All Cost Centers"},
                {"id": "f6", "label": "Responsible Employee", "source": "resp_employee", "all_label": "All Employees"},
                {"id": "f7", "label": "Depreciation Key", "source": "depr_key", "all_label": "All Keys"},
                {"id": "f8", "label": "Depreciation Area Key", "source": "depr_area", "all_label": "All Areas"},
                {"id": "f9", "label": "Created By", "source": "created_by", "all_label": "All Creators"},
                {"id": "f10", "label": "Changed By", "source": "changed_by", "all_label": "All Modifiers"},
                {"id": "f11", "label": "Country", "source": "country", "all_label": "All Countries"},
                {"id": "f12", "label": "City", "source": "city", "all_label": "All Cities"},
                {"id": "f13", "label": "Company Name", "source": "company_name", "all_label": "All Company Names"},
                {"id": "f14", "label": "Currency", "source": "currency", "all_label": "All Currencies"},
                {"id": "f15", "label": "Asset Description", "source": "asset_desc", "all_label": "All Descriptions"},
                {"id": "f16", "label": "Plant Description", "source": "plant_desc", "all_label": "All Plant Descriptions"},
                {"id": "f17", "label": "Location", "source": "location", "all_label": "All Locations"},
                {"id": "f18", "label": "Business Area", "source": "business_area", "all_label": "All Areas"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "asset_class",
                    "y": "salvage_percent",
                    "agg": "avg",
                    "title": "Asset Class-wise Salvage Value Analysis"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "company_name",
                    "y": "asset_number",
                    "agg": "count",
                    "title": "Company-wise Exception Distribution"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "plant_desc",
                    "y": "salvage_value",
                    "agg": "sum",
                    "title": "Plant-wise Salvage Value Exposure"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "asset_number",
                    "y": "salvage_percent",
                    "agg": "avg",
                    "top_n": 10,
                    "title": "Asset-wise Salvage Percentage"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "cost_center",
                    "y": "current_book_value",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Cost Center-wise Asset Exposure"
                }
            ]
        }
    ],
    "columns": {
        "company_code": ["Company Code"],
        "plant_code": ["Plant Code"],
        "asset_class": ["Asset Class"],
        "asset_number": ["Asset Number"],
        "cost_center": ["Cost Center"],
        "resp_employee": ["Responsible Employee"],
        "depr_key": ["Depreciation key"],
        "depr_area": ["Depreciation Area Key"],
        "created_by": ["Created By"],
        "changed_by": ["Changed By"],
        "country": ["Country"],
        "city": ["City"],
        "company_name": ["Company Name"],
        "currency": ["Currency"],
        "asset_desc": ["Asset Description"],
        "plant_desc": ["Plant Description"],
        "location": ["Location"],
        "business_area": ["Business Area"],
        "acquisition_value": ["Acquisition Value"],
        "salvage_value": ["Scrap Value/Salvage Value"],
        "salvage_percent": ["Salvage Percentage"],
        "current_book_value": ["Current Book Value"],
        "date": ["Capitalisation Date"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Depreciation"
    }

def get_data(exc_id):
    paths = [
        rf"D:\off\JKC Dashboard\output\FJDE28_Exception{int(exc_id):02}.csv",
        rf"data_files/FJDE28_Exception{int(exc_id):02}.csv"
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
        "Capitalisation Date": "Capitalisation Date",
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
        "Cumulative Acquisition Value": "Cumulative Acquisition Value",
        "Accumulated Depreciation": "Accumulated Depreciation",
        "Asset Value (Current Year)": "Asset Value (Current Year)",
        "Scrap Value/Salvage Value": "Scrap Value/Salvage Value",
        "Acquisition Value": "Acquisition Value",
        "Current Book Value": "Current Book Value"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = 0.0 if "Value" in col or "value" in col or "Depreciation" in col or "Scrap" in col or "Percent" in col else ""
            
    # Parse numbers to float
    for c in ["Acquisition Value", "Scrap Value/Salvage Value", "Current Book Value"]:
        df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0.0)
        
    # Calculate Salvage Percentage: (Scrap Value/Salvage Value / Acquisition Value) * 100
    salvage_percents = []
    for idx, row in df.iterrows():
        acq = float(row.get("Acquisition Value", 0.0))
        sal = float(row.get("Scrap Value/Salvage Value", 0.0))
        if acq > 0:
            salvage_percents.append((sal / acq) * 100.0)
        else:
            salvage_percents.append(0.0)
            
    df["Salvage Percentage"] = salvage_percents
    
    return df.fillna('')
