# Customer/ITAC/CJIT3.py — Credit sales exceeding limit
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJIT3",

    "name": "Credit sales exceeding limit",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Credit sales exceeding limit"),

            "cards": [

                {"id": "k1", "label": "Total Value", "agg": "total_value", "source": "amount", "format": "currency"},

                {"id": "k2", "label": "Exceptions", "agg": "row_count"},

                {"id": "k3", "label": "Unique Customers", "agg": "unique", "source": "customer"},

                {"id": "k4", "label": "Avg Impact", "agg": "avg", "source": "amount"},

                {"id": "k5", "label": "Max Deviation", "agg": "max", "source": "amount"},

                {"id": "k6", "label": "Total Base Records", "agg": "row_count"}
            ],

            "filters": [

                {"id": "f1", "label": "Country", "source": "country"},

                {"id": "f2", "label": "Region", "source": "region"},

                {"id": "f3", "label": "CCA Description", "source": "cca"}
            ],

            "charts": [

                {"id": "c1", "type": "doughnut", "x": "country", "agg": "count", "title": get_chart_title("Split by Country")},

                {"id": "c2", "type": "bar", "x": "customer", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": get_chart_title("Top Violators", "Customer")},

                {"id": "c3", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": get_chart_title("Timeline Trend")},

                {"id": "c4", "type": "bar", "x": "region", "agg": "count", "top_n": 10, "title": get_chart_title("Distribution", "Region")}
            ]
        }
    ],

    "columns": {

        "country": ["country_key"],

        "region": ["region"],

        "cca": ["cca_description"],

        "customer": ["name1"],

        "amount": ["tot_receivables"],

        "date": ["Posting Date"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer ITAC"
    }


def get_data(exc_id):

    path = rf"D:\off\JKC Dashboard\output\CJIT03_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')
