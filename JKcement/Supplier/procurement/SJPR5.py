# Supplier/procurement/SJPR5.py — Single Source Vendors
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR5",
    "name": "Single Source Vendors",
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
        "material": [
            "Material Number",
            "Material Type",
            "Material Group",
            "Material Description"
        ],
        "material_group": [
            "Material Group"
        ],
        "qty": [
            "Purchase Order Quantity"
        ],
        "amount": [
            "Net Price in Purchasing Document (in Document Currency)"
        ],
        "po": [
            "Purchasing Document Number",
            "Item Number of Purchasing Document",
            "Purchasing Document Type",
            "Purchasing Document Category"
        ],
        "date": [
            "Purchasing Document Date"
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
        rf"data_files/SJPR5_Exception{int(exc_id):02}.csv",
        rf"data_files/SJPR5_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None