# Supplier/master_data/SJMA51.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJMA51",
    "name": "Vendor Foreign Account",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "vendor": ["Vendor code"],
        "vendor_country": ["Vendor Country"],
        "vendor_name": ["Vendor_Name"],
        "vendor_group": ["Vendor Account group"],
        "bank_country": ["Vendor Bank Country"],
        "bank_acct": ["Vendor Bank Account"],
        "date": ["Vendor Created on"],
        "created_by": ["Vendor Created by"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Supplier Master Data"
    }

def get_data(exc_id):
    paths = [
        rf"data_files/SJMA51_Exception{int(exc_id):02}.csv",
        rf"data_files/SJMA51_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
