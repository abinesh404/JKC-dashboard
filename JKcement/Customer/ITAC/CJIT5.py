# Customer/ITAC/CJIT5.py — Delivery excess to SO tolerance
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJIT5",

    "name": "Delivery excess to SO tolerance",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Delivery excess to SO tolerance"),

            "cards": [

                {"id": "k1", "label": "Total Value", "agg": "total_value", "source": "amount", "format": "currency"},

                {"id": "k2", "label": "Exceptions", "agg": "row_count"},

                {"id": "k3", "label": "Unique Pricing Procedures", "agg": "unique", "source": "pricing"},

                {"id": "k4", "label": "Avg Impact", "agg": "avg", "source": "amount"},

                {"id": "k5", "label": "Max Deviation", "agg": "max", "source": "amount"},

                {"id": "k6", "label": "Total Base Records", "agg": "row_count"}
            ],

            "filters": [

                {"id": "f1", "label": "Sales Organisation", "source": "sales_org"},

                {"id": "f2", "label": "Division", "source": "division"},

                {"id": "f3", "label": "Condition Type", "source": "condition"}
            ],

            "charts": [

                {"id": "c1", "type": "doughnut", "x": "sales_org", "agg": "count", "title": get_chart_title("Split by Sales Organisation")},

                {"id": "c2", "type": "bar", "x": "pricing", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": get_chart_title("Top Pricing Procedures", "Amount")},

                {"id": "c3", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": get_chart_title("Timeline Trend")},

                {"id": "c4", "type": "bar", "x": "condition", "agg": "count", "top_n": 10, "title": get_chart_title("Distribution", "Condition Type")}
            ]
        }
    ],

    "columns": {

        "sales_org": ["Sales Organisation"],

        "division": ["Division"],

        "condition": ["Condition Type"],

        "pricing": ["Pricing Procedure"],

        "amount": ["Step Number"],

        "date": ["Date"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer ITAC"
    }


def get_data(exc_id):

    path = rf"D:\off\JKC Dashboard\output\CJIT05_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')

