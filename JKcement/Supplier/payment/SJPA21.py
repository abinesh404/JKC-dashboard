# Supplier/payment/SJPA21.py
import pandas as pd
import os
from .template import get_exception_title, get_chart_title

CONFIG = {
    "id": "SJPA21",
    "name": "Bank Payments without Vendor & Customer",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Bank Payments Posted without Linking to Any Vendor or Customer"),
            "cards": [
                {
                    "id": "k1",
                    "label": "Companies",
                    "agg": "unique",
                    "source": "company"
                },
                {
                    "id": "k2",
                    "label": "G/L Accounts",
                    "agg": "unique",
                    "source": "gl_account"
                },
                {
                    "id": "k3",
                    "label": "Bank Payment Documents",
                    "agg": "unique",
                    "source": "document"
                },
                {
                    "id": "k4",
                    "label": "Cost Centers",
                    "agg": "unique",
                    "source": "cost_center"
                },
                {
                    "id": "k5",
                    "label": "Profit Centers",
                    "agg": "unique",
                    "source": "profit_center"
                },
                {
                    "id": "k6",
                    "label": "Total Payment Amount",
                    "agg": "total_value",
                    "source": "amount",
                    "format": "currency"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "G/L Account", "source": "gl_account"},
                {"id": "f3", "label": "Cost Center", "source": "cost_center"},
                {"id": "f4", "label": "Profit Center", "source": "profit_center"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "pie",
                    "x": "gl_account",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top 5 G/L Accounts by Payment Amount"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "cost_center",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Cost Centers by Payment Amount"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Bank Payment Trend"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "company",
                    "y": "amount",
                    "agg": "sum",
                    "title": "Company-wise Payment Distribution"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "profit_center",
                    "y": "amount",
                    "agg": "sum",
                    "title": "Top Profit Centers by Payment Amount"
                }
            ]
        }
    ],
    "columns": {
        "company": [
            "Company Code",
            "Company Name",
            "City",
            "Country Key"
        ],
        "document": [
            "Document Number",
            "Fiscal Year",
            "Document Header Text",
            "Line Item Number",
            "Line Item Text"
        ],
        "gl_account": [
            "G/L Account",
            "Account Type",
            "Chart of Accounts",
            "Order Number"
        ],
        "business_partner": [
            "Vendor",
            "Customer"
        ],
        "amount": [
            "Amount in Local Currency",
            "Amount in Document Currency",
            "Currency",
            "Exchange Rate"
        ],
        "date": [
            "Posting Date",
            "Document Date",
            "Entry Date",
            "Entry Time",
            "Changed On",
            "Posting Period"
        ],
        "reference": [
            "Reference Key",
            "Reference Document Number",
            "Clearing Document No.",
            "Assignment Field"
        ],
        "cost_center": [
            "Cost Center"
        ],
        "profit_center": [
            "Profit Center"
        ],
        "user": [
            "User ID",
            "Transaction Code"
        ],
        "status": [
            "Payment Block",
            "Debit/Credit Indicator"
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
        f"data_files/SJPA21_Exception0{exc_id}.csv",
        f"data_files/SJPA21_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
