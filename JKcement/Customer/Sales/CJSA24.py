# Customer/Sales/CJSA24.py — Timely manner of LR date and Invoice date
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJSA24",

    "name": "Timely manner of LR date and Invoice date",

    "active_exceptions": [

        {
            "id": "1",

            "label": "Exception 01",

            "title": get_exception_title("Timely manner of LR date and Invoice date"),

            "cards": [

                {"id": "k1", "label": "Vendor Code", "agg": "unique", "source": "vendor"},

                {"id": "k2", "label": "Invoice Doc", "agg": "unique", "source": "invoice_doc"},

                {"id": "k3", "label": "PO Number", "agg": "unique", "source": "po_number"},

                {"id": "k4", "label": "Delivery Number", "agg": "unique", "source": "delivery"},

                {"id": "k5", "label": "Delivery Item", "agg": "unique", "source": "delivery_item"},

                {"id": "k6", "label": "Gross Amount", "agg": "sum", "source": "gross_amount", "format": "currency"}
            ],

            "filters": [

                {"id": "f1", "label": "Vendor Name", "source": "vendor_name"},

                {"id": "f2", "label": "Delivery Type", "source": "delivery_type"},

                {"id": "f3", "label": "Days Difference", "source": "days_diff"},

                {"id": "f4", "label": "Invoice Date", "source": "date"}
            ],

            "charts": [

                {"id": "c1", "type": "bar", "x": "vendor_name", "y": "days_diff", "agg": "avg", "title": get_chart_title("Vendor", "Avg Days Difference")},

                {"id": "c2", "type": "pie", "x": "delivery_type", "y": "delivery", "agg": "count", "title": get_chart_title("Delivery Type", "Documents")},

                {"id": "c3", "type": "bar", "x": "delivery", "y": "delivery", "agg": "count", "horizontal": True, "title": get_chart_title("Delivery Number", "Count")},

                {"id": "c4", "type": "line", "x": "date", "y": "days_diff", "agg": "avg", "time_group": "month", "title": get_chart_title("Invoice Date", "Days Difference Trend")},

                {"id": "c5", "type": "doughnut", "x": "material", "y": "days_diff", "agg": "sum", "title": get_chart_title("Material", "Days Difference")}
            ]
        }
    ],

    "columns": {

        "vendor": ["Vendor Code"],

        "invoice_doc": ["Invoice Document Number"],

        "po_number": ["Purchase Order Number"],

        "delivery": ["Delivery Number"],

        "delivery_item": ["Delivery Item"],

        "gross_amount": ["Gross Invoice Amount"],

        "vendor_name": ["Vendor Name"],

        "delivery_type": ["Delivery Type"],

        "days_diff": ["Days_Difference"],

        "material": ["Material"],

        "date": ["Invoice Date"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer Sales"
    }


def get_data(exc_id):

    path = rf"D:\off\JKC Dashboard\output\CJSA24_Exception{int(exc_id):02}.csv"

    if not os.path.exists(path):

        return None

    return pd.read_csv(
        path,
        encoding='latin1',
        low_memory=False
    ).fillna('')

