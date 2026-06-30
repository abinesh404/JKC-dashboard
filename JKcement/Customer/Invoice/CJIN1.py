# Customer/Invoice/CJIN1.py — Invoice Series discrepancies
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------
# AXIS ACCESS:
#   Pie    -> X: Material           | Y: Sum(Quantity)
#   Bar    -> X: Customer           | Y: Sum(Invoice Amount)
#   Line   -> X: Billing Date       | Y: Count of rows
#   Donut  -> X: Company Code       | Y: Sum(Invoice Amount)
#   Column -> X: Plant              | Y: Sum(Gap)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJIN1",

    "name": "Invoice Series discrepancies",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Invoice Series discrepancies"),

            "cards": [

                {"id": "k1", "label": "Total Gap Count", "agg": "sum", "source": "gap"},

                {"id": "k2", "label": "Total Invoice Amt", "agg": "total_value", "source": "amount", "format": "currency"},

                {"id": "k3", "label": "Company Count", "agg": "unique", "source": "company"},

                {"id": "k4", "label": "Count of Customers", "agg": "unique", "source": "customer"},

                {"id": "k5", "label": "Prev Invoice Total", "agg": "total_value", "source": "prev_amount", "format": "currency"},

                {"id": "k6", "label": "Impacted Plants", "agg": "unique", "source": "plant"}
            ],

            "filters": [

                {"id": "f1", "label": "Company", "source": "company"},

                {"id": "f2", "label": "Billing Type", "source": "doctype"},

                {"id": "f3", "label": "Gap Value", "source": "gap"}
            ],

            "charts": [

                {"id": "c1", "type": "pie", "x": "material", "y": "quantity", "agg": "sum", "top_n": 5, "title": get_chart_title("Material", "Quantity", top_n=5)},

                {"id": "c2", "type": "bar", "x": "customer", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": get_chart_title("Customer", "Invoice Amount", top_n=10)},

                {"id": "c3", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": get_chart_title("Monthly Anomaly Trend")},

                {"id": "c4", "type": "doughnut", "x": "company", "y": "amount", "agg": "sum", "title": get_chart_title("Company Share", "Invoice Amount")},

                {"id": "c5", "type": "bar", "x": "plant", "y": "gap", "agg": "sum", "top_n": 10, "title": get_chart_title("Top 10 Plants", "Gap")}
            ]
        }
    ],

    "columns": {

        "company": ["Company Code"],

        "customer": ["Customer"],

        "material": ["Material"],

        "doctype": ["Billing Type"],

        "date": ["Billing Date"],

        "plant": ["Plant"],

        "gap": ["Gap"],

        "quantity": ["Quantity"],

        "amount": ["Invoice Amount"],

        "prev_amount": ["Previous_Invoice Amount"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer Invoice"
    }


def get_data(exc_id):

    path = rf"D:\off\JKC Dashboard\output\CJIN01_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')
