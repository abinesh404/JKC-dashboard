# Supplier/invoice/SJIN11.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJIN11",
    "name": "Mismatch Invoice and PO Quantity and Amount",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Name", "Company Code"],
        "plant": ["Plant"],
        "po_vendor": ["PO_Vendor"],
        "invoice_vendor": ["Invoice_Vendor"],
        "purchasing_org": ["Purchasing Organization"],
        "purchasing_group": ["Purchasing Group"],
        "po_amt": ["PO_Amt"],
        "invoice_amt": ["Invoice_Amt"],
        "variance_amt": ["variance_amt"],
        "date": ["Posting Date"],
        "amount": ["Invoice_Amt"]
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
        rf"data_files/SJIN11_Exception{int(exc_id):02}.csv",
        rf"data_files/SJIN11_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None