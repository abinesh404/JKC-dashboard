# Supplier/invoice/SJIN33.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJIN33",
    "name": "IV Quantity Exceeds GRN Quantity",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Name", "Company Code"],
        "vendor": ["Vendor Name1", "Vendor Code"],
        "plant": ["Plant Name", "Plant Code"],
        "invoice_amount": ["Invoice Amount"],
        "excess_qty": ["(IV Qty - GR Qty)"],
        "amount_lc": ["Amount in Local Currency"],
        "po_number": ["Purchasing Document Number"],
        "purchasing_group": ["Purchasing Group"],
        "date": ["Posting Date"],
        "amount": ["Invoice Amount"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Supplier Invoice"
    }

def get_data(exc_id):
    paths = [
        rf"data_files/SJIN33_Exception{int(exc_id):02}.csv",
        rf"data_files/SJIN33_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None