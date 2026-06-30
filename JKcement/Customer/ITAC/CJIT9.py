# Customer/ITAC/CJIT9.py — Price change after Sales orders
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJIT9",

    "name": "Price change after Sales orders",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Price change after Sales orders"),

            "cards": [

                {"id": "k1", "label": "Total Value", "agg": "total_value", "source": "amount", "format": "currency"},

                {"id": "k2", "label": "Exceptions", "agg": "row_count"},

                {"id": "k3", "label": "Unique Materials", "agg": "unique", "source": "material"},

                {"id": "k4", "label": "Avg Impact", "agg": "avg", "source": "amount"},

                {"id": "k5", "label": "Max Deviation", "agg": "max", "source": "amount"},

                {"id": "k6", "label": "Total Base Records", "agg": "row_count"}
            ],

            "filters": [

                {"id": "f1", "label": "Order Type", "source": "order_type"},

                {"id": "f2", "label": "Material", "source": "material"},

                {"id": "f3", "label": "Remarks", "source": "remarks"}
            ],

            "charts": [

                {"id": "c1", "type": "doughnut", "x": "order_type", "agg": "count", "title": get_chart_title("Split by Order Type")},

                {"id": "c2", "type": "bar", "x": "material", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": get_chart_title("Top Materials", "Price Difference")},

                {"id": "c3", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": get_chart_title("Timeline Trend")},

                {"id": "c4", "type": "bar", "x": "remarks", "agg": "count", "top_n": 10, "title": get_chart_title("Distribution", "Remarks")}
            ]
        }
    ],

    "columns": {

        "order_type": ["Order Type"],

        "material": ["Material"],

        "remarks": ["REMARKS"],

        "amount": ["Difference in Price Change"],

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

    path = rf"D:\off\JKC Dashboard\output\CJIT09_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')
