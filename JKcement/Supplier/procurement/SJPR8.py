# Supplier/procurement/SJPR8.py — Time gap PO vs GRN Date
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR8",
    "name": "Time gap PO vs GRN Date",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")},
        {"id": "3", "label": "Exception 03", "title": get_exception_title("Exception 03")}
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
        "plant": [
            "Plant Code",
            "City",
            "Country Key"
        ],
        "plant_code": [
            "Plant Code"
        ],
        "vendor": [
            "Vendor"
        ],
        "material": [
            "Material No",
            "Material"
        ],
        "po": [
            "Purchasing Document",
            "Purchase Group"
        ],
        "purch_group": [
            "Purch. Group",
            "Purchase Group"
        ],
        "mat_doc": [
            "Material Document",
            "Material Doc. Item"
        ],
        "qty": [
            "Quantity",
            "Del. Note Quantity"
        ],
        "amount": [
            "Amount in LC",
            "PO_Derived_Price",
            "GRN_Derived_Price",
            "Material_Net_Price",
            "Price_Diff"
        ],
        "price_diff": [
            "Price_Diff"
        ],
        "po_price": [
            "PO_Derived_Price"
        ],
        "grn_price": [
            "GRN_Derived_Price"
        ],
        "date": [
            "Document Date",
            "Posting Date",
            "Entry Date",
            "Created On"
        ],
        "user": [
            "User name",
            "Created by"
        ],
        "movement_type": [
            "Movement Type_EKBE"
        ],
        "delay_days": [
            "date&time diff"
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
        rf"data_files/SJPR8_Exception{int(exc_id):02}.csv",
        rf"data_files/SJPR8_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None