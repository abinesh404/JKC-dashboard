# Supplier/master_data/SJMA6.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJMA6",
    "name": "Detect the Inactive Vendors",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": [
            "Company Code",
            "Company Name"
        ],
        "vendor": [
            "Vendor",
            "Vendor Name"
        ],
        "plant": [
            "Plant"
        ],
        "location": [
            "Company City",
            "Vendor City",
            "Vendor Country",
            "Vendor Region"
        ],
        "amount": [
            "Total_Amount",
            "Open_Balance"
        ],
        "open_balance": [
            "Open_Balance"
        ],
        "activity": [
            "Transaction_Count",
            "Last_Posting_Date",
            "Posting Date",
            "Document Date"
        ],
        "transaction_count": [
            "Transaction_Count"
        ],
        "date": [
            "Clearing Date",
            "Posting Date",
            "Document Date",
            "Last_Posting_Date"
        ],
        "months_inactive": [
            "Months_Inactive"
        ],
        "inactivity_aging": [
            "Inactivity Aging"
        ],
        "account_group": [
            "Account Group"
        ],
        "vendor_details": [
            "Account Group",
            "Search Term 1",
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
        rf"data_files/SJMA6_Exception{int(exc_id):02}.csv",
        rf"data_files/SJMA6_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
