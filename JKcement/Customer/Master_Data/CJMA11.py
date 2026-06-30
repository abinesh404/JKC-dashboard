# Customer/MasterData/CJMA11.py — Payment term issues
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA11",

    "name": "Payment term issues",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Payment term issues"),

            "cards": [

                {"id": "k1", "label": "Customer Number", "agg": "unique", "source": "customer"},

                {"id": "k2", "label": "Billing Document", "agg": "unique", "source": "billing_doc"},

                {"id": "k3", "label": "Plant", "agg": "unique", "source": "plant"},

                {"id": "k4", "label": "Payment Terms", "agg": "unique", "source": "payment_terms"},

                {"id": "k5", "label": "Total Amount", "agg": "sum", "source": "amount", "format": "currency"},

                {"id": "k6", "label": "Record Count", "agg": "row_count"}
            ],

            "filters": [

                {"id": "f1", "label": "Payment Terms", "source": "payment_terms"},

                {"id": "f2", "label": "Billing Type", "source": "billing_type"},

                {"id": "f3", "label": "Company Code", "source": "company"},

                {"id": "f4", "label": "Sales Order Number", "source": "sales_order"}
            ],

            "charts": [

                {"id": "c1", "type": "bar", "x": "billing_doc", "y": "amount", "agg": "sum", "top_n": 10, "title": get_chart_title("Billing Document", "Amount")},

                {"id": "c2", "type": "doughnut", "x": "billing_type", "y": "amount", "agg": "sum", "title": get_chart_title("Billing Type", "Amount")},

                {"id": "c3", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": get_chart_title("Billing Date", "Billing Amount Trend")},

                {"id": "c4", "type": "pie", "x": "payment_terms", "y": "amount", "agg": "sum", "title": get_chart_title("Payment Terms", "Amount Distribution")},

                {"id": "c5", "type": "bar", "x": "payment_terms", "y": "amount", "agg": "sum", "top_n": 10, "title": get_chart_title("Payment Terms", "Amount")}
            ]
        }
    ],

    "columns": {

        "customer": ["Customer Number"],

        "billing_doc": ["Billing Document Number"],

        "plant": ["Plant"],

        "payment_terms": ["Payment Terms"],

        "billing_type": ["Billing Type"],

        "company": ["Company Code"],

        "sales_order": ["Sales Order Number"],

        "amount": ["Amount in Local Currency"],

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

    path = rf"D:\off\JKC Dashboard\output\CJMA11_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')

