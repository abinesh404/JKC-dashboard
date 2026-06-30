# Customer/MasterData/CJMA15.py — Vendor To Customer setoff
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA15",

    "name": "Vendor To Customer setoff",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Vendor To Customer setoff"),

            "cards": [

                {"id": "k1", "label": "Vendor Number", "agg": "unique", "source": "vendor"},

                {"id": "k2", "label": "Clearing Doc", "agg": "unique", "source": "clearing_doc"},

                {"id": "k3", "label": "Company Code", "agg": "unique", "source": "company"},

                {"id": "k4", "label": "Customer Number", "agg": "unique", "source": "customer"},

                {"id": "k5", "label": "Cust Amount", "agg": "sum", "source": "customer_amount", "format": "currency"},

                {"id": "k6", "label": "Vend Amount", "agg": "sum", "source": "vendor_amount", "format": "currency"}
            ],

            "filters": [

                {"id": "f1", "label": "Vendor Name", "source": "vendor_name"},

                {"id": "f2", "label": "CLEARING_KEY", "source": "clearing_key"},

                {"id": "f3", "label": "Customer Name", "source": "customer_name"},

                {"id": "f4", "label": "City", "source": "city"}
            ],

            "charts": [

                {"id": "c1", "type": "bar", "x": "customer_name", "agg": "count", "top_n": 10, "title": get_chart_title("Customer Name", "Clearing Docs")},

                {"id": "c2", "type": "doughnut", "x": "doc_type", "agg": "count", "title": get_chart_title("Document Type", "Docs Count")},

                {"id": "c3", "type": "line", "x": "date", "y": "vendor_amount", "agg": "sum", "time_group": "month", "title": get_chart_title("Clearing Date", "Vendor Amount Trend")},

                {"id": "c4", "type": "pie", "x": "city", "agg": "count", "title": get_chart_title("City", "Vendor Volume")},

                {"id": "c5", "type": "bar", "x": "vendor_name", "agg": "count", "top_n": 10, "title": get_chart_title("Vendor Name", "Clearing Docs")}
            ]
        }
    ],

    "columns": {

        "vendor": ["Vendor Number"],

        "clearing_doc": ["Clearing Document Number"],

        "company": ["Company Code"],

        "customer": ["Customer Number"],

        "customer_amount": ["Customer Amount"],

        "vendor_amount": ["Vendor Amount"],

        "vendor_name": ["Vendor Name"],

        "clearing_key": ["CLEARING_KEY"],

        "customer_name": ["Customer Name"],

        "doc_type": ["Document Type_Vendor"],

        "city": ["City"],

        "date": ["Clearing Date_Vendor"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer Master Data"
    }


def get_data(exc_id):

    path = rf"D:\off\JKC Dashboard\output\CJMA15_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')

