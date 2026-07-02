# Customer/MasterData/CJMA14.py — Customer To vendor setoff
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA14",

    "name": "Customer To vendor setoff",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "customer": ["Customer Number"],

        "company": ["Company Code"],

        "clearing_match": ["CLEARING_DATE_MATCH"],

        "vendor": ["Vendor Number"],

        "customer_amount": ["Customer Amount"],

        "vendor_amount": ["Vendor Amount"],

        "customer_name": ["Customer Name"],

        "clearing_key": ["CLEARING_KEY"],

        "vendor_name": ["Vendor Name"],

        "doc_type": ["Document Type_Customer"],

        "city": ["City"],

        "date": ["Clearing Date_Customer"]
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
        rf"data_files/CJMA14_Exception{int(exc_id):02}.csv",
        rf"data_files/CJMA14_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None