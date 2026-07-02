# Supplier/payment/SJPA52.py
import pandas as pd
import os
from .template import get_exception_title, get_chart_title

CONFIG = {
    "id": "SJPA52",
    "name": "Non Routine Transactions",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")},
        {"id": "3", "label": "Exception 03", "title": get_exception_title("Exception 03")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": [
            "Company Code"
        ],
        "vendor": [
            "Account Number vendor",
            "Name1",
            "Vendor account group"
        ],
        "plant": [
            "Plant"
        ],
        "amount": [
            "Amount in Local Currency",
            "Amount in document currency"
        ],
        "document": [
            "Accounting Document Number",
            "Purchasing Document Number"
        ],
        "date": [
            "Clearing Date",
            "Document Date in Document",
            "Posting Date in the Document",
            "Day  Acc. Doc. Entered"
        ],
        "clearing_date": [
            "Clearing Date"
        ],
        "account": [
            "General Ledger Account",
            "G/L Account Number"
        ],
        "duplicate_payment": [
            "Duplicate-flag",
            "Duplicate_Flag_Num"
        ],
        "high_payment": [
            "High_Payment_Flag"
        ],
        "delay": [
            "Diff_Days"
        ],
        "reference": [
            "Reference Key"
        ],
        "transaction_code": [
            "Transaction Code"
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
        rf"data_files/SJPA52_Exception{int(exc_id):02}.csv",
        rf"data_files/SJPA52_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None