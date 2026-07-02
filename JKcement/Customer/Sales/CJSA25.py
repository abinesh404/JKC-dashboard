# Customer/Sales/CJSA25.py — Delivery in excess to the tolerance defined for sales order. (Qty and Transactional)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJSA25",

    "name": "Delivery in excess to the tolerance defined for sales order. (Qty and Transactional)",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "company": ["Company Code"],

        "pricing": ["Pricing Procedures"],

        "docs": ["Docs"],

        "condition": ["Condition Types"],

        "sales_org": ["Sales Organisation"],

        "diff": ["%Diff"],

        "billing_type": ["Billing Type"],

        "division": ["Division"],

        "billing_doc": ["Billing Document"],

        "gross_weight": ["Gross weight"],

        "material": ["Material Number"],

        "net_price": ["NetPrice"],

        "date": ["Date for pricing and exchange rate"]
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
        rf"data_files/CJSA25_Exception{int(exc_id):02}.csv",
        rf"data_files/CJSA25_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None