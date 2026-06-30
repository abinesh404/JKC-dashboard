# Supplier/procurement/SJPR25.py — Invoice Date Prior to PO Date – Part II
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR25",
    "name": "Invoice Date Prior to PO Date – Part II",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Invoice Date and PO Creation Date are the Same"),
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
                    "label": "Accounting Documents",
                    "agg": "unique",
                    "source": "invoice"
                },
                {
                    "id": "k5",
                    "label": "Purchase Orders",
                    "agg": "unique",
                    "source": "po"
                },
                {
                    "id": "k6",
                    "label": "Total Invoice Amount",
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
                    "x": "vendor_name",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top 5 Vendors by Invoice Amount"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "plant_name",
                    "agg": "count",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Plants by Invoice Count"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "invoice_date",
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
                    "title": "Company-wise Invoice Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "purch_group",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Top Purchasing Groups by Invoice Value"
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": get_exception_title("Entry Date Before PO Date or Equal to Invoice Date"),
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
                    "label": "Accounting Documents",
                    "agg": "unique",
                    "source": "invoice"
                },
                {
                    "id": "k5",
                    "label": "Purchase Orders",
                    "agg": "unique",
                    "source": "po"
                },
                {
                    "id": "k6",
                    "label": "Total Invoice Amount",
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
                    "x": "vendor_name",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top 5 Vendors by Invoice Amount"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "plant_name",
                    "agg": "count",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Plants by Exception Count"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "entry_date",
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
                    "title": "Company-wise Invoice Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "user",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Top Users by Exception Count"
                }
            ]
        },
        {
            "id": "3",
            "label": "Exception 03",
            "title": get_exception_title("Posting Date Before PO Date or Equal to Invoice Date"),
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
                    "label": "Accounting Documents",
                    "agg": "unique",
                    "source": "invoice"
                },
                {
                    "id": "k5",
                    "label": "Purchase Orders",
                    "agg": "unique",
                    "source": "po"
                },
                {
                    "id": "k6",
                    "label": "Total Invoice Amount",
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
                    "x": "vendor_name",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top 5 Vendors by Invoice Amount"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "plant_name",
                    "agg": "count",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Plants by Exception Count"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "posting_date",
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
                    "title": "Company-wise Invoice Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "user",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Top Users by Exception Count"
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
        "vendor_name": [
            "Vendor Name"
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
        "po": [
            "Purchasing Document Number",
            "Item Number of Purchasing Document",
            "Purchasing Document Type"
        ],
        "purch_group": [
            "Purchasing Group"
        ],
        "invoice": [
            "Accounting Document Number",
            "Document Type",
            "Document Item in Invoice Document"
        ],
        "invoice_date": [
            "Invoice Date"
        ],
        "entry_date": [
            "Entry Date"
        ],
        "posting_date": [
            "Posting Date in the Document"
        ],
        "date": [
            "Invoice Date",
            "PO Date",
            "Entry Date",
            "Posting Date in the Document"
        ],
        "user": [
            "User name",
            "Entered by external system user",
            "Name of Person who Created the Object"
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
        f"data_files/SJPR25_Exception0{exc_id}.csv",
        f"data_files/SJPR25_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
