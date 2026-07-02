# Supplier/procurement/SJPR2.py — Open Purchase Order
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR2",
    "name": "Open Purchase Order",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": [
            "Company Code"
        ],
        "plant": [
            "Plant",
            "Storage Location",
            "City",
            "Region"
        ],
        "vendor": [
            "Vendor Account Number",
            "Name 1"
        ],
        "material": [
            "Material Number"
        ],
        "qty": [
            "Purchase Order Quantity",
            "Quantity_MSEG"
        ],
        "open_qty": [
            "Open_Qty"
        ],
        "amount": [
            "Amount in document currency",
            "Billed_Amount",
            "Open_Amount",
            "Net Order Value in PO Currency",
            "Gross order value in PO currency"
        ],
        "billed_amount": [
            "Billed_Amount"
        ],
        "open_amount": [
            "Open_Amount"
        ],
        "date": [
            "Purchasing Document Date",
            "Purchase Order Document Date"
        ],
        "region": [
            "City",
            "Region"
        ],
        "po": [
            "Purchasing Document Number"
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
        rf"data_files/SJPR2_Exception{int(exc_id):02}.csv",
        rf"data_files/SJPR2_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None