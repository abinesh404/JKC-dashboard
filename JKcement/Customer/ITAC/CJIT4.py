# Customer/ITAC/CJIT4.py — Credit note > invoice value
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJIT4",

    "name": "Credit note > invoice value",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Credit note > invoice value"),

            "cards": [

                {"id": "k1", "label": "Total Value", "agg": "total_value", "source": "amount", "format": "currency"},

                {"id": "k2", "label": "Exceptions", "agg": "row_count"},

                {"id": "k3", "label": "Unique Fields", "agg": "unique", "source": "field"},

                {"id": "k4", "label": "Avg Impact", "agg": "avg", "source": "amount"},

                {"id": "k5", "label": "Max Deviation", "agg": "max", "source": "amount"},

                {"id": "k6", "label": "Total Base Records", "agg": "row_count"}
            ],

            "filters": [

                {"id": "f1", "label": "Table Name", "source": "table"},

                {"id": "f2", "label": "Field Name", "source": "field"},

                {"id": "f3", "label": "User", "source": "user"}
            ],

            "charts": [

                {"id": "c1", "type": "doughnut", "x": "table", "agg": "count", "title": get_chart_title("Split by Table")},

                {"id": "c2", "type": "bar", "x": "field", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": get_chart_title("Top Violations", "Field")},

                {"id": "c3", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": get_chart_title("Timeline Trend")},

                {"id": "c4", "type": "bar", "x": "user", "agg": "count", "top_n": 10, "title": get_chart_title("Distribution", "User")}
            ]
        }
    ],

    "columns": {

        "table": ["TableName"],

        "field": ["FieldName"],

        "user": ["User"],

        "amount": ["NewValue"],

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

    path = rf"D:\off\JKC Dashboard\output\CJIT04_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')

