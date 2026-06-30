# Supplier/procurement/SJPR27.py — High Price PO – Minimum & Average Price (Six Month)
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR27",
    "name": "High Price PO – Minimum & Average Price (Six Month)",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("High Price PO – Minimum & Average Price (Six Month Period)"),
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
                    "label": "Average Unit Price",
                    "agg": "avg",
                    "source": "unit_price",
                    "format": "currency"
                },
                {
                    "id": "k6",
                    "label": "Total Purchase Value",
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
                    "x": "material_desc",
                    "y": "qty",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top 5 Materials by Quantity Ordered"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "vendor",
                    "y": "unit_price",
                    "agg": "avg",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Vendors by Average Unit Price"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "created_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Exception Trend"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "company_name",
                    "y": "amount",
                    "agg": "sum",
                    "title": "Company-wise Purchase Value Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "plant",
                    "y": "unit_price",
                    "agg": "avg",
                    "top_n": 10,
                    "title": "Top Plants by Average Unit Price"
                }
            ]
        }
    ],
    "columns": {
        "company": [
            "Company Code",
            "Company Name",
            "City",
            "Country Code"
        ],
        "company_name": [
            "Company Name"
        ],
        "plant": [
            "Plant",
            "Storage Location"
        ],
        "vendor": [
            "Vendor Number",
            "Customer Number",
            "Payment Terms"
        ],
        "material": [
            "Material Number",
            "Material Description",
            "Material Group"
        ],
        "material_desc": [
            "Material Description"
        ],
        "qty": [
            "Quantity Ordered"
        ],
        "amount": [
            "Net Value (Total Amount)"
        ],
        "unit_price": [
            "Net Price (per unit)"
        ],
        "price": [
            "Min_Price",
            "Avg_Price",
            "Net Price (per unit)"
        ],
        "po": [
            "Purchase Order Number",
            "Purchase Order Item Number",
            "Purchase Order Category",
            "Document Type",
            "Item Category"
        ],
        "date": [
            "Document Date in Document",
            "Date on Created",
            "Month",
            "six month Period"
        ],
        "created_date": [
            "Date on Created"
        ],
        "user": [
            "Created By"
        ],
        "prediction": [
            "prediction"
        ],
        "six_month_period": [
            "six month Period"
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
        f"data_files/SJPR27_Exception0{exc_id}.csv",
        f"data_files/SJPR27_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
