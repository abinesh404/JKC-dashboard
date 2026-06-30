# Customer/MasterData/CJMA12.py — Adverse payment terms in invoice
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA12",

    "name": "Adverse payment terms in invoice",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Adverse payment terms in invoice"),

            "cards": [

                {"id": "k1", "label": "Company Code", "agg": "unique", "source": "company"},

                {"id": "k2", "label": "User Name", "agg": "unique", "source": "user"},

                {"id": "k3", "label": "Clearing Document", "agg": "unique", "source": "clearing_doc"},

                {"id": "k4", "label": "Line Item", "agg": "unique", "source": "line_item"},

                {"id": "k5", "label": "GL Account", "agg": "unique", "source": "gl_account"},

                {"id": "k6", "label": "Total Amount", "agg": "sum", "source": "amount", "format": "currency"}
            ],

            "filters": [

                {"id": "f1", "label": "Company Name", "source": "company_name"},

                {"id": "f2", "label": "Payer Code", "source": "payer"},

                {"id": "f3", "label": "City", "source": "city"},

                {"id": "f4", "label": "Ageing Bucket", "source": "ageing"}
            ],

            "charts": [

                {"id": "c1", "type": "bar", "x": "ageing", "agg": "count", "top_n": 10, "title": get_chart_title("Ageing Bucket", "Amount Count")},

                {"id": "c2", "type": "doughnut", "x": "invoice_terms", "agg": "count", "title": get_chart_title("Payment Terms", "Usage Frequency")},

                {"id": "c3", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": get_chart_title("Billing Date", "Amount Trend")},

                {"id": "c4", "type": "pie", "x": "days_invoice", "y": "amount", "agg": "sum", "title": get_chart_title("Days Invoice", "Amount")},

                {"id": "c5", "type": "bar", "x": "sold_to", "agg": "count", "top_n": 10, "title": get_chart_title("Sold-To Party", "User Count")}
            ]
        }
    ],

    "columns": {

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

    path = rf"D:\off\JKC Dashboard\output\CJMA12_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')

