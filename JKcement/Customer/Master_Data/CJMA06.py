# Customer/MasterData/CJMA06.py — Updates in Recon Account pending
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA06",

    "name": "Updates in Recon Account pending",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Updates in Recon Account pending"),

            "cards": [

                {"id": "k1", "label": "Company Code", "agg": "unique", "source": "company"},

                {"id": "k2", "label": "Customer", "agg": "unique", "source": "customer"},

                {"id": "k3", "label": "Recon Account", "agg": "unique", "source": "recon"},

                {"id": "k4", "label": "City", "agg": "unique", "source": "city"},

                {"id": "k5", "label": "Total Open Balance", "agg": "sum", "source": "amount", "format": "currency"},

                {"id": "k6", "label": "Record Count", "agg": "row_count"}
            ],

            "filters": [

                {"id": "f1", "label": "Company Code", "source": "company"},

                {"id": "f2", "label": "City", "source": "city"},

                {"id": "f3", "label": "Recon Account", "source": "recon"},

                {"id": "f4", "label": "Customer", "source": "customer"}
            ],

            "charts": [

                {"id": "c1", "type": "bar", "x": "company", "y": "amount", "agg": "sum", "top_n": 10, "title": get_chart_title("Company Code", "Open Balance")},

                {"id": "c2", "type": "doughnut", "x": "city", "agg": "count", "title": get_chart_title("City", "Customer Count")},

                {"id": "c3", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": get_chart_title("Created On", "Open Balance Trend")},

                {"id": "c4", "type": "pie", "x": "recon", "y": "amount", "agg": "sum", "title": get_chart_title("Recon Account", "Open Balance")},

                {"id": "c5", "type": "bar", "x": "customer", "y": "amount", "agg": "sum", "top_n": 10, "title": get_chart_title("Customer", "Open Balance")}
            ]
        }
    ],

    "columns": {

        "company": ["Company Code"],

        "customer": ["Customer"],

        "recon": ["Recon Account"],

        "city": ["City"],

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

    path = rf"D:\off\JKC Dashboard\output\CJMA06_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')
