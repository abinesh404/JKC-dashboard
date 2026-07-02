# Supplier/master_data/SJMA44.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJMA44",
    "name": "Payment by Creating One Time Vendor Account",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Description", "Company Code"],
        "vendor": ["Vendor Name", "Vendor Code"],
        "vendor_code": ["Vendor Code"],
        "plant": ["Plant Code"],
        "account_group": ["Vendor account group"],
        "account_group_desc": ["Vendor Account Group Description"],
        "amount": ["Amount in Local Currency"],
        "date": ["Posting Date in the Document", "Document Date in Document", "Clearing Date"],
        "user": ["Name of Person who Created the Object"],
        "document": ["Accounting Document Number"]
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
        rf"data_files/SJMA44_Exception{int(exc_id):02}.csv",
        rf"data_files/SJMA44_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
