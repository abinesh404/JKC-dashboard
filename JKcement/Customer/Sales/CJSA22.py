# Customer/Sales/CJSA22.py — Sale of goods at free of cost
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJSA22",

    "name": "Sale of goods at free of cost",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "company": ["Company Name"],

        "material": ["Material Number"],

        "plant": ["Plant"],

        "billing_doc": ["Billing Document"],

        "customer": ["Sold to Party"],

        "net_value": ["Net Valuet"],

        "material_desc": ["Material Description"],

        "sales_doc": ["Sales Document"],

        "impact": ["Impact"],

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
        rf"data_files/CJSA22_Exception{int(exc_id):02}.csv",
        rf"data_files/CJSA22_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None