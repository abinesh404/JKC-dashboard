# Customer/MasterData/CJMA10.py — Duplicate Customer Masters
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA10",

    "name": "Duplicate Customer Masters",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "account_group": ["Account group"],

        "customer": ["Customer"],

        "company": ["Company Code"],

        "region": ["Region"],

        "open_balance": ["Open Balance"],

        "dup_balance": ["Net Balance for Duplicates"],

        "name": ["Name 1"],

        "duplicate_customer": ["Duplicate Customers"],

        "created_by": ["Created by"],

        "pan": ["Permanent account number"],

        "payment_terms": ["Terms of Payment"],

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
        rf"data_files/CJMA10_Exception{int(exc_id):02}.csv",
        rf"data_files/CJMA10_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None