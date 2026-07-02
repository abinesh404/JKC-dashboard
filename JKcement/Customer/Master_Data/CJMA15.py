# Customer/MasterData/CJMA15.py — Vendor To Customer setoff
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA15",

    "name": "Vendor To Customer setoff",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "vendor": ["Vendor Number"],

        "clearing_doc": ["Clearing Document Number"],

        "company": ["Company Code"],

        "customer": ["Customer Number"],

        "customer_amount": ["Customer Amount"],

        "vendor_amount": ["Vendor Amount"],

        "vendor_name": ["Vendor Name"],

        "clearing_key": ["CLEARING_KEY"],

        "customer_name": ["Customer Name"],

        "doc_type": ["Document Type_Vendor"],

        "city": ["City"],

        "date": ["Clearing Date_Vendor"]
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
        rf"data_files/CJMA15_Exception{int(exc_id):02}.csv",
        rf"data_files/CJMA15_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None