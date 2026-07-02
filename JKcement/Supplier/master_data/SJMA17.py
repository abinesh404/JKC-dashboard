# Supplier/master_data/SJMA17.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJMA17",
    "name": "Vendor Bank Information Changed for Releasing the Payment and After Payout the Original Details Updated",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Description", "Company Code"],
        "vendor": ["Vendor Name", "Vendor Code"],
        "user": ["User name of the person responsible in change document", "Name of Person who Created the Object"],
        "change_type": ["Change Type (U, I, S, D)", "Application object change type (U, I, E, D)"],
        "date": ["Creation date of the change document", "Creation date of the change document (Change 2)"],
        "amount": ["Amount in Local Currency"],
        "document": ["Accounting Document Number", "Document Number of the Clearing Document"],
        "bank_acc": ["Bank account number"],
        "change_num": ["Document change number"]
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
        rf"data_files/SJMA17_Exception{int(exc_id):02}.csv",
        rf"data_files/SJMA17_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
