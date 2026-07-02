# Supplier/payment/SJPA23.py
import pandas as pd
import os
from .template import get_exception_title, get_chart_title

CONFIG = {
    "id": "SJPA23",
    "name": "Delayed & Early Payment to Vendors from Due Date",
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
        "company_name": [
            "Company Name"
        ],
        "vendor": [
            "Vendor Code",
            "Vendor Name1",
            "Vendor Name2",
            "Vendor City",
            "Vendor District",
            "Vendor account group",
            "Vendor Account Group Description"
        ],
        "amount": [
            "Amount in Local Currency",
            "Amount in Document Currency",
            "Currency"
        ],
        "document": [
            "Accounting Document Number",
            "Document Number of the Clearing Document",
            "Document Type",
            "Fiscal Yaer",
            "Number of Line Item Within Accounting Document",
            "Clearing Item"
        ],
        "date": [
            "Clearing Date",
            "Document Date in Document",
            "Posting Date",
            "Due Date",
            "Clearing Entry Date",
            "Baseline Date for Due Date Calculation"
        ],
        "clearing_date": [
            "Clearing Date"
        ],
        "delay": [
            "Difference Clearing Date and Due Date"
        ],
        "payment": [
            "Payment Method",
            "Payment Block Key",
            "List of the Payment Methods to be Considered"
        ],
        "payment_method": [
            "Payment Method"
        ],
        "business": [
            "Type of Business",
            "Type of Industry"
        ],
        "age_bucket": [
            "Age Bucket"
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
        rf"data_files/SJPA23_Exception{int(exc_id):02}.csv",
        rf"data_files/SJPA23_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None