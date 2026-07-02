
# Customer/Sales/CJSA21.py — Sale price
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJSA21",

    "name": "Sale price",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "company": ["Company Name"],

        "plant": ["Plant"],

        "material": ["Material Number"],

        "customer": ["Sold to Party"],

        "billing_doc": ["Billing Document"],

        "impact": ["Impact"],

        "material_desc": ["Material Description"],

        "customer_name": ["Sold to Party Name"],

        "sd_type": ["SD Type Description"],

        "billing_type": ["Billing Type Description"],

        "date": ["Created On"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer Sales"
    }


def get_data(exc_id):
    paths = [
        rf"data_files/CJSA21_Exception{int(exc_id):02}.csv",
        rf"data_files/CJSA21_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None