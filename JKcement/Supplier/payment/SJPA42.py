# Supplier/payment/SJPA42.py
import pandas as pd
import os
from .template import get_exception_title, get_chart_title

CONFIG = {
    "id": "SJPA42",
    "name": "Payment to Blocked Invoices",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Payment Made to Blocked Invoices"),
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
                    "label": "Blocked Invoices",
                    "agg": "unique",
                    "source": "document"
                },
                {
                    "id": "k4",
                    "label": "Payment Documents",
                    "agg": "unique",
                    "source": "document"
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
                    "label": "Payment Blocks",
                    "agg": "unique",
                    "source": "payment_block"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "Payment Block", "source": "payment_block"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "pie",
                    "x": "vendor",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top Vendors by Payment Amount"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "company",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Top Companies by Blocked Payments"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Blocked Payment Trend"
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
                    "x": "payment_method",
                    "agg": "count",
                    "title": "Payment Method Distribution"
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
        "vendor": [
            "Vendor Code",
            "Vendor Name"
        ],
        "amount": [
            "Amount in Local Currency",
            "Amount in document currency"
        ],
        "document": [
            "Accounting Document Number",
            "Document Type"
        ],
        "gl": [
            "G/L Account Number",
            "General Ledger Account"
        ],
        "date": [
            "Posting Date",
            "Document Date in Document",
            "Due date of an invoice"
        ],
        "payment_block": [
            "Payment Block Key",
            "Payment Block Key(BSEG)",
            "Logistics payment block"
        ],
        "payment_method": [
            "Payment Method (REGUP)"
        ],
        "user": [
            "User name"
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
        f"data_files/SJPA42_Exception0{exc_id}.csv",
        f"data_files/SJPA42_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
