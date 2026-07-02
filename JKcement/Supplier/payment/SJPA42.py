# Supplier/payment/SJPA42.py
import pandas as pd
import os
from .template import get_exception_title, get_chart_title

CONFIG = {
    "id": "SJPA42",
    "name": "Payment to Blocked Invoices",
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
            "Vendor Code",
            "Vendor Name"
        ],
        "amount": [
            "Amount in Local Currency",
            "Amount in document currency"
        ],
        "document": [
            "Accounting Document Number",
            "Document Type"
        ],
        "gl": [
            "G/L Account Number",
            "General Ledger Account"
        ],
        "date": [
            "Posting Date",
            "Document Date in Document",
            "Due date of an invoice"
        ],
        "payment_block": [
            "Payment Block Key",
            "Payment Block Key(BSEG)",
            "Logistics payment block"
        ],
        "payment_method": [
            "Payment Method (REGUP)"
        ],
        "user": [
            "User name"
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
        rf"data_files/SJPA42_Exception{int(exc_id):02}.csv",
        rf"data_files/SJPA42_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None