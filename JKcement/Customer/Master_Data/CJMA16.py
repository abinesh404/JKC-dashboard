# Customer/MasterData/CJMA16.py — No Updates in Customer Account #1
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA16",

    "name": "No Updates in Customer Account #1",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("No Updates in Customer Account #1"),

            "cards": [

                {"id": "k1", "label": "Company Code", "agg": "unique", "source": "company"},

                {"id": "k2", "label": "Recon Account", "agg": "unique", "source": "recon"},

                {"id": "k3", "label": "City", "agg": "unique", "source": "city"},

                {"id": "k4", "label": "Customer Number", "agg": "unique", "source": "customer"},

                {"id": "k5", "label": "Currency Key", "agg": "unique", "source": "currency"},

                {"id": "k6", "label": "Net Value", "agg": "sum", "source": "amount", "format": "currency"}
            ],

            "filters": [

                {"id": "f1", "label": "Name 1", "source": "name"},

                {"id": "f2", "label": "Customer Account Group", "source": "account_group"},

                {"id": "f3", "label": "Permanent Account Number", "source": "pan"},

                {"id": "f4", "label": "Date on which the record was created", "source": "date"}
            ],

            "charts": [

                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "top_n": 10, "title": get_chart_title("Company Code", "Cities per Company")},

                {"id": "c2", "type": "doughnut", "x": "prediction", "y": "amount", "agg": "sum", "title": get_chart_title("Prediction", "Net Value")},

                {"id": "c3", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": get_chart_title("Created Date", "Net Value Trend")},

                {"id": "c4", "type": "pie", "x": "prediction", "y": "amount", "agg": "sum", "title": get_chart_title("Prediction", "Mix")},

                {"id": "c5", "type": "bar", "x": "name", "y": "amount", "agg": "sum", "top_n": 10, "title": get_chart_title("Name", "Net Value")}
            ]
        }
    ],

    "columns": {

        "company": ["Company Code"],

        "recon": ["Reconciliation Account in General Ledger"],

        "city": ["City"],

        "customer": ["Customer Number"],

        "currency": ["Currency Key"],

        "amount": ["Net Value (INR)"],

        "name": ["Name 1"],

        "account_group": ["Customer Account Group"],

        "pan": ["Permanent Account Number"],

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

    path = rf"D:\off\JKC Dashboard\output\CJMA16_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')

