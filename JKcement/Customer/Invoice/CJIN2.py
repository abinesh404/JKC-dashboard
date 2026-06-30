# Customer/Invoice/CJIN2.py — Anomalies to CR Note
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------
# AXIS ACCESS:
#   Pie    -> X: Mat. Type          | Y: Count of rows
#   Bar    -> X: Material           | Y: Sum(Net Value)
#   Line   -> X: Billing Doc.       | Y: Count of rows
#   Donut  -> X: Doc type           | Y: Sum(Net Value)
#   Column -> X: Test Case          | Y: Count of rows
# -----------------------------------------------------


import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJIN2",

    "name": "Anomalies to CR Note",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Anomalies to CR Note"),

            "cards": [

                {"id": "k1", "label": "Total Anomalies", "agg": "row_count"},

                {"id": "k2", "label": "Total Net Value", "agg": "total_value", "source": "net_value", "format": "currency"},

                {"id": "k3", "label": "Company Count", "agg": "unique", "source": "doctype"},

                {"id": "k4", "label": "Unique Mat Types", "agg": "unique", "source": "mattype"},

                {"id": "k5", "label": "Target Qty Total", "agg": "sum", "source": "targetqty"},

                {"id": "k6", "label": "Test Case Count", "agg": "unique", "source": "testcase"}
            ],

            "filters": [

                {"id": "f1", "label": "Doc Type", "source": "doctype"},

                {"id": "f2", "label": "Description", "source": "desc"},

                {"id": "f3", "label": "Test Case", "source": "testcase"}
            ],

            "charts": [

                {"id": "c1", "type": "pie", "x": "mattype", "agg": "count", "top_n": 5, "title": get_chart_title("Mat Type Share")},

                {"id": "c2", "type": "bar", "x": "material", "y": "net_value", "agg": "sum", "top_n": 10, "horizontal": True, "title": get_chart_title("Top 10 Materials", "Net Value")},

                {"id": "c3", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": get_chart_title("Monthly Anomaly Trend")},

                {"id": "c4", "type": "doughnut", "x": "doctype", "y": "net_value", "agg": "sum", "title": get_chart_title("Doc Type Share", "Net Value")},

                {"id": "c5", "type": "bar", "x": "testcase", "agg": "count", "top_n": 10, "title": get_chart_title("Top Test Cases")}
            ]
        }
    ],

    "columns": {

        "material": ["Material"],

        "mattype": ["Mat. Type"],

        "doctype": ["Doc type"],

        "desc": ["Doc. Type Desc"],

        "date": ["Billing Date"],

        "net_value": ["Net Value"],

        "targetqty": ["Target Qty"],

        "testcase": ["Test Case"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer Invoice"
    }


def get_data(exc_id):

    path = rf"D:\off\JKC Dashboard\output\CJIN02_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')

