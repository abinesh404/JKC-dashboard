# Supplier/procurement/SJPR4.py — PO with non-global address
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR4",
    "name": "PO with non-global address",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Delivery Address in PO Different from Master Address"),
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
                    "label": "Unique Delivery Addresses",
                    "agg": "unique",
                    "source": "delivery_address"
                },
                {
                    "id": "k6",
                    "label": "Total PO Value",
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
                    "x": "vendor",
                    "agg": "count",
                    "top_n": 5,
                    "title": "Top 5 Vendors with Address Exceptions"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "plant",
                    "agg": "count",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Plants with Address Exceptions"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Address Exception Trend"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "company",
                    "agg": "count",
                    "title": "Company-wise Address Exception Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "po_region",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Region-wise Address Exceptions"
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
            "PLANT_NAME1",
            "PLANT_CITY1",
            "PLANT_REGION",
            "PLANT_COUNTRY"
        ],
        "vendor": [
            "Account Number of Vendor",
            "Vendor Name",
            "Address_Vendor"
        ],
        "po": [
            "Purchasing Document Number"
        ],
        "material": [
            "Material Number"
        ],
        "amount": [
            "Net PricePurchasing Doc."
        ],
        "date": [
            "Purchasing Document Date",
            "Date Record Was Created"
        ],
        "delivery_address": [
            "Delivery Address Number PO",
            "PO_NAME1",
            "PO_CITY1",
            "PO_POSTCODE",
            "PO_STREET",
            "PO_COUNTRY",
            "PO_REGION"
        ],
        "master_address": [
            "Address number plant",
            "PLANT_NAME1",
            "PLANT_CITY1",
            "PLANT_POSTCODE",
            "PLANT_STREET",
            "PLANT_COUNTRY",
            "PLANT_REGION"
        ],
        "po_region": [
            "PO_REGION"
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
        f"data_files/SJPR4_Exception0{exc_id}.csv",
        f"data_files/SJPR4_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
