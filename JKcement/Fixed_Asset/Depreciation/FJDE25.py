# Fixed_Asset/Depreciation/FJDE25.py
import pandas as pd
import os

CONFIG = {
    "id": "FJDE25",
    "name": "Gap in Capitalisation Date & Depreciation Date in Asset Master",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Gap in Capitalisation Date and Depreciation Start Date in Asset Master",
            "cards": [
                {"id": "k1", "label": "Assets with Depreciation Gap", "agg": "unique", "source": "asset_number"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Asset Classes Impacted", "agg": "unique", "source": "asset_class"},
                {"id": "k4", "label": "Total Asset Value Impacted", "agg": "total_value", "source": "current_book_value", "format": "currency"},
                {"id": "k5", "label": "Average Gap Days", "agg": "avg", "source": "gap_days"},
                {"id": "k6", "label": "Total Financial Impact", "agg": "total_value", "source": "impact", "format": "currency"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Asset Class", "source": "asset_class", "all_label": "All Classes"},
                {"id": "f3", "label": "Plant Code", "source": "plant_code", "all_label": "All Plants"},
                {"id": "f4", "label": "Responsible Employee", "source": "resp_employee", "all_label": "All Employees"},
                {"id": "f5", "label": "Depreciation Area Key", "source": "depr_area", "all_label": "All Areas"},
                {"id": "f6", "label": "Depreciation Key", "source": "depr_key", "all_label": "All Keys"},
                {"id": "f7", "label": "Company Name", "source": "company_name", "all_label": "All Company Names"},
                {"id": "f8", "label": "Country", "source": "country", "all_label": "All Countries"},
                {"id": "f9", "label": "City", "source": "city", "all_label": "All Cities"},
                {"id": "f10", "label": "Currency", "source": "currency", "all_label": "All Currencies"},
                {"id": "f11", "label": "Asset Number", "source": "asset_number", "all_label": "All Assets"},
                {"id": "f12", "label": "Asset Description", "source": "asset_desc", "all_label": "All Descriptions"},
                {"id": "f13", "label": "Plant Description", "source": "plant_desc", "all_label": "All Plant Descriptions"},
                {"id": "f14", "label": "Location", "source": "location", "all_label": "All Locations"},
                {"id": "f15", "label": "Business Area", "source": "business_area", "all_label": "All Areas"},
                {"id": "f16", "label": "Cost Center", "source": "cost_center", "all_label": "All Cost Centers"},
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
                    "title": "Company-wise Depreciation Gap Cases"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "asset_class",
                    "y": "impact",
                    "agg": "sum",
                    "title": "Asset Class-wise Financial Impact"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "gap_days",
                    "y": "asset_number",
                    "agg": "count",
                    "title": "Gap Days Distribution"
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
        "asset_class": ["Asset Class"],
        "plant_code": ["Plant Code"],
        "resp_employee": ["Responsible Employee"],
        "depr_area": ["Depreciation Area Key"],
        "depr_key": ["Depreciation key"],
        "company_name": ["Company Name"],
        "country": ["Country"],
        "city": ["City"],
        "currency": ["Currency"],
        "asset_number": ["Asset Number"],
        "asset_desc": ["Asset Description"],
        "plant_desc": ["Plant Description"],
        "location": ["Location"],
        "business_area": ["Business Area"],
        "cost_center": ["Cost Center"],
        "created_by": ["Created By"],
        "changed_by": ["Changed By"],
        "current_book_value": ["Current Book Value"],
        "gap_days": ["GapDays"],
        "impact": ["Impact"],
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
        rf"D:\off\JKC Dashboard\output\FJDE25_Exception{int(exc_id):02}.csv",
        rf"data_files/FJDE25_Exception{int(exc_id):02}.csv"
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
        "Scrap Value": "Scrap Value",
        "Cumulative Acquisition Value": "Cumulative Acquisition Value",
        "Accumulated Depreciation": "Accumulated Depreciation",
        "Asset Value (Current Year)": "Asset Value (Current Year)",
        "Acquisition Value": "Acquisition Value",
        "Current Book Value": "Current Book Value",
        "GapDays": "GapDays",
        "Impact": "Impact"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = 0.0 if "Value" in col or "value" in col or "Depreciation" in col or "Scrap" in col or "Impact" in col or "Days" in col else ""
            
    # Parse numbers to float
    for c in ["Current Book Value", "GapDays", "Impact"]:
        df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0.0)
        
    return df.fillna('')
