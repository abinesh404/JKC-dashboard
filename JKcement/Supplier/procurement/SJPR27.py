# Supplier/procurement/SJPR27.py — High Price PO – Minimum & Average Price (Six Month)
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR27",
    "name": "High Price PO – Minimum & Average Price (Six Month)",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": [
            "Company Code",
            "Company Name",
            "City",
            "Country Code"
        ],
        "company_name": [
            "Company Name"
        ],
        "plant": [
            "Plant",
            "Storage Location"
        ],
        "vendor": [
            "Vendor Number",
            "Customer Number",
            "Payment Terms"
        ],
        "material": [
            "Material Number",
            "Material Description",
            "Material Group"
        ],
        "material_desc": [
            "Material Description"
        ],
        "qty": [
            "Quantity Ordered"
        ],
        "amount": [
            "Net Value (Total Amount)"
        ],
        "unit_price": [
            "Net Price (per unit)"
        ],
        "price": [
            "Min_Price",
            "Avg_Price",
            "Net Price (per unit)"
        ],
        "po": [
            "Purchase Order Number",
            "Purchase Order Item Number",
            "Purchase Order Category",
            "Document Type",
            "Item Category"
        ],
        "date": [
            "Document Date in Document",
            "Date on Created",
            "Month",
            "six month Period"
        ],
        "created_date": [
            "Date on Created"
        ],
        "user": [
            "Created By"
        ],
        "prediction": [
            "prediction"
        ],
        "six_month_period": [
            "six month Period"
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
        rf"data_files/SJPR27_Exception{int(exc_id):02}.csv",
        rf"data_files/SJPR27_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None