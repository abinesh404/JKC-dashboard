# Fixed_Asset/ITAC/FJIT24.py
import pandas as pd
import os

CONFIG = {
    "id": "FJIT24",
    "name": "Asset Capitalisation Date as per Masters vs Asset Capitalisation Entry Date",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
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
        rf"data_files/FJIT24_Exception{int(exc_id):02}.csv",
        rf"data_files/FJIT24_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None