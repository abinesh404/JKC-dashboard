# Supplier/procurement/SJPR1.py — Delay in PR to PO
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR1",
    "name": "Delay in PR to PO",
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
        "plant": [
            "Plant",
            "City"
        ],
        "material": [
            "Material",
            "PO_Material"
        ],
        "qty": [
            "Quantity"
        ],
        "amount": [
            "Net price"
        ],
        "vendor": [
            "Vendor"
        ],
        "pr": [
            "PR number"
        ],
        "po": [
            "PO number"
        ],
        "date": [
            "PO creation date"
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
        rf"data_files/SJPR1_Exception{int(exc_id):02}.csv",
        rf"data_files/SJPR1_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None