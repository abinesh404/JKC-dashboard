# Supplier/invoice/SJIN40.py
import pandas as pd
import os

CONFIG = {
    "id": "SJIN40",
    "name": "Single Source Vendor - Company Level",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Name", "Company Code"],
        "vendor": ["Vendor Code"],
        "vendor_name": ["Vendor Name"],
        "material": ["Material Number"],
        "material_group": ["Material Group"],
        "net_price": ["Net Price in Purchasing Document (in Document Currency)"],
        "po_qty": ["Purchase Order Quantity"],
        "purchasing_group": ["Purchasing Group"],
        "date": ["Purchasing Document Date"],
        "amount": ["Net Price in Purchasing Document (in Document Currency)"]
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
        rf"data_files/SJIN40_Exception{int(exc_id):02}.csv",
        rf"data_files/SJIN40_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None