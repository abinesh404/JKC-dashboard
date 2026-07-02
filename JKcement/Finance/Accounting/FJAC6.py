# Finance/Accounting/FJAC6.py — Missing & Backdated Invoicing
# -------------------------------------------------------------------------

import pandas as pd
import os
import numpy as np
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC6",
    "name": "Missing & Backdated Invoicing",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Code", "BUKRS"],
        "fiscal_year": ["Fiscal Year", "GJAHR"],
        "billing_type": ["Billing Type", "FKART"],
        "sales_org": ["Sales Organization", "VKORG"],
        "user": ["User", "ERNAM"],
        "billing_date": ["Billing Date", "FKDAT"],
        "posting_date": ["Posting Date", "BUDAT"],
        "created_on": ["Created On (Document Date)", "ERDAT"],
        "entry_date": ["Entry Date", "CPUDT"],
        "amount": ["Net Value", "NETWR"],
        "is_missing": ["is_missing"],
        "missing_billing": ["missing_billing"],
        "missing_posting": ["missing_posting"],
        "missing_doc": ["missing_doc"],
        "is_backdated": ["is_backdated"],
        "backdate_days": ["backdate_days"],
        "missing_type": ["missing_type"],
        "completeness_status": ["completeness_status"],
        "backdated_status": ["backdated_status"],
        "missing_val": ["missing_val"],
        "backdated_val": ["backdated_val"],
        "date": ["Entry Date", "Posting Date", "Created On (Document Date)"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    paths = [
        rf"data_files/FJAC6_Exception{int(exc_id):02}.csv",
        rf"data_files/FJAC6_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None