# Customer/MasterData/CJMA19.py — Unblocked duplicate customers
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA19",

    "name": "Unblocked duplicate customers",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Unblocked duplicate customers"),

            "cards": [

                {"id": "k1", "label": "Company Code", "agg": "unique", "source": "company"},

                {"id": "k2", "label": "Customer Code", "agg": "unique", "source": "customer"},

                {"id": "k3", "label": "PAN", "agg": "unique", "source": "pan"},

                {"id": "k4", "label": "Region", "agg": "unique", "source": "region"},

                {"id": "k5", "label": "Country", "agg": "unique", "source": "country"},

                {"id": "k6", "label": "Balance", "agg": "sum", "source": "amount", "format": "currency"}
            ],

            "filters": [

                {"id": "f1", "label": "Name", "source": "name"},

                {"id": "f2", "label": "Postal Code", "source": "postal_code"},

                {"id": "f3", "label": "Duplicate Details", "source": "duplicate_details"}
            ],

            "charts": [

                {"id": "c1", "type": "bar", "x": "name", "y": "duplicate_count", "agg": "sum", "top_n": 10, "title": get_chart_title("Name", "Duplicate Count")},

                {"id": "c2", "type": "doughnut", "x": "company", "y": "amount", "agg": "sum", "title": get_chart_title("Company Code", "Balance")},

                {"id": "c3", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": get_chart_title("Balance Date", "Balance Trend")},

                {"id": "c4", "type": "pie", "x": "customer", "agg": "count", "title": get_chart_title("Customer Code", "Region Distribution")},

                {"id": "c5", "type": "bar", "x": "name", "y": "amount", "agg": "sum", "top_n": 10, "title": get_chart_title("Name", "Balance")}
            ]
        }
    ],

    "columns": {

        "company": ["Company Code"],

        "customer": ["Customer Code"],

        "pan": ["PAN"],

        "region": ["Region"],

        "country": ["Country"],

        "amount": ["Balance as on Date"],

        "name": ["Name"],

        "postal_code": ["Postal Code"],

        "duplicate_details": ["Duplicate Details"],

        "duplicate_count": ["Count of Duplicate"],

        "date": ["Balance as on Date"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer Master Data"
    }


def get_data(exc_id):

    path = rf"D:\off\JKC Dashboard\output\CJMA19_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')

