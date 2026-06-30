
# Customer/Sales/CJSA21.py — Sale price
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJSA21",

    "name": "Sale price",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Sale price"),

            "cards": [

                {"id": "k1", "label": "Company Name", "agg": "unique", "source": "company"},

                {"id": "k2", "label": "Plant", "agg": "unique", "source": "plant"},

                {"id": "k3", "label": "Material Number", "agg": "unique", "source": "material"},

                {"id": "k4", "label": "Customer", "agg": "unique", "source": "customer"},

                {"id": "k5", "label": "Billing Document", "agg": "unique", "source": "billing_doc"},

                {"id": "k6", "label": "Impact", "agg": "sum", "source": "impact", "format": "currency"}
            ],

            "filters": [

                {"id": "f1", "label": "Company Name", "source": "company"},

                {"id": "f2", "label": "Material Description", "source": "material_desc"},

                {"id": "f3", "label": "Sold to Party Name", "source": "customer_name"},

                {"id": "f4", "label": "Created On", "source": "date"}
            ],

            "charts": [

                {"id": "c1", "type": "bar", "x": "sd_type", "y": "billing_doc", "agg": "count", "title": get_chart_title("SD Type", "Billing Docs")},

                {"id": "c2", "type": "line", "x": "date", "y": "impact", "agg": "sum", "time_group": "month", "title": get_chart_title("Created On", "Impact Trend")},

                {"id": "c3", "type": "bar", "x": "material_desc", "y": "impact", "agg": "sum", "horizontal": True, "top_n": 10, "title": get_chart_title("Material", "Impact")},

                {"id": "c4", "type": "pie", "x": "billing_type", "y": "billing_doc", "agg": "count", "title": get_chart_title("Billing Type", "Billing Docs")}
            ]
        }
    ],

    "columns": {

        "company": ["Company Name"],

        "plant": ["Plant"],

        "material": ["Material Number"],

        "customer": ["Sold to Party"],

        "billing_doc": ["Billing Document"],

        "impact": ["Impact"],

        "material_desc": ["Material Description"],

        "customer_name": ["Sold to Party Name"],

        "sd_type": ["SD Type Description"],

        "billing_type": ["Billing Type Description"],

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

    path = rf"D:\off\JKC Dashboard\output\CJSA21_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')

