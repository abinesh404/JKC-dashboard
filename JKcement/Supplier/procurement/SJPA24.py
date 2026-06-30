# Supplier/procurement/SJPA24.py — Invoice Date prior to PO date
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPA24",
    "name": "Invoice Date prior to PO date",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Invoice Date prior to PO date"),
            "cards": [
                        {
                                        "id": "k1",
                                        "label": "Companies",
                                        "agg": "unique",
                                        "source": "company"
                        },
                        {
                                        "id": "k2",
                                        "label": "Plants",
                                        "agg": "unique",
                                        "source": "plant"
                        },
                        {
                                        "id": "k3",
                                        "label": "Vendors",
                                        "agg": "unique",
                                        "source": "vendor"
                        },
                        {
                                        "id": "k4",
                                        "label": "Total Invoices",
                                        "agg": "row_count"
                        },
                        {
                                        "id": "k5",
                                        "label": "Total Amount",
                                        "agg": "total_value",
                                        "source": "amount",
                                        "format": "currency"
                        },
                        {
                                        "id": "k6",
                                        "label": "Avg Prior Days",
                                        "agg": "avg",
                                        "source": "prior_days"
                        }
        ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "Plant", "source": "plant"}
            ],
            "charts": [
                        {
                                        "id": "c1",
                                        "type": "pie",
                                        "x": "material",
                                        "y": "qty",
                                        "agg": "sum",
                                        "top_n": 5,
                                        "title": "Top Materials by Qty"
                        },
                        {
                                        "id": "c2",
                                        "type": "bar",
                                        "x": "vendor",
                                        "y": "prior_days",
                                        "agg": "avg",
                                        "top_n": 10,
                                        "horizontal": "true",
                                        "title": "Top 10 Vendors by Avg Prior Days"
                        },
                        {
                                        "id": "c3",
                                        "type": "line",
                                        "x": "date",
                                        "y": "amount",
                                        "agg": "sum",
                                        "time_group": "month",
                                        "title": "Prior Invoice Value Trend"
                        },
                        {
                                        "id": "c4",
                                        "type": "doughnut",
                                        "x": "company",
                                        "y": "amount",
                                        "agg": "sum",
                                        "title": "Company Spend Share"
                        },
                        {
                                        "id": "c5",
                                        "type": "bar",
                                        "x": "plant",
                                        "y": "prior_days",
                                        "agg": "avg",
                                        "top_n": 10,
                                        "title": "Top Plants by Avg Prior Days"
                        }
        ]
        }
    ],
    "columns": {
            "company": [
                    "Company Code",
                    "Company Name"
            ],
            "plant": [
                    "Plant Code",
                    "Plant Name",
                    "Plant City"
            ],
            "material": [
                    "Material Number",
                    "Item Text"
            ],
            "qty": [
                    "Quantity"
            ],
            "amount": [
                    "Amount in document currency"
            ],
            "vendor": [
                    "Vendor Name",
                    "Vendor Code"
            ],
            "prior_days": [
                    "Invoice Date Prior to PO Date"
            ],
            "date": [
                    "Invoice Date",
                    "PO Date"
            ],
            "po": [
                    "Purchasing Document Number",
                    "Accounting Document Number"
            ]
    }
}


def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Supplier Procurement"
    }


def get_data(exc_id):
    paths = [
        f"data_files/SJPA24_Exception0{exc_id}.csv",
        f"data_files/SJPA24_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
