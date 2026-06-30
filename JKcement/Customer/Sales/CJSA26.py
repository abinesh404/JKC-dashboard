# Customer/Sales/CJSA26.py — Sales return quantity variance
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJSA26",

    "name": "Sales return quantity variance",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Sales return quantity variance"),

            "cards": [

                {"id": "k1", "label": "Company Code", "agg": "unique", "source": "company"},

                {"id": "k2", "label": "Material", "agg": "unique", "source": "material"},

                {"id": "k3", "label": "Plant", "agg": "unique", "source": "plant"},

                {"id": "k4", "label": "Billing Doc", "agg": "unique", "source": "billing_doc"},

                {"id": "k5", "label": "Batch", "agg": "unique", "source": "batch"},

                {"id": "k6", "label": "Net Value", "agg": "sum", "source": "net_value", "format": "currency"}
            ],

            "filters": [

                {"id": "f1", "label": "Material", "source": "material"},

                {"id": "f2", "label": "Billing Type", "source": "billing_type"},

                {"id": "f3", "label": "Combined String", "source": "combined"},

                {"id": "f4", "label": "Created On", "source": "date"}
            ],

            "charts": [

                {"id": "c1", "type": "bar", "x": "material", "y": "shelf_life", "agg": "sum", "title": get_chart_title("Material", "Shelf Life")},

                {"id": "c2", "type": "doughnut", "x": "billing_doc", "y": "net_value", "agg": "sum", "title": get_chart_title("Billing Doc", "Net Value")},

                {"id": "c3", "type": "bar", "x": "sales_doc", "y": "shelf_life", "agg": "sum", "horizontal": True, "title": get_chart_title("Sales Document", "Shelf Life")},

                {"id": "c4", "type": "pie", "x": "billing_type", "y": "net_value", "agg": "sum", "title": get_chart_title("Billing Type", "Net Value")}
            ]
        }
    ],

    "columns": {

        "company": ["Company Code"],

        "material": ["Material"],

        "plant": ["Plant"],

        "billing_doc": ["Billing Document"],

        "batch": ["Batch"],

        "net_value": ["Net Value"],

        "billing_type": ["Billing Type"],

        "combined": ["Combined String"],

        "sales_doc": ["Sales Document"],

        "shelf_life": ["Remaining Shelf Life"],

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

    path = rf"D:\off\JKC Dashboard\output\CJSA26_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')

