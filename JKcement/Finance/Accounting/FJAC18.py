# Finance/Accounting/FJAC18.py — Statistical Model for Expenses
# -------------------------------------------------------------------------

import pandas as pd
import os
import numpy as np
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC18",
    "name": "Statistical Model_Expense",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")},
        {"id": "3", "label": "Exception 03", "title": get_exception_title("Exception 03")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "amount":       ["Amount in Local Currency", "DMBTR"],
        "digit":        ["First_Digit"],
        "digit_count":  ["Count_of_Digit"],
        "deviation":    ["Deviation"],
        "z_score":      ["Z_Score"],
        "chi_square":   ["Chi_Square_Val"],
        "actual_pct":   ["Actual_percent"],
        "benford_prob": ["Benford_Prob"],
        "company":      ["Company Code", "BUKRS"],
        "year":         ["Fiscal Year", "GJAHR"],
        "gl":           ["General Ledger Account", "HKONT"],
        "cost_center":  ["Cost Center", "KOSTL"],
        "profit_center":["Profit Center", "PRCTR"],
        "user":         ["Username"],
        "vendor_code":  ["Vendor Code"],
        "vendor_name":  ["Vendor Name"],
        "posting_date_dt": ["Posting Date"],
        "is_exception": ["is_exception"],
        "status_label": ["status_label"],
        "flagged_amount":["flagged_amount"],
        "flagged_digit":["flagged_digit"],
        "crit_val":     ["crit_val"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    paths = [
        rf"data_files/FJAC18_Exception{int(exc_id):02}.csv",
        rf"data_files/FJAC18_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None