# Finance/Accounting/FJAC8.py — Non-usage GL Accounts
# -------------------------------------------------------------------------

import pandas as pd
import os
import numpy as np
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC8",
    "name": "Non-usage GL Accounts",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "coa": ["Chart of Accounts", "KTOPL"],
        "gl": ["G/L Account Number", "SAKNR"],
        "acc_group": ["G/L Account Group", "KTOKS"],
        "created_by": ["Created By", "ERNAM"],
        "created_on": ["Created On", "ERDAT"],
        "is_bs": ["Balance Sheet Account Indicator", "XBILK"],
        "del_flag": ["Indicator: Account marked for deletion", "LOEVM"],
        "block_flag": ["Indicator: Is Account Blocked for Posting", "SPERR"],
        "status": ["GL Status", "Status"],
        "is_not_used": ["is_not_used"],
        "is_used": ["is_used"],
        "usage_label": ["usage_label"],
        "account_type": ["account_type"],
        "recent_unused": ["recent_unused"],
        "date": ["Created On", "ERDAT"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    paths = [
        rf"data_files/FJAC8_Exception{int(exc_id):02}.csv",
        rf"data_files/FJAC8_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None