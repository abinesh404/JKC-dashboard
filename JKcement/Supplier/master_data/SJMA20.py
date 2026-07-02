# Supplier/master_data/SJMA20.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJMA20",
    "name": "To identify transactions where Vendor to Vendor & Vendor to customer Transfers have been made",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Code"],
        "vendor": ["Vendor", "OffAccNo"],
        "customer": ["Customer Number"],
        "fiscal_year": ["Fiscal Year"],
        "amount": ["Amount_LC_Converted", "Amount in LC", "Amount"],
        "date": ["Posting Date", "Document Date", "Clearing Date", "Created On"],
        "user": ["User Name", "Created By"],
        "clearing_doc": ["Clearing Document"],
        "offacc_grp_desc": ["OffAcc_Grp_Desc"],
        "cust_acct_grp": ["Cust Account Group", "Cust Account group"]
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
        rf"data_files/SJMA20_Exception{int(exc_id):02}.csv",
        rf"data_files/SJMA20_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
