# Finance/Accounting/FJAC11.py — Cost Center not belonging to WBS structure
# -------------------------------------------------------------------------

import pandas as pd
import os
import numpy as np
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC11",
    "name": "Cost Center not belonging to WBS structure",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "amount":       ["Amount", "DMBTR"],
        "cost_center":  ["Cost Center", "KOSTL"],
        "wbs":          ["WBS Element", "PS_PSP_PNR"],
        "ctrl_area":    ["Controlling Area", "KOKRS"],
        "company":      ["Company Code", "BUKRS"],
        "period":       ["Period", "MONAT"],
        "year":         ["Fiscal Year", "Fisacl Year", "GJAHR"],
        "exception":    ["Exception"],
        "is_exception": ["is_exception"],
        "affected_amount": ["affected_amount"],
        "status_label": ["status_label"],
        "mismatch_cc":  ["mismatch_cc"],
        "mismatch_wbs": ["mismatch_wbs"],
        "period_year":  ["period_year"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    paths = [
        rf"data_files/FJAC11_Exception{int(exc_id):02}.csv",
        rf"data_files/FJAC11_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None