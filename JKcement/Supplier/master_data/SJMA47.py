# Supplier/master_data/SJMA47.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJMA47",
    "name": "Excess Payment to Vendor with Unadjusted Advances",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Name"],
        "vendor": ["Vendor Name"],
        "special_gl": ["Special G/L Indicator"],
        "invoice_amt": ["Invoice Amount Paid"],
        "advance_amt": ["Total Unadjusted Advance Amount"],
        "open_advance_docs": ["Open Advance Document Numbers"],
        "open_advance_count": ["Count of Open Advance Posting Date"],
        "date": ["Date the Payment was Made"],
        "amount": ["Invoice Amount Paid"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Supplier Master Data"
    }

def get_data(exc_id):
    paths = [
        rf"data_files/SJMA47_Exception{int(exc_id):02}.csv",
        rf"data_files/SJMA47_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
