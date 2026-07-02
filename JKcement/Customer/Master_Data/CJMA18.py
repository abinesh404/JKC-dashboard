# Customer/MasterData/CJMA18.py — Updates don't match record
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA18",

    "name": "Updates don't match record",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "company": ["Company Code"],

        "customer": ["Customer Number"],

        "tax_number": ["Tax Number 3"],

        "pan": ["Permanent Account Number"],

        "city": ["City"],

        "amount": ["Net Value (INR)"],

        "account_group": ["Customer Account Group"],

        "name": ["Name 1"],

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
        rf"data_files/CJMA18_Exception{int(exc_id):02}.csv",
        rf"data_files/CJMA18_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None