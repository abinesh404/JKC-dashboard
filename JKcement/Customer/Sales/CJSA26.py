# Customer/Sales/CJSA26.py — Sales return quantity variance
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJSA26",

    "name": "Sales return quantity variance",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")},
        {"id": "3", "label": "Exception 03", "title": get_exception_title("Exception 03")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "company": ["Company Code"],

        "material": ["Material"],

        "plant": ["Plant"],

        "billing_doc": ["Billing Document"],

        "batch": ["Batch"],

        "net_value": ["Net Value"],

        "billing_type": ["Billing Type"],

        "combined": ["Combined String"],

        "sales_doc": ["Sales Document"],

        "shelf_life": ["Remaining Shelf Life"],

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
        rf"data_files/CJSA26_Exception{int(exc_id):02}.csv",
        rf"data_files/CJSA26_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None