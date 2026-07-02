# Customer/MasterData/CJMA19.py — Unblocked duplicate customers
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA19",

    "name": "Unblocked duplicate customers",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "company": ["Company Code"],

        "customer": ["Customer Code"],

        "pan": ["PAN"],

        "region": ["Region"],

        "country": ["Country"],

        "amount": ["Balance as on Date"],

        "name": ["Name"],

        "postal_code": ["Postal Code"],

        "duplicate_details": ["Duplicate Details"],

        "duplicate_count": ["Count of Duplicate"],

        "date": ["Balance as on Date"]
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
        rf"data_files/CJMA19_Exception{int(exc_id):02}.csv",
        rf"data_files/CJMA19_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None