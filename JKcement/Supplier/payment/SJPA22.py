# Supplier/payment/SJPA22.py
import pandas as pd
import os
from .template import get_exception_title, get_chart_title

CONFIG = {
    "id": "SJPA22",
    "name": "Payment Released without Quality Clearance",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Payment Released Without Quality Clearance"),
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
                    "source": "purchase_order"
                },
                {
                    "id": "k4",
                    "label": "Inspection Lots",
                    "agg": "unique",
                    "source": "inspection_lot"
                },
                {
                    "id": "k5",
                    "label": "Total Payment Amount",
                    "agg": "total_value",
                    "source": "amount",
                    "format": "currency"
                },
                {
                    "id": "k6",
                    "label": "Average Delay (Days)",
                    "agg": "avg",
                    "source": "delay"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "Plant", "source": "plant"},
                {"id": "f4", "label": "Purchasing Organization", "source": "purchasing_org"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "pie",
                    "x": "vendor",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top 5 Vendors by Payment Amount"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "plant",
                    "agg": "count",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Plants by Exception Count"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "clearing_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Payment Release Trend"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "company_name",
                    "y": "amount",
                    "agg": "sum",
                    "title": "Company-wise Payment Distribution"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "purchasing_org",
                    "agg": "count",
                    "title": "Purchasing Organizations with Maximum Exceptions"
                }
            ]
        }
    ],
    "columns": {
        "company": [
            "Company Code",
            "Name of Company",
            "City",
            "Country Key"
        ],
        "company_name": [
            "Name of Company"
        ],
        "vendor": [
            "Vendor Account Number",
            "VAT Registration Number"
        ],
        "purchase_order": [
            "Purchasing Document Number",
            "Purchasing Document Type",
            "Purchasing Organization",
            "Purchasing Group",
            "Item Number of Purchasing Document"
        ],
        "purchasing_org": [
            "Purchasing Organization"
        ],
        "material": [
            "Material Number",
            "Short Text Material Description",
            "Plant"
        ],
        "plant": [
            "Plant"
        ],
        "quantity": [
            "Purchase Order Quantity",
            "Purchase Order Unit of Measure"
        ],
        "amount": [
            "Amount in Local Currency",
            "Net Value",
            "Net Price",
            "Amount in Document Currency",
            "Currency Key"
        ],
        "quality_inspection": [
            "Inspection Lot Number",
            "Catalog",
            "Usage Decision Code",
            "Usage Decision Has Been Made",
            "Date of Code Used for Usage Decision"
        ],
        "inspection_lot": [
            "Inspection Lot Number"
        ],
        "accounting": [
            "Accounting Document Number",
            "Document Number of the Clearing Document",
            "Document Type",
            "Fiscal Year",
            "Number of Line Item Within Accounting Document",
            "Terms of Payment Key",
            "Reversal Doc"
        ],
        "date": [
            "Clearing Date",
            "Purchasing Document Date",
            "Posting Date in the Document",
            "Day On Which Accounting Document Was Entered",
            "Date on Which the Data Record Was Created"
        ],
        "clearing_date": [
            "Clearing Date"
        ],
        "delay": [
            "Days_Difference (AUGDT – VDATUM)",
            "Days_Difference"
        ],
        "user": [
            "User Name"
        ],
        "exception": [
            "Exception"
        ]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Supplier Payment"
    }

def get_data(exc_id):
    paths = [
        f"data_files/SJPA22_Exception0{exc_id}.csv",
        f"data_files/SJPA22_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
