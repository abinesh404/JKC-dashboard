# Finance/Accounting/FJAC12.py — Unauthorised MIRO Entries
# -------------------------------------------------------------------------

import pandas as pd
import os
import numpy as np
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC12",
    "name": "Unauthorised MIRO Entries",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "amount":       ["Amount"],
        "vendor":       ["Vendor Name", "Vendor"],
        "vendor_name":  ["Vendor Name"],
        "date":         ["Posting Date"],
        "miro_user":    ["MIRO Created User"],
        "company":      ["Company Code"],
        "year":         ["Fiscal Year"],
        "tcode":        ["Transaction Code"],
        "valid_from":   ["User Valid From Date"],
        "valid_to":     ["User Valid To Date"],
        "user_type":    ["User Type"],
        "user_group":   ["User Group"],
        "is_miro":      ["is_miro"],
        "is_exception": ["is_exception"],
        "affected_amount": ["affected_amount"],
        "status_label": ["status_label"],
        "unauth_user":  ["unauth_user"],
        "unauth_vendor": ["unauth_vendor"],
        "posting_date_dt": ["Posting Date"],
        "user_type_group": ["user_type_group"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    paths = [
        rf"data_files/FJAC12_Exception{int(exc_id):02}.csv",
        rf"data_files/FJAC12_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None