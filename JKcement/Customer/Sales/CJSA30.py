# Customer/Sales/CJSA29.py — Pending Processing
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJSA29",

    "name": "Pending Processing",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Pending Processing"),

            "cards": [

                {"id": "k1", "label": "Company Code", "agg": "unique", "source": "company"},

                {"id": "k2", "label": "Billing Document", "agg": "unique", "source": "billing_doc"},

                {"id": "k3", "label": "Material", "agg": "unique", "source": "material"},

                {"id": "k4", "label": "Plant", "agg": "unique", "source": "plant"},

                {"id": "k5", "label": "Customer", "agg": "unique", "source": "customer"},

                {"id": "k6", "label": "Pending Amount", "agg": "sum", "source": "amount", "format": "currency"}
            ],

            "filters": [

                {"id": "f1", "label": "Company Name", "source": "company_name"},

                {"id": "f2", "label": "Billing Type", "source": "billing_type"},

                {"id": "f3", "label": "Material Description", "source": "material_desc"},

                {"id": "f4", "label": "Created On", "source": "date"}
            ],

            "charts": [

                {"id": "c1", "type": "bar", "x": "company_name", "y": "amount", "agg": "sum", "top_n": 10, "title": get_chart_title("Company", "Pending Amount")},

                {"id": "c2", "type": "pie", "x": "billing_type", "y": "billing_doc", "agg": "count", "title": get_chart_title("Billing Type", "Billing Docs")},

                {"id": "c3", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": get_chart_title("Created On", "Pending Trend")},

                {"id": "c4", "type": "doughnut", "x": "plant", "y": "amount", "agg": "sum", "title": get_chart_title("Plant", "Pending Amount")},

                {"id": "c5", "type": "bar", "x": "material_desc", "y": "amount", "agg": "sum", "horizontal": True, "top_n": 10, "title": get_chart_title("Material", "Pending Amount")}
            ]
        }
    ],

    "columns": {

        "company": ["Company Code"],

        "billing_doc": ["Billing Document"],

        "material": ["Material"],

        "plant": ["Plant"],

        "customer": ["Sold to Party"],

        "amount": ["Pending Amount"],

        "company_name": ["Company Name"],

        "billing_type": ["Billing Type"],

        "material_desc": ["Material Description"],

        "date": ["Created On"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer Sales"
    }


def get_data(exc_id):

    path = rf"D:\off\JKC Dashboard\output\CJSA29_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')

