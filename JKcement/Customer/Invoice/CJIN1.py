# Customer/Invoice/CJIN1.py — Invoice Series discrepancies
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------
# AXIS ACCESS:
#   Pie    -> X: Material           | Y: Sum(Quantity)
#   Bar    -> X: Customer           | Y: Sum(Invoice Amount)
#   Line   -> X: Billing Date       | Y: Count of rows
#   Donut  -> X: Company Code       | Y: Sum(Invoice Amount)
#   Column -> X: Plant              | Y: Sum(Gap)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJIN1",

    "name": "Invoice Series discrepancies",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "company": ["Company Code"],

        "customer": ["Customer"],

        "material": ["Material"],

        "doctype": ["Billing Type"],

        "date": ["Billing Date"],

        "plant": ["Plant"],

        "gap": ["Gap"],

        "quantity": ["Quantity"],

        "amount": ["Invoice Amount"],

        "prev_amount": ["Previous_Invoice Amount"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer Invoice"
    }


def get_data(exc_id):
    paths = [
        rf"data_files/CJIN1_Exception{int(exc_id):02}.csv",
        rf"data_files/CJIN1_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None