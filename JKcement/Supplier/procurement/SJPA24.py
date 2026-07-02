# Supplier/procurement/SJPA24.py — Invoice Date prior to PO date
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPA24",
    "name": "Invoice Date prior to PO date",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
            "company": [
                    "Company Code",
                    "Company Name"
            ],
            "plant": [
                    "Plant Code",
                    "Plant Name",
                    "Plant City"
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
            "vendor": [
                    "Vendor Name",
                    "Vendor Code"
            ],
            "prior_days": [
                    "Invoice Date Prior to PO Date"
            ],
            "date": [
                    "Invoice Date",
                    "PO Date"
            ],
            "po": [
                    "Purchasing Document Number",
                    "Accounting Document Number"
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
        rf"data_files/SJPA24_Exception{int(exc_id):02}.csv",
        rf"data_files/SJPA24_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None