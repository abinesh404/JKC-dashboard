# Fixed_Asset/Depreciation/FJDE27.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "FJDE27",
    "name": "Negative Book Value of Asset",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company_code": ["Company Code"],
        "asset_class": ["Asset Class"],
        "plant_code": ["Plant Code"],
        "depr_area": ["Depreciation Area Key"],
        "resp_employee": ["Responsible Employee"],
        "cost_center": ["Cost Center"],
        "company_name": ["Company Name"],
        "country": ["Country"],
        "city": ["City"],
        "currency": ["Currency"],
        "asset_number": ["Asset Number"],
        "asset_desc": ["Asset Description"],
        "depr_key": ["Depreciation key"],
        "plant_desc": ["Plant Description"],
        "location": ["Location"],
        "business_area": ["Business Area"],
        "created_by": ["Created By"],
        "changed_by": ["Changed By"],
        "current_book_value": ["Current Book Value"],
        "acquisition_value": ["Acquisition Value"],
        "accumulated_depreciation": ["Accumulated Depreciation"],
        "excess_depr": ["Excess Depreciation"],
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
        rf"data_files/FJDE27_Exception{int(exc_id):02}.csv",
        rf"data_files/FJDE27_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None