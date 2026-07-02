# Supplier/payment/SJPA21.py
import pandas as pd
import os
from .template import get_exception_title, get_chart_title

CONFIG = {
    "id": "SJPA21",
    "name": "Bank Payments without Vendor & Customer",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": [
            "Company Code",
            "Company Name",
            "City",
            "Country Key"
        ],
        "document": [
            "Document Number",
            "Fiscal Year",
            "Document Header Text",
            "Line Item Number",
            "Line Item Text"
        ],
        "gl_account": [
            "G/L Account",
            "Account Type",
            "Chart of Accounts",
            "Order Number"
        ],
        "business_partner": [
            "Vendor",
            "Customer"
        ],
        "amount": [
            "Amount in Local Currency",
            "Amount in Document Currency",
            "Currency",
            "Exchange Rate"
        ],
        "date": [
            "Posting Date",
            "Document Date",
            "Entry Date",
            "Entry Time",
            "Changed On",
            "Posting Period"
        ],
        "reference": [
            "Reference Key",
            "Reference Document Number",
            "Clearing Document No.",
            "Assignment Field"
        ],
        "cost_center": [
            "Cost Center"
        ],
        "profit_center": [
            "Profit Center"
        ],
        "user": [
            "User ID",
            "Transaction Code"
        ],
        "status": [
            "Payment Block",
            "Debit/Credit Indicator"
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
        rf"data_files/SJPA21_Exception{int(exc_id):02}.csv",
        rf"data_files/SJPA21_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None