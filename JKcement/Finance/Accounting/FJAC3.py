# Finance/Accounting/FJAC3.py — Vendor recon account not defined
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC3",
    "name": "Vendor recon account not defined",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Code", "BUKRS", "Name of Company Code or Company"],
        "vendor": ["Account Number of Vendor or Creditor", "Vendor Name", "LIFNR"],
        "recon": ["Reconciliation Account in General Ledger", "HKONT"],
        "acc_group": ["Vendor account group", "KTOKK"],
        "country": ["Country Key", "LAND1"],
        "created_by": ["Name of Person who Created the Object", "ERNAM"],
        "created_on": ["Date on which the Record Was Created", "ERDAT"],
        "del_flag": ["Deletion Flag for Master Record (Company Code Level)", "LOEVM"],
        "post_block": ["Posting block for company code", "SPERR"],
        "pay_block": ["Block Key for Payment", "SPERM"],
        "amount": ["Amount in Local Currency", "DMBTR"],
        "recon_issue": ["recon_issue"],
        "recon_status": ["recon_status"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    paths = [
        rf"data_files/FJAC3_Exception{int(exc_id):02}.csv",
        rf"data_files/FJAC3_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None