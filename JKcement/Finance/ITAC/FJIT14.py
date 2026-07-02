# Finance/ITAC/FJIT14.py
import pandas as pd
import os

CONFIG = {
    "id": "FJIT14",
    "name": "PO Quantity Exceeds PR Quantity",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company_code": ["Company Code"],
        "plant": ["Plant"],
        "vendor_name": ["Vendor Name"],
        "region": ["Region"],
        "city": ["City"],
        "purch_org": ["Purchasing Organization"],
        "purch_group": ["Purchasing Group"],
        "purch_doc_type": ["Purchasing Document Type"],
        "pr_blocked": ["Purchase Requisition Blocked"],
        "pr_state": ["Requisition Processing State"],
        "material_code": ["Material Number"],
        "material_desc": ["Material Description"],
        "batch_number": ["Batch Number"],
        "purch_doc_num": ["Purchasing Document Number"],
        "vendor_code": ["Vendor Account Number"],
        "company_name": ["Name of Company"],
        "purch_doc_date": ["Purchasing Document Date"],
        "qty_diff": ["Qty_Diff"],
        "excess_value": ["Excess Procurement Value"],
        "date": ["Purchasing Document Date"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "ITAC"
    }

def get_data(exc_id):
    paths = [
        rf"data_files/FJIT14_Exception{int(exc_id):02}.csv",
        rf"data_files/FJIT14_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None