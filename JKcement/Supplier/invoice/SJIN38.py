# Supplier/invoice/SJIN38.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJIN38",
    "name": "Duplicate Vendor Invoices - II",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")},
        {"id": "3", "label": "Exception 03", "title": get_exception_title("Exception 03")},
        {"id": "4", "label": "Exception 04", "title": get_exception_title("Exception 04")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Name", "Company Code"],
        "vendor": ["Vendor Name1", "Vendor"],
        "fiscal_year": ["Fiscal Year"],
        "amount_lc": ["Amount LC"],
        "region": ["REGION"],
        "country": ["Country"],
        "payment_method": ["Payment method"],
        "user_name": ["User Name"],
        "doc_type": ["Document Type", "Document type"],
        "date": ["Posting Date"],
        "reference_number": ["Reference Number"],
        "amount": ["Amount LC"]
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
        rf"data_files/SJIN38_Exception{int(exc_id):02}.csv",
        rf"data_files/SJIN38_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None