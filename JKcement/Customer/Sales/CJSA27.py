# Customer/Sales/CJSA27.py — Sales return quantity variance for sold to party
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJSA27",

    "name": "Sales return quantity variance for sold to party",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "company": ["Company Code"],

        "material": ["Material Number"],

        "batch": ["Batch No"],

        "plant": ["Plant Code"],

        "sales_qty": ["Total Sales Quantity"],

        "return_qty": ["Total Sales Return Quantity"],

        "company_name": ["Company Name"],

        "qty_diff": ["Qty Difference"],

        "material_desc": ["Material Description"],

        "plant_name": ["Plant Name"],

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
        rf"data_files/CJSA27_Exception{int(exc_id):02}.csv",
        rf"data_files/CJSA27_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None