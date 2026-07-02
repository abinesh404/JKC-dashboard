# Customer/MasterData/CJMA13.py — Key fields missing in master
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA13",

    "name": "Key fields missing in master",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "customer": ["Customer"],

        "city": ["City"],

        "pan": ["PAN"],

        "region": ["Region"],

        "country": ["Country"],

        "name": ["Name"],

        "street": ["Street"],

        "account_group": ["Account Group"],

        "amount": ["Open Balance"],

        "date": ["Created On"]
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
        rf"data_files/CJMA13_Exception{int(exc_id):02}.csv",
        rf"data_files/CJMA13_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None