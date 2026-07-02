# Supplier/master_data/SJMA48.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJMA48",
    "name": "Blacklisted vendors",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Name", "Company Code"],
        "vendor": ["Vendor Name", "Vendor Code"],
        "plant": ["Plant"],
        "location": ["City", "Country key"],
        "amount": ["Amount"],
        "date": ["Posting Date", "Document Date"]
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
        rf"data_files/SJMA48_Exception{int(exc_id):02}.csv",
        rf"data_files/SJMA48_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
