# Customer/MasterData/CJMA10.py — Duplicate Customer Masters
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA10",

    "name": "Duplicate Customer Masters",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Duplicate Customer Masters"),

            "cards": [

                {"id": "k1", "label": "Account Group", "agg": "unique", "source": "account_group"},

                {"id": "k2", "label": "Customer", "agg": "unique", "source": "customer"},

                {"id": "k3", "label": "Company Code", "agg": "unique", "source": "company"},

                {"id": "k4", "label": "Region", "agg": "unique", "source": "region"},

                {"id": "k5", "label": "Open Balance", "agg": "sum", "source": "open_balance", "format": "currency"},

                {"id": "k6", "label": "Net Dup Balance", "agg": "sum", "source": "dup_balance", "format": "currency"}
            ],

            "filters": [

                {"id": "f1", "label": "Name", "source": "name"},

                {"id": "f2", "label": "Duplicate Customers", "source": "duplicate_customer"},

                {"id": "f3", "label": "Created by", "source": "created_by"},

                {"id": "f4", "label": "Permanent account number", "source": "pan"}
            ],

            "charts": [

                {"id": "c1", "type": "bar", "x": "created_by", "agg": "count", "top_n": 10, "title": get_chart_title("Created by", "Customer Count")},

                {"id": "c2", "type": "doughnut", "x": "name", "y": "open_balance", "agg": "sum", "title": get_chart_title("Name", "Open Balance")},

                {"id": "c3", "type": "line", "x": "date", "y": "open_balance", "agg": "sum", "time_group": "month", "title": get_chart_title("Created On", "Open Balance Trend")},

                {"id": "c4", "type": "pie", "x": "payment_terms", "agg": "count", "title": get_chart_title("Terms of Payment", "Customer Count")},

                {"id": "c5", "type": "bar", "x": "name", "y": "open_balance", "agg": "sum", "top_n": 10, "title": get_chart_title("Name", "Open Balance")}
            ]
        }
    ],

    "columns": {

        "account_group": ["Account group"],

        "customer": ["Customer"],

        "company": ["Company Code"],

        "region": ["Region"],

        "open_balance": ["Open Balance"],

        "dup_balance": ["Net Balance for Duplicates"],

        "name": ["Name 1"],

        "duplicate_customer": ["Duplicate Customers"],

        "created_by": ["Created by"],

        "pan": ["Permanent account number"],

        "payment_terms": ["Terms of Payment"],

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

    path = rf"D:\off\JKC Dashboard\output\CJMA10_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')
