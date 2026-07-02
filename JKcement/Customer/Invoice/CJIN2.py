# Customer/Invoice/CJIN2.py — Anomalies to CR Note
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------
# AXIS ACCESS:
#   Pie    -> X: Mat. Type          | Y: Count of rows
#   Bar    -> X: Material           | Y: Sum(Net Value)
#   Line   -> X: Billing Doc.       | Y: Count of rows
#   Donut  -> X: Doc type           | Y: Sum(Net Value)
#   Column -> X: Test Case          | Y: Count of rows
# -----------------------------------------------------


import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJIN2",

    "name": "Anomalies to CR Note",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "material": ["Material"],

        "mattype": ["Mat. Type"],

        "doctype": ["Doc type"],

        "desc": ["Doc. Type Desc"],

        "date": ["Billing Date"],

        "net_value": ["Net Value"],

        "targetqty": ["Target Qty"],

        "testcase": ["Test Case"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer Invoice"
    }


def get_data(exc_id):
    paths = [
        rf"data_files/CJIN2_Exception{int(exc_id):02}.csv",
        rf"data_files/CJIN2_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None