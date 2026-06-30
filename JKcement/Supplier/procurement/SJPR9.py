# Supplier/procurement/SJPR9.py — Split Purchase Requisition
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR9",
    "name": "Split Purchase Requisition",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Split PR Within 10 Days"),
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
                    "label": "Purchase Requisitions",
                    "agg": "unique",
                    "source": "pr"
                },
                {
                    "id": "k5",
                    "label": "Total Quantity",
                    "agg": "sum",
                    "source": "qty"
                },
                {
                    "id": "k6",
                    "label": "Material Groups",
                    "agg": "unique",
                    "source": "material_group"
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
                    "x": "material_group",
                    "y": "qty",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top 5 Material Groups by Quantity"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "vendor",
                    "agg": "count",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Vendors by PR Count"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Split PR Trend"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "company_name",
                    "agg": "count",
                    "title": "Company-wise Split PR Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "plant",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Top Plants by Split PR Count"
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": get_exception_title("Split PR Within 30 Days"),
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
                    "label": "Purchase Requisitions",
                    "agg": "unique",
                    "source": "pr"
                },
                {
                    "id": "k5",
                    "label": "Total Quantity",
                    "agg": "sum",
                    "source": "qty"
                },
                {
                    "id": "k6",
                    "label": "Material Groups",
                    "agg": "unique",
                    "source": "material_group"
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
                    "x": "material_group",
                    "y": "qty",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top 5 Material Groups by Quantity"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "vendor",
                    "agg": "count",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Vendors by PR Count"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Split PR Trend"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "company_name",
                    "agg": "count",
                    "title": "Company-wise Split PR Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "plant",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Top Plants by Split PR Count"
                }
            ]
        }
    ],
    "columns": {
        "company": [
            "Company Code",
            "Company Name",
            "City",
            "Country"
        ],
        "company_name": [
            "Company Name"
        ],
        "plant": [
            "Plant",
            "Storage Location"
        ],
        "vendor": [
            "Vendor",
            "Related_Vendor"
        ],
        "material": [
            "Material Number",
            "Material Description",
            "Material Group",
            "Material Type",
            "Old Material Number"
        ],
        "material_group": [
            "Material Group"
        ],
        "qty": [
            "Quantity",
            "Related_Quantity"
        ],
        "pr": [
            "Purchase Requisition Number",
            "Related PR No."
        ],
        "date": [
            "Creation Date",
            "Related PR Date",
            "Last Change Date"
        ],
        "user": [
            "Created By"
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
        f"data_files/SJPR9_Exception0{exc_id}.csv",
        f"data_files/SJPR9_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
