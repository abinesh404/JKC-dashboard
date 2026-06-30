# Customer/ITAC/CJIT8.py — Price condition change before SO
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJIT8",

    "name": "Price condition change before SO",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Price condition change before SO"),

            "cards": [

                {"id": "k1", "label": "Total Value", "agg": "total_value", "source": "amount", "format": "currency"},

                {"id": "k2", "label": "Exceptions", "agg": "row_count"},

                {"id": "k3", "label": "Unique Plants", "agg": "unique", "source": "plant"},

                {"id": "k4", "label": "Avg Impact", "agg": "avg", "source": "amount"},

                {"id": "k5", "label": "Max Deviation", "agg": "max", "source": "amount"},

                {"id": "k6", "label": "Total Base Records", "agg": "row_count"}
            ],

            "filters": [

                {"id": "f1", "label": "Plant", "source": "plant"},

                {"id": "f2", "label": "Material Group", "source": "material_group"},

                {"id": "f3", "label": "Sold-to-Party", "source": "customer"}
            ],

            "charts": [

                {"id": "c1", "type": "doughnut", "x": "plant", "agg": "count", "title": get_chart_title("Split by Plant")},

                {"id": "c2", "type": "bar", "x": "material_group", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": get_chart_title("Top Material Groups", "Net Price")},

                {"id": "c3", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": get_chart_title("Timeline Trend")},

                {"id": "c4", "type": "bar", "x": "customer", "agg": "count", "top_n": 10, "title": get_chart_title("Distribution", "Sold-to-Party")}
            ]
        }
    ],

    "columns": {

        "plant": ["Plant"],

        "material_group": ["Material Group"],

        "customer": ["Sold-to-Party"],

        "amount": ["Net price"],

        "date": ["Created on"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer ITAC"
    }


def get_data(exc_id):

    path = rf"D:\off\JKC Dashboard\output\CJIT08_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')
