# Customer/Sales/CJSA25.py — Delivery in excess to the tolerance defined for sales order. (Qty and Transactional)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJSA25",

    "name": "Delivery in excess to the tolerance defined for sales order. (Qty and Transactional)",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Delivery in excess to the tolerance defined for sales order. (Qty and Transactional)"),

            "cards": [

                {"id": "k1", "label": "Company Codes", "agg": "unique", "source": "company"},

                {"id": "k2", "label": "Pricing Procedures", "agg": "unique", "source": "pricing"},

                {"id": "k3", "label": "Docs", "agg": "unique", "source": "docs"},

                {"id": "k4", "label": "Condition Types", "agg": "unique", "source": "condition"},

                {"id": "k5", "label": "Sales Org", "agg": "unique", "source": "sales_org"},

                {"id": "k6", "label": "% Diff", "agg": "sum", "source": "diff"}
            ],

            "filters": [

                {"id": "f1", "label": "Company Code", "source": "company"},

                {"id": "f2", "label": "Billing Type", "source": "billing_type"},

                {"id": "f3", "label": "Division", "source": "division"},

                {"id": "f4", "label": "Pricing Date", "source": "date"}
            ],

            "charts": [

                {"id": "c1", "type": "bar", "x": "billing_doc", "y": "diff", "agg": "sum", "title": get_chart_title("Billing Document", "% Diff")},

                {"id": "c2", "type": "pie", "x": "company", "y": "gross_weight", "agg": "count", "title": get_chart_title("Company", "Gross Weight Count")},

                {"id": "c3", "type": "bar", "x": "material", "y": "net_price", "agg": "count", "horizontal": True, "title": get_chart_title("Material", "Net Price Count")},

                {"id": "c4", "type": "line", "x": "date", "y": "diff", "agg": "sum", "time_group": "month", "title": get_chart_title("Pricing Date", "% Diff Trend")},

                {"id": "c5", "type": "doughnut", "x": "material", "y": "net_price", "agg": "sum", "title": get_chart_title("Material", "Net Price")}
            ]
        }
    ],

    "columns": {

        "company": ["Company Code"],

        "pricing": ["Pricing Procedures"],

        "docs": ["Docs"],

        "condition": ["Condition Types"],

        "sales_org": ["Sales Organisation"],

        "diff": ["%Diff"],

        "billing_type": ["Billing Type"],

        "division": ["Division"],

        "billing_doc": ["Billing Document"],

        "gross_weight": ["Gross weight"],

        "material": ["Material Number"],

        "net_price": ["NetPrice"],

        "date": ["Date for pricing and exchange rate"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer Sales"
    }


def get_data(exc_id):

    path = rf"D:\off\JKC Dashboard\output\CJSA25_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')

