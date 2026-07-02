# Finance/Accounting/FJAC10.py — Documents of PY processed in CY with Ageing
# -------------------------------------------------------------------------

import pandas as pd
import os
import numpy as np
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC10",
    "name": "Vendor Documents of PY processed in CY with Ageing",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "amount":   ["Amount in Local Currency", "Amount", "DMBTR"],
        "vendor":   ["Vendor Number", "LIFNR", "Account"],
        "vendor_name": ["Vendor Name", "NAME1"],
        "date":     ["Document Date", "BLDAT"],
        "clearing_date": ["Clearing Date", "AUGDT"],
        "company":  ["Company Code", "BUKRS"],
        "fiscal_year": ["Fiscal Year", "GJAHR"],
        "fiscal_year_clearing": ["Fiscal Year_Clearing Document", "GJAHR_AUG"],
        "doctype":  ["Document Type", "BLART"],
        "is_exception": ["is_exception"],
        "affected_amount": ["affected_amount"],
        "status_label": ["status_label"],
        "ageing_days": ["ageing_days"],
        "ageing_days_filtered": ["ageing_days_filtered"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    paths = [
        rf"data_files/FJAC10_Exception{int(exc_id):02}.csv",
        rf"data_files/FJAC10_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None