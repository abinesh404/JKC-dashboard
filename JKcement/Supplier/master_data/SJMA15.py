# Supplier/master_data/SJMA15.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJMA15",
    "name": "Dormant Vendor Accounts Not Blocked",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": [
            "Company Code",
            "Company Name"
        ],
        "company_name": [
            "Company Name"
        ],
        "vendor": [
            "Vendor",
            "Vendor Name"
        ],
        "plant": [
            "Plant"
        ],
        "account_group": [
            "Account Group"
        ],
        "status": [
            "Status",
            "Posting Block",
            "Deletion Flag"
        ],
        "net_outstanding": [
            "Net_Outstanding",
            "Net Outstanding"
        ],
        "amount": [
            "Net_Outstanding",
            "Net Outstanding"
        ],
        "date": [
            "Created On"
        ]
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
        rf"data_files/SJMA15_Exception{int(exc_id):02}.csv",
        rf"data_files/SJMA15_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
