# Supplier/procurement/SJPR1.py — Delay in PR to PO
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR1",
    "name": "Delay in PR to PO",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Delay Greater than 30 Days"),
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
                    "label": "PR Numbers",
                    "agg": "unique",
                    "source": "pr"
                },
                {
                    "id": "k4",
                    "label": "PO Numbers",
                    "agg": "unique",
                    "source": "po"
                },
                {
                    "id": "k5",
                    "label": "Total Quantity",
                    "agg": "sum",
                    "source": "qty"
                },
                {
                    "id": "k6",
                    "label": "Total Value",
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
                    "y": "qty",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top Materials by Quantity"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "vendor",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Vendors by Value"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Delay Trend"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "company",
                    "y": "qty",
                    "agg": "sum",
                    "title": "Company Quantity Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "plant",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Top Plants by Value"
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": get_exception_title("Negative Day Difference"),
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
                    "label": "PR Numbers",
                    "agg": "unique",
                    "source": "pr"
                },
                {
                    "id": "k4",
                    "label": "PO Numbers",
                    "agg": "unique",
                    "source": "po"
                },
                {
                    "id": "k5",
                    "label": "Total Quantity",
                    "agg": "sum",
                    "source": "qty"
                },
                {
                    "id": "k6",
                    "label": "Total Value",
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
                    "y": "qty",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top Materials by Quantity"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "vendor",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Vendors by Value"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Negative Cases"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "company",
                    "y": "qty",
                    "agg": "sum",
                    "title": "Company Quantity Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "plant",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Top Plants by Value"
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
            "Plant",
            "City"
        ],
        "material": [
            "Material",
            "PO_Material"
        ],
        "qty": [
            "Quantity"
        ],
        "amount": [
            "Net price"
        ],
        "vendor": [
            "Vendor"
        ],
        "pr": [
            "PR number"
        ],
        "po": [
            "PO number"
        ],
        "date": [
            "PO creation date"
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
        f"data_files/SJPR1_Exception0{exc_id}.csv",
        f"data_files/SJPR1_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
