# Supplier/procurement/SJPR2.py — Open Purchase Order
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR2",
    "name": "Open Purchase Order",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Open Purchase Orders – Ordered Quantity Not Fully Delivered"),
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
                    "label": "Purchase Orders",
                    "agg": "unique",
                    "source": "po"
                },
                {
                    "id": "k5",
                    "label": "Open Quantity",
                    "agg": "sum",
                    "source": "open_qty"
                },
                {
                    "id": "k6",
                    "label": "Open PO Value",
                    "agg": "total_value",
                    "source": "amount",
                    "format": "currency"
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
                    "y": "open_qty",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top Materials by Open Quantity"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "vendor",
                    "y": "open_qty",
                    "agg": "sum",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Vendors by Open Quantity"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Open PO Trend"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "company",
                    "y": "open_qty",
                    "agg": "sum",
                    "title": "Company-wise Open Quantity Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "plant",
                    "y": "open_qty",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Top Plants by Open Quantity"
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": get_exception_title("Goods Received but Invoice/Payment Pending"),
            "cards": [
                {
                    "id": "k1",
                    "label": "Companies",
                    "agg": "unique",
                    "source": "company"
                },
                {
                    "id": "k2",
                    "label": "Vendors",
                    "agg": "unique",
                    "source": "vendor"
                },
                {
                    "id": "k3",
                    "label": "Purchase Orders",
                    "agg": "unique",
                    "source": "po"
                },
                {
                    "id": "k4",
                    "label": "Total Billed Amount",
                    "agg": "sum",
                    "source": "billed_amount",
                    "format": "currency"
                },
                {
                    "id": "k5",
                    "label": "Open Amount",
                    "agg": "sum",
                    "source": "open_amount",
                    "format": "currency"
                },
                {
                    "id": "k6",
                    "label": "Pending Payments",
                    "agg": "row_count"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "Region", "source": "region"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "pie",
                    "x": "material",
                    "y": "open_amount",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top Materials by Open Amount"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "vendor",
                    "y": "open_amount",
                    "agg": "sum",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Vendors by Pending Amount"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Pending Invoice Trend"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "company",
                    "y": "open_amount",
                    "agg": "sum",
                    "title": "Company-wise Pending Amount Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "vendor",
                    "y": "open_amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Top Vendors by Pending Amount"
                }
            ]
        }
    ],
    "columns": {
        "company": [
            "Company Code"
        ],
        "plant": [
            "Plant",
            "Storage Location",
            "City",
            "Region"
        ],
        "vendor": [
            "Vendor Account Number",
            "Name 1"
        ],
        "material": [
            "Material Number"
        ],
        "qty": [
            "Purchase Order Quantity",
            "Quantity_MSEG"
        ],
        "open_qty": [
            "Open_Qty"
        ],
        "amount": [
            "Amount in document currency",
            "Billed_Amount",
            "Open_Amount",
            "Net Order Value in PO Currency",
            "Gross order value in PO currency"
        ],
        "billed_amount": [
            "Billed_Amount"
        ],
        "open_amount": [
            "Open_Amount"
        ],
        "date": [
            "Purchasing Document Date",
            "Purchase Order Document Date"
        ],
        "region": [
            "City",
            "Region"
        ],
        "po": [
            "Purchasing Document Number"
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
        f"data_files/SJPR2_Exception0{exc_id}.csv",
        f"data_files/SJPR2_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
