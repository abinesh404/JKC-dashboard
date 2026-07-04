# Fixed_Asset/Master_Data/FJMA26.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "FJMA26",
    "name": "Changes to Useful Life of Asset",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
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
        rf"data_files/FJMA26_Exception{int(exc_id):02}.csv",
        rf"data_files/FJMA26_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None