# Customer/MasterData/CJMA18.py — Updates don't match record
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA18",

    "name": "Updates don't match record",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Updates don't match record"),

            "cards": [

                {"id": "k1", "label": "Company Code", "agg": "unique", "source": "company"},

                {"id": "k2", "label": "Customer Number", "agg": "unique", "source": "customer"},

                {"id": "k3", "label": "Tax Number", "agg": "unique", "source": "tax_number"},

                {"id": "k4", "label": "PAN", "agg": "unique", "source": "pan"},

                {"id": "k5", "label": "City", "agg": "unique", "source": "city"},

                {"id": "k6", "label": "Net Value", "agg": "sum", "source": "amount", "format": "currency"}
            ],

            "filters": [

                {"id": "f1", "label": "Net Value (INR)", "source": "amount"},

                {"id": "f2", "label": "Permanent Account Number", "source": "pan"},

                {"id": "f3", "label": "Customer Account Group", "source": "account_group"},

                {"id": "f4", "label": "Date on which the record was created", "source": "date"}
            ],

            "charts": [

                {"id": "c1", "type": "bar", "x": "company", "y": "amount", "agg": "sum", "top_n": 10, "title": get_chart_title("Company Code", "Mismatch Value")},

                {"id": "c2", "type": "doughnut", "x": "account_group", "agg": "count", "title": get_chart_title("Customer Account Group", "Impacted Cities")},

                {"id": "c3", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": get_chart_title("Created Date", "Value Discovery Trend")},

                {"id": "c4", "type": "pie", "x": "company", "y": "amount", "agg": "sum", "title": get_chart_title("Company Code", "Mismatch Distribution")},

                {"id": "c5", "type": "bar", "x": "name", "y": "amount", "agg": "sum", "top_n": 10, "title": get_chart_title("Name", "Value Discrepancy")}
            ]
        }
    ],

    "columns": {

        "company": ["Company Code"],

        "customer": ["Customer Number"],

        "tax_number": ["Tax Number 3"],

        "pan": ["Permanent Account Number"],

        "city": ["City"],

        "amount": ["Net Value (INR)"],

        "account_group": ["Customer Account Group"],

        "name": ["Name 1"],

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

    path = rf"D:\off\JKC Dashboard\output\CJMA18_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')

