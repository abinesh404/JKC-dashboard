# Fixed_Asset/Depreciation/FJDE25.py
import pandas as pd
import os

CONFIG = {
    "id": "FJDE25",
    "name": "Gap in Capitalisation Date & Depreciation Date in Asset Master",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
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
        rf"data_files/FJDE25_Exception{int(exc_id):02}.csv",
        rf"data_files/FJDE25_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None