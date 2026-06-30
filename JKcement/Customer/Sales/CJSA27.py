# Customer/Sales/CJSA27.py — Sales return quantity variance for sold to party
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJSA27",

    "name": "Sales return quantity variance for sold to party",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Sales return quantity variance for sold to party"),

            "cards": [

                {"id": "k1", "label": "Company Code", "agg": "unique", "source": "company"},

                {"id": "k2", "label": "Material Number", "agg": "unique", "source": "material"},

                {"id": "k3", "label": "Batch No", "agg": "unique", "source": "batch"},

                {"id": "k4", "label": "Plant Code", "agg": "unique", "source": "plant"},

                {"id": "k5", "label": "Total Sales Qty", "agg": "sum", "source": "sales_qty"},

                {"id": "k6", "label": "Total Return Qty", "agg": "sum", "source": "return_qty"}
            ],

            "filters": [

                {"id": "f1", "label": "Company Name", "source": "company_name"},

                {"id": "f2", "label": "Qty Difference", "source": "qty_diff"},

                {"id": "f3", "label": "Material Description", "source": "material_desc"},

                {"id": "f4", "label": "Plant Code", "source": "plant"}
            ],

            "charts": [

                {"id": "c1", "type": "bar", "x": "material_desc", "y": "sales_qty", "agg": "sum", "title": get_chart_title("Material", "Sales Qty")},

                {"id": "c2", "type": "pie", "x": "plant", "y": "return_qty", "agg": "sum", "title": get_chart_title("Plant", "Return Qty")},

                {"id": "c3", "type": "bar", "x": "plant_name", "y": "qty_diff", "agg": "sum", "horizontal": True, "title": get_chart_title("Plant", "Qty Difference")}
            ]
        }
    ],

    "columns": {

        "company": ["Company Code"],

        "material": ["Material Number"],

        "batch": ["Batch No"],

        "plant": ["Plant Code"],

        "sales_qty": ["Total Sales Quantity"],

        "return_qty": ["Total Sales Return Quantity"],

        "company_name": ["Company Name"],

        "qty_diff": ["Qty Difference"],

        "material_desc": ["Material Description"],

        "plant_name": ["Plant Name"],

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

    path = rf"D:\off\JKC Dashboard\output\CJSA27_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')

