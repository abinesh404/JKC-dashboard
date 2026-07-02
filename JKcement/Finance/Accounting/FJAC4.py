# Finance/Accounting/FJAC4.py — Documents Posted in Prior Reporting Period
# -------------------------------------------------------------------------

import pandas as pd
import os
import numpy as np
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC4",
    "name": "Documents Posted in Prior Reporting Period",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Code", "BUKRS"],
        "fiscal_year": ["Fiscal Year", "GJAHR"],
        "customer": ["Customer Number", "KUNNR"],
        "cust_name": ["Customer Name", "NAME1_C"],
        "vendor": ["Vendor Number", "LIFNR", "Customer Number"],
        "vend_name": ["Vendor Name", "NAME1_V", "Customer Name"],
        "date": ["Accounting Document Entry Date", "CPUDT", "Posting Date in Document"],
        "posting_date": ["Posting Date in Document", "BUDAT"],
        "entry_date": ["Accounting Document Entry Date", "CPUDT"],
        "posting_period": ["Fiscal period", "MONAT"],
        "posting_key_name": ["Posting Key Name", "PTEXT"],
        "amount": ["Amount in Local Currency", "DMBTR"],
        "is_exception": ["is_exception"],
        "status_label": ["status_label"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    paths = [
        rf"data_files/FJAC4_Exception{int(exc_id):02}.csv",
        rf"data_files/FJAC4_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None