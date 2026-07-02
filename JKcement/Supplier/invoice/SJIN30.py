# Supplier/invoice/SJIN30.py
import pandas as pd
import os

CONFIG = {
    "id": "SJIN30",
    "name": "PO Items Where GR Based IV Indicator is Not Activated",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Name", "Company Code"],
        "vendor": ["Vendor Name", "Vendor Code"],
        "plant": ["Plant Name", "Plant Code"],
        "po_amount": ["PO Amount"],
        "invoice_amount": ["Invoice Amount"],
        "po_number": ["Purchasing Document Number"],
        "purchasing_group": ["Puchasing Group", "Purchasing Group"],
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
        rf"data_files/SJIN30_Exception{int(exc_id):02}.csv",
        rf"data_files/SJIN30_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None