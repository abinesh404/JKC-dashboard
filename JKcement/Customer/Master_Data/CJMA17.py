# Customer/MasterData/CJMA17.py — No Updates in Customer Account #2
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA17",

    "name": "No Updates in Customer Account #2",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("No Updates in Customer Account #2"),

            "cards": [

                {"id": "k1", "label": "Company Code", "agg": "unique", "source": "company"},

                {"id": "k2", "label": "Customer Number", "agg": "unique", "source": "customer"},

                {"id": "k3", "label": "Recon Account", "agg": "unique", "source": "recon"},

                {"id": "k4", "label": "Creator", "agg": "unique", "source": "creator"},

                {"id": "k5", "label": "City", "agg": "unique", "source": "city"},

                {"id": "k6", "label": "Net Value", "agg": "sum", "source": "amount", "format": "currency"}
            ],

            "filters": [

                {"id": "f1", "label": "Name 1", "source": "name"},

                {"id": "f2", "label": "Tax Number", "source": "tax_number"},

                {"id": "f3", "label": "Permanent Account Number", "source": "pan"},

                {"id": "f4", "label": "Customer Account Group", "source": "account_group"}
            ],

            "charts": [

                {"id": "c1", "type": "bar", "x": "company", "y": "amount", "agg": "sum", "top_n": 10, "title": get_chart_title("Company Code", "Net Value")},

                {"id": "c2", "type": "doughnut", "x": "prediction", "agg": "count", "title": get_chart_title("Prediction", "Distinct Cities")},

                {"id": "c3", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": get_chart_title("Created Date", "Creation Value Trend")},

                {"id": "c4", "type": "pie", "x": "company", "y": "amount", "agg": "sum", "title": get_chart_title("Company Code", "Share")},

                {"id": "c5", "type": "bar", "x": "name", "y": "amount", "agg": "sum", "top_n": 10, "title": get_chart_title("Name", "Net Value")}
            ]
        }
    ],

    "columns": {

        "company": ["Company Code"],

        "customer": ["Customer Number"],

        "recon": ["Reconciliation Account in General Ledger"],

        "creator": ["Name of Person who Created the Object"],

        "city": ["City"],

        "amount": ["Net Value (INR)"],

        "name": ["Name 1"],

        "tax_number": ["Tax Number"],

        "pan": ["Permanent Account Number"],

        "account_group": ["Customer Account Group"],

        "prediction": ["prediction"],

        "date": ["Date on which the record was created"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer Master Data"
    }


def get_data(exc_id):

    path = rf"D:\off\JKC Dashboard\output\CJMA17_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')
