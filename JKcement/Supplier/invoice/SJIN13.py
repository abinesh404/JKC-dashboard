# Supplier/invoice/SJIN13.py
import pandas as pd
import os

CONFIG = {
    "id": "SJIN13",
    "name": "Unplanned Delivery Cost More Than 5% of Gross Invoice Value",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Code Name", "Company Code"],
        "vendor": ["Vendor Number"],
        "plant": ["Plant Name", "Plant"],
        "gross_invoice_amount": ["Gross Invoice Amount"],
        "unplanned_delivery_cost": ["Unplanned Delivery Cost"],
        "pct_unplanned_delivery_cost": ["% of Unplanned Delivery Cost"],
        "date": ["Posting Date"],
        "user_name": ["User Name (who posted)"],
        "po_number": ["PO Number"],
        "amount": ["Gross Invoice Amount"]
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
        rf"data_files/SJIN13_Exception{int(exc_id):02}.csv",
        rf"data_files/SJIN13_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None