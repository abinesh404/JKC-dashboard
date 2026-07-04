# Fixed_Asset/Depreciation/FJDE28.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "FJDE28",
    "name": "No Depreciation Against In-Use Asset with Salvage Value Greater Than 5%",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
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
        rf"data_files/FJDE28_Exception{int(exc_id):02}.csv",
        rf"data_files/FJDE28_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None