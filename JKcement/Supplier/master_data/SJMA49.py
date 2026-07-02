# Supplier/master_data/SJMA49.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJMA49",
    "name": "Duplicate Vendor with Outstanding and Opposite Balance",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")},
        {"id": "3", "label": "Exception 03", "title": get_exception_title("Exception 03")},
        {"id": "4", "label": "Exception 04", "title": get_exception_title("Exception 04")},
        {"id": "5", "label": "Exception 05", "title": get_exception_title("Exception 05")},
        {"id": "6", "label": "Exception 06", "title": get_exception_title("Exception 06")},
        {"id": "7", "label": "Exception 07", "title": get_exception_title("Exception 07")}
    ],
    "columns": {
        "company": ["Company Name", "Company Code"],
        "vendor": ["Vendor Name", "Vendor Code"],
        "vendor_code": ["Vendor Code"],
        "vendor_code_right": ["Vendor Code (Right)"],
        "vendor_name": ["Vendor Name"],
        "account_group": ["Account group"],
        "country": ["Country"],
        "pan_number": ["PAN Number"],
        "tax_number": ["Tax Registration No.", "Tax Number"],
        "bank_acct": ["Bank Account Number"],
        "bank_country": ["Bank Country"],
        "exception_type": ["Exception"],
        "date": ["Created On"],
        "debit": ["Debit"],
        "credit": ["Credit"],
        "total_debit": ["Total Debit"],
        "total_credit": ["Total Credit"],
        "net_outstanding": ["Net Outstanding"],
        "amount": ["Net Outstanding"]
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
        rf"data_files/SJMA49_Exception{int(exc_id):02}.csv",
        rf"data_files/SJMA49_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
