# Supplier/procurement/SJPR25.py — Invoice Date Prior to PO Date – Part II
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR25",
    "name": "Invoice Date Prior to PO Date – Part II",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")},
        {"id": "3", "label": "Exception 03", "title": get_exception_title("Exception 03")}
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
        "plant": [
            "Plant Code",
            "Plant Name",
            "Plant City"
        ],
        "plant_name": [
            "Plant Name"
        ],
        "vendor": [
            "Vendor Code",
            "Vendor Name",
            "Vendor City"
        ],
        "vendor_name": [
            "Vendor Name"
        ],
        "material": [
            "Material Number",
            "Item Text"
        ],
        "qty": [
            "Quantity"
        ],
        "amount": [
            "Amount in document currency"
        ],
        "po": [
            "Purchasing Document Number",
            "Item Number of Purchasing Document",
            "Purchasing Document Type"
        ],
        "purch_group": [
            "Purchasing Group"
        ],
        "invoice": [
            "Accounting Document Number",
            "Document Type",
            "Document Item in Invoice Document"
        ],
        "invoice_date": [
            "Invoice Date"
        ],
        "entry_date": [
            "Entry Date"
        ],
        "posting_date": [
            "Posting Date in the Document"
        ],
        "date": [
            "Invoice Date",
            "PO Date",
            "Entry Date",
            "Posting Date in the Document"
        ],
        "user": [
            "User name",
            "Entered by external system user",
            "Name of Person who Created the Object"
        ]
    }
}


def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Supplier Procurement"
    }


def get_data(exc_id):
    paths = [
        rf"data_files/SJPR25_Exception{int(exc_id):02}.csv",
        rf"data_files/SJPR25_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None