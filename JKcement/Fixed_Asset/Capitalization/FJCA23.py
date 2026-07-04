# Fixed_Asset/Capitalization/FJCA23.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "FJCA23",
    "name": "Delay in Capitalisation (Changes to the Date)",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
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
        rf"data_files/FJCA23_Exception{int(exc_id):02}.csv",
        rf"data_files/FJCA23_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None