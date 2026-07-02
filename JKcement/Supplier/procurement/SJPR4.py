# Supplier/procurement/SJPR4.py — PO with non-global address
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR4",
    "name": "PO with non-global address",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": [
            "Company Code"
        ],
        "plant": [
            "Plant",
            "PLANT_NAME1",
            "PLANT_CITY1",
            "PLANT_REGION",
            "PLANT_COUNTRY"
        ],
        "vendor": [
            "Account Number of Vendor",
            "Vendor Name",
            "Address_Vendor"
        ],
        "po": [
            "Purchasing Document Number"
        ],
        "material": [
            "Material Number"
        ],
        "amount": [
            "Net PricePurchasing Doc."
        ],
        "date": [
            "Purchasing Document Date",
            "Date Record Was Created"
        ],
        "delivery_address": [
            "Delivery Address Number PO",
            "PO_NAME1",
            "PO_CITY1",
            "PO_POSTCODE",
            "PO_STREET",
            "PO_COUNTRY",
            "PO_REGION"
        ],
        "master_address": [
            "Address number plant",
            "PLANT_NAME1",
            "PLANT_CITY1",
            "PLANT_POSTCODE",
            "PLANT_STREET",
            "PLANT_COUNTRY",
            "PLANT_REGION"
        ],
        "po_region": [
            "PO_REGION"
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
        rf"data_files/SJPR4_Exception{int(exc_id):02}.csv",
        rf"data_files/SJPR4_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None