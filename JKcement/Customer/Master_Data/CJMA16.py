# Customer/MasterData/CJMA16.py — No Updates in Customer Account #1
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA16",

    "name": "No Updates in Customer Account #1",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "company": ["Company Code"],

        "recon": ["Reconciliation Account in General Ledger"],

        "city": ["City"],

        "customer": ["Customer Number"],

        "currency": ["Currency Key"],

        "amount": ["Net Value (INR)"],

        "name": ["Name 1"],

        "account_group": ["Customer Account Group"],

        "pan": ["Permanent Account Number"],

        "prediction": ["prediction"],

        "date": ["Date on which the record was created"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer Master Data"
    }


def get_data(exc_id):
    paths = [
        rf"data_files/CJMA16_Exception{int(exc_id):02}.csv",
        rf"data_files/CJMA16_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None