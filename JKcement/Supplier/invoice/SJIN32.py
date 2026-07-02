# Supplier/invoice/SJIN32.py
import pandas as pd
import os

CONFIG = {
    "id": "SJIN32",
    "name": "IV Quantity Exceeds GRN Quantity and Payment Done",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Code"],
        "vendor": ["Vendor Account Number"],
        "plant": ["Plant"],
        "amount_lc": ["Amount in Local Currency"],
        "grn_qty": ["Q+Sum(Derived_Quantity)"],
        "excess_qty": ["excess_qty"],
        "po_number": ["Purchasing Document Number"],
        "po_type": ["Purchasing Document Type"],
        "date": ["Posting Date in the Document"],
        "amount": ["Amount in Local Currency"]
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
        rf"data_files/SJIN32_Exception{int(exc_id):02}.csv",
        rf"data_files/SJIN32_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None