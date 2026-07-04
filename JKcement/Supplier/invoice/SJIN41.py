# Supplier/invoice/SJIN41.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJIN41",
    "name": "PO Change After GRN",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")},
        {"id": "3", "label": "Exception 03", "title": get_exception_title("Exception 03")},
        {"id": "4", "label": "Exception 04", "title": get_exception_title("Exception 04")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Name", "Company Code"],
        "vendor": ["Vendor Code"],
        "vendor_name": ["Vendor Name"],
        "po": ["Object Value (Purchase Order Number)"],
        "purchasing_group": ["Purchasing Group"],
        "amount": ["Amount in Local Currency", "Net Order Price"],
        "date": ["Date of change", "PO Document date"],
        "days_after_grn": ["Change Date - GRN Date"],
        "field_description": ["Field Description"],
        "re_release_triggered": ["Re-Release Trigerred", "Re-Release Triggered Due to Change"],
        "user": ["User"],
        "document_number": ["Document Number"]
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
        rf"data_files/SJIN41_Exception{int(exc_id):02}.csv",
        rf"data_files/SJIN41_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None