# Supplier/master_data/SJMA50.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJMA50",
    "name": "Vendor Employee Name & Address Check",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Name", "Company Code"],
        "vendor": ["Vendor code"],
        "employee_code": ["Employee code"],
        "vendor_group": ["Vendor Account group"],
        "vendor_country": ["Vendor Country"],
        "employee_country": ["Employee Country"],
        "vendor_city": ["Vendor City"],
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
        rf"data_files/SJMA50_Exception{int(exc_id):02}.csv",
        rf"data_files/SJMA50_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
