# Customer/MasterData/CJMA17.py — No Updates in Customer Account #2
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA17",

    "name": "No Updates in Customer Account #2",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "company": ["Company Code"],

        "customer": ["Customer Number"],

        "recon": ["Reconciliation Account in General Ledger"],

        "creator": ["Name of Person who Created the Object"],

        "city": ["City"],

        "amount": ["Net Value (INR)"],

        "name": ["Name 1"],

        "tax_number": ["Tax Number"],

        "pan": ["Permanent Account Number"],

        "account_group": ["Customer Account Group"],

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
        rf"data_files/CJMA17_Exception{int(exc_id):02}.csv",
        rf"data_files/CJMA17_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None