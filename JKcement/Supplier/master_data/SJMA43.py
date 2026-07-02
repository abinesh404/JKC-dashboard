# Supplier/master_data/SJMA43.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJMA43",
    "name": "Vendors with debit balances & ageing",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Name", "Company Code"],
        "vendor": ["Vendor Name", "Vendor Code"],
        "plant": ["Plant"],
        "location": ["City", "ZIP/Pin code", "REGION", "Country key"],
        "amount": ["Amount in local currency"],
        "date": ["Posting Date", "document date", "Clearing Date"],
        "document": ["document number", "Clearing document no."]
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
        rf"data_files/SJMA43_Exception{int(exc_id):02}.csv",
        rf"data_files/SJMA43_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
