# Supplier/payment/SJPA19.py
import pandas as pd
import os
from .template import get_exception_title, get_chart_title

CONFIG = {
    "id": "SJPA19",
    "name": "Payee Name in Cheque Payments is Different from Vendor Name or Alternate Payee",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": [
            "Company Code",
            "Company Name",
            "Company City"
        ],
        "vendor": [
            "Vendor Code",
            "Vendor Name1",
            "Vendor Name2"
        ],
        "customer": [
            "Customer Code",
            "Customer Name1",
            "Customer Name2"
        ],
        "payee": [
            "Name of the Payee1",
            "Name of the Payee2",
            "Account Number of Alternate Payee"
        ],
        "cheque_details": [
            "Check Number",
            "Check Number From",
            "Check Type",
            "Replacement Check Number"
        ],
        "amount": [
            "Amount",
            "Currency"
        ],
        "date": [
            "Print Date",
            "Print Time",
            "Probable Payment Date (Cash Discount 1 Due)"
        ],
        "user": [
            "Print User",
            "Creation User"
        ],
        "address": [
            "City",
            "Street"
        ],
        "master_data_status": [
            "Central Deletion Flag",
            "Central Posting Block",
            "Centrally Imposed Purchasing Block",
            "Payment Block",
            "Central Deletion Block for Master Record"
        ],
        "exception": [
            "Exception"
        ]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Supplier Payment"
    }

def get_data(exc_id):
    paths = [
        rf"data_files/SJPA19_Exception{int(exc_id):02}.csv",
        rf"data_files/SJPA19_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None