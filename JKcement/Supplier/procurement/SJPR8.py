# Supplier/procurement/SJPR8.py — Time gap PO vs GRN Date
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR8",
    "name": "Time gap PO vs GRN Date",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Non-Standard Movement Types"),
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
                    "label": "Material Documents",
                    "agg": "unique",
                    "source": "mat_doc"
                },
                {
                    "id": "k6",
                    "label": "Total Amount (LC)",
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
                    "x": "movement_type",
                    "agg": "count",
                    "top_n": 5,
                    "title": "Top 5 Movement Types"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "vendor",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Vendors by Transaction Value"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Exception Trend"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "company_name",
                    "agg": "count",
                    "title": "Company-wise Exception Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "plant_code",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Top Plants by Exception Count"
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": get_exception_title("PO vs GRN Delay Greater Than 180 Days"),
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
                    "label": "Material Documents",
                    "agg": "unique",
                    "source": "mat_doc"
                },
                {
                    "id": "k5",
                    "label": "Average Delay Days",
                    "agg": "avg",
                    "source": "delay_days"
                },
                {
                    "id": "k6",
                    "label": "Maximum Delay Days",
                    "agg": "max",
                    "source": "delay_days"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "Purchasing Group", "source": "purch_group"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "pie",
                    "x": "vendor",
                    "y": "delay_days",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top Vendors by Delay Days"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "purch_group",
                    "y": "delay_days",
                    "agg": "sum",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top Purchasing Groups by Delay"
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
                    "x": "company_name",
                    "agg": "count",
                    "title": "Company-wise Delay Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "user",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Top Users Creating Delayed POs"
                }
            ]
        },
        {
            "id": "3",
            "label": "Exception 03",
            "title": get_exception_title("Negative Price Difference Between PO and GRN"),
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
                    "label": "Average PO Price",
                    "agg": "avg",
                    "source": "po_price",
                    "format": "currency"
                },
                {
                    "id": "k5",
                    "label": "Average GRN Price",
                    "agg": "avg",
                    "source": "grn_price",
                    "format": "currency"
                },
                {
                    "id": "k6",
                    "label": "Total Negative Price Difference",
                    "agg": "sum",
                    "source": "price_diff",
                    "format": "currency"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "Purchasing Group", "source": "purch_group"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "pie",
                    "x": "vendor",
                    "y": "price_diff",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top Vendors by Negative Price Difference"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "purch_group",
                    "y": "price_diff",
                    "agg": "sum",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top Purchasing Groups by Price Variance"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Price Difference Trend"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "company_name",
                    "agg": "count",
                    "title": "Company-wise Price Variance Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "user",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Top Users with Price Variances"
                }
            ]
        }
    ],
    "columns": {
        "company": [
            "Company Code",
            "Company Name"
        ],
        "company_name": [
            "Company Name"
        ],
        "plant": [
            "Plant Code",
            "City",
            "Country Key"
        ],
        "plant_code": [
            "Plant Code"
        ],
        "vendor": [
            "Vendor"
        ],
        "material": [
            "Material No",
            "Material"
        ],
        "po": [
            "Purchasing Document",
            "Purchase Group"
        ],
        "purch_group": [
            "Purch. Group",
            "Purchase Group"
        ],
        "mat_doc": [
            "Material Document",
            "Material Doc. Item"
        ],
        "qty": [
            "Quantity",
            "Del. Note Quantity"
        ],
        "amount": [
            "Amount in LC",
            "PO_Derived_Price",
            "GRN_Derived_Price",
            "Material_Net_Price",
            "Price_Diff"
        ],
        "price_diff": [
            "Price_Diff"
        ],
        "po_price": [
            "PO_Derived_Price"
        ],
        "grn_price": [
            "GRN_Derived_Price"
        ],
        "date": [
            "Document Date",
            "Posting Date",
            "Entry Date",
            "Created On"
        ],
        "user": [
            "User name",
            "Created by"
        ],
        "movement_type": [
            "Movement Type_EKBE"
        ],
        "delay_days": [
            "date&time diff"
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
        f"data_files/SJPR8_Exception0{exc_id}.csv",
        f"data_files/SJPR8_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
