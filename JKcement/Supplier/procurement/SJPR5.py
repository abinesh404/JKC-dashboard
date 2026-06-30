# Supplier/procurement/SJPR5.py — Single Source Vendors
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR5",
    "name": "Single Source Vendors",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Single Source Vendor – Plant Level"),
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
                    "label": "Materials",
                    "agg": "unique",
                    "source": "material"
                },
                {
                    "id": "k5",
                    "label": "Purchase Orders",
                    "agg": "unique",
                    "source": "po"
                },
                {
                    "id": "k6",
                    "label": "Total Procurement Value",
                    "agg": "total_value",
                    "source": "amount",
                    "format": "currency"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Plant", "source": "plant"},
                {"id": "f3", "label": "Vendor", "source": "vendor"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "pie",
                    "x": "vendor",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top 5 Vendors by Procurement Value"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "plant_name",
                    "agg": "count",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Plants with Single Source Vendors"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Single Source Vendor Trend"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "company_name",
                    "agg": "count",
                    "title": "Company-wise Single Source Vendor Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "material_group",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Material Groups with Single Source Dependency"
                }
            ]
        }
    ],
    "columns": {
        "company": [
            "Company Code",
            "Company Name",
            "Company City"
        ],
        "company_name": [
            "Company Name"
        ],
        "plant": [
            "Plant Code",
            "Plant Name",
            "Plant City"
        ],
        "plant_name": [
            "Plant Name"
        ],
        "vendor": [
            "Vendor Code",
            "Vendor Name",
            "Vendor City"
        ],
        "material": [
            "Material Number",
            "Material Type",
            "Material Group",
            "Material Description"
        ],
        "material_group": [
            "Material Group"
        ],
        "qty": [
            "Purchase Order Quantity"
        ],
        "amount": [
            "Net Price in Purchasing Document (in Document Currency)"
        ],
        "po": [
            "Purchasing Document Number",
            "Item Number of Purchasing Document",
            "Purchasing Document Type",
            "Purchasing Document Category"
        ],
        "date": [
            "Purchasing Document Date"
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
        f"data_files/SJPR5_Exception0{exc_id}.csv",
        f"data_files/SJPR5_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
