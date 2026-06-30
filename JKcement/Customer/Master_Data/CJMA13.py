# Customer/MasterData/CJMA13.py — Key fields missing in master
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA13",

    "name": "Key fields missing in master",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Key fields missing in master"),

            "cards": [

                {"id": "k1", "label": "Customer", "agg": "unique", "source": "customer"},

                {"id": "k2", "label": "City", "agg": "unique", "source": "city"},

                {"id": "k3", "label": "PAN", "agg": "unique", "source": "pan"},

                {"id": "k4", "label": "Region", "agg": "unique", "source": "region"},

                {"id": "k5", "label": "Country", "agg": "unique", "source": "country"},

                {"id": "k6", "label": "Open Balance", "agg": "sum", "source": "amount", "format": "currency"}
            ],

            "filters": [

                {"id": "f1", "label": "Name", "source": "name"},

                {"id": "f2", "label": "Street", "source": "street"},

                {"id": "f3", "label": "Account Group", "source": "account_group"},

                {"id": "f4", "label": "Created On", "source": "date"}
            ],

            "charts": [

                {"id": "c1", "type": "bar", "x": "customer", "y": "amount", "agg": "sum", "top_n": 10, "title": get_chart_title("Customer", "Open Balance")},

                {"id": "c2", "type": "doughnut", "x": "account_group", "agg": "count", "title": get_chart_title("Account Group", "Region Count")},

                {"id": "c3", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": get_chart_title("Created On", "Creation Balance Trend")},

                {"id": "c4", "type": "pie", "x": "account_group", "agg": "count", "title": get_chart_title("Account Group", "Distribution")},

                {"id": "c5", "type": "bar", "x": "name", "y": "amount", "agg": "sum", "top_n": 10, "title": get_chart_title("Name", "Open Balance")}
            ]
        }
    ],

    "columns": {

        "customer": ["Customer"],

        "city": ["City"],

        "pan": ["PAN"],

        "region": ["Region"],

        "country": ["Country"],

        "name": ["Name"],

        "street": ["Street"],

        "account_group": ["Account Group"],

        "amount": ["Open Balance"],

        "date": ["Created On"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer Master Data"
    }


def get_data(exc_id):

    path = rf"D:\off\JKC Dashboard\output\CJMA13_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')

