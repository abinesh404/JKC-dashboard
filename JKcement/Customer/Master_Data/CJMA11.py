# Customer/MasterData/CJMA11.py — Payment term issues
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA11",

    "name": "Payment term issues",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "customer": ["Customer Number"],

        "billing_doc": ["Billing Document Number"],

        "plant": ["Plant"],

        "payment_terms": ["Payment Terms"],

        "billing_type": ["Billing Type"],

        "company": ["Company Code"],

        "sales_order": ["Sales Order Number"],

        "amount": ["Amount in Local Currency"],

        "date": ["Billing Date"]
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
        rf"data_files/CJMA11_Exception{int(exc_id):02}.csv",
        rf"data_files/CJMA11_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None