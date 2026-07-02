# Supplier/procurement/SJPR9.py — Split Purchase Requisition
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR9",
    "name": "Split Purchase Requisition",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": [
            "Company Code",
            "Company Name",
            "City",
            "Country"
        ],
        "company_name": [
            "Company Name"
        ],
        "plant": [
            "Plant",
            "Storage Location"
        ],
        "vendor": [
            "Vendor",
            "Related_Vendor"
        ],
        "material": [
            "Material Number",
            "Material Description",
            "Material Group",
            "Material Type",
            "Old Material Number"
        ],
        "material_group": [
            "Material Group"
        ],
        "qty": [
            "Quantity",
            "Related_Quantity"
        ],
        "pr": [
            "Purchase Requisition Number",
            "Related PR No."
        ],
        "date": [
            "Creation Date",
            "Related PR Date",
            "Last Change Date"
        ],
        "user": [
            "Created By"
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
        rf"data_files/SJPR9_Exception{int(exc_id):02}.csv",
        rf"data_files/SJPR9_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None