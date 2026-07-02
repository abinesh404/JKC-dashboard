# Supplier/master_data/SJMA46.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJMA46",
    "name": "Identify Duplicate Vendors in the System",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")},
        {"id": "3", "label": "Exception 03", "title": get_exception_title("Exception 03")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Code"],
        "vendor_group": ["Vendor account group"],
        "country": ["Country Key"],
        "vendor": ["Vendor code ", "Vendor code", " Vendor code"],
        "vendor_name": ["NAME1_Ven"],
        "amount": ["Amount_LC", "Amount in Local Currency", "Sum(Amount_LC)"],
        "amount_lc": ["Amount_LC", "Amount in Local Currency"],
        "date": ["Posting Date in the Document"],
        "blocked_flag": ["BLOCKED_FLAG"],
        "vendorcode_count": ["Vendorcode_count"],
        "vendor_count2": ["Vendor_Count2"],
        "base_key": ["Base_Key"]
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
        rf"data_files/SJMA46_Exception{int(exc_id):02}.csv",
        rf"data_files/SJMA46_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
