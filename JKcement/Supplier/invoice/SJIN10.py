# Supplier/invoice/SJIN10.py
import pandas as pd
import os

CONFIG = {
    "id": "SJIN10",
    "name": "Mismatch Invoice and PO Vendor",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Name", "Company Code"],
        "plant": ["Plant"],
        "po_vendor": ["PO Vendor"],
        "invoice_vendor": ["Invoice Vendor"],
        "date": ["Document Date"],
        "amount_doc": ["Amount in Document Currency"],
        "amount": ["Amount in Document Currency"]
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
        rf"data_files/SJIN10_Exception{int(exc_id):02}.csv",
        rf"data_files/SJIN10_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None