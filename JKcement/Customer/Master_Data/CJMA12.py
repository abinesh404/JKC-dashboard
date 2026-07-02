# Customer/MasterData/CJMA12.py — Adverse payment terms in invoice
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA12",

    "name": "Adverse payment terms in invoice",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "company": ["Company Code"],

        "user": ["User Name"],

        "clearing_doc": ["Clearing Document"],

        "line_item": ["Line Item"],

        "gl_account": ["GL Account"],

        "company_name": ["Company Name"],

        "payer": ["Payer Code"],

        "city": ["City"],

        "ageing": ["Ageing_Bucket"],

        "invoice_terms": ["Payment Terms (Invoice)"],

        "days_invoice": ["Days_Invoice"],

        "sold_to": ["Sold-To Party Code"],

        "amount": ["Amount in Doc Currency"],

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
        rf"data_files/CJMA12_Exception{int(exc_id):02}.csv",
        rf"data_files/CJMA12_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None