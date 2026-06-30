# Supplier/payment/SJPA52.py
import pandas as pd
import os
from .template import get_exception_title, get_chart_title

CONFIG = {
    "id": "SJPA52",
    "name": "Non Routine Transactions",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Payment to One-Time Vendors"),
            "cards": [
                {
                    "id": "k1",
                    "label": "Companies",
                    "agg": "unique",
                    "source": "company"
                },
                {
                    "id": "k2",
                    "label": "One-Time Vendors",
                    "agg": "unique",
                    "source": "vendor"
                },
                {
                    "id": "k3",
                    "label": "Payment Documents",
                    "agg": "unique",
                    "source": "document"
                },
                {
                    "id": "k4",
                    "label": "Total Payment Amount",
                    "agg": "total_value",
                    "source": "amount",
                    "format": "currency"
                },
                {
                    "id": "k5",
                    "label": "Plants",
                    "agg": "unique",
                    "source": "plant"
                },
                {
                    "id": "k6",
                    "label": "Duplicate Payments",
                    "agg": "sum",
                    "source": "duplicate_payment"
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
                    "title": "Top Companies by Payments"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "clearing_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Payment Trend"
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
                    "x": "plant",
                    "agg": "count",
                    "title": "Plant-wise Payments"
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": get_exception_title("Manual / Irregular Payment"),
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
                    "label": "Manual Payments",
                    "agg": "total_rows"
                },
                {
                    "id": "k4",
                    "label": "Total Payment Amount",
                    "agg": "total_value",
                    "source": "amount",
                    "format": "currency"
                },
                {
                    "id": "k5",
                    "label": "Average Delay (Days)",
                    "agg": "avg",
                    "source": "delay"
                },
                {
                    "id": "k6",
                    "label": "Exception Count",
                    "agg": "total_rows"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "Transaction Code", "source": "transaction_code"}
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
                    "title": "Top Companies by Manual Payments"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "clearing_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Exception Trend"
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
                    "x": "transaction_code",
                    "agg": "count",
                    "title": "Transaction Code Distribution"
                }
            ]
        },
        {
            "id": "3",
            "label": "Exception 03",
            "title": get_exception_title("Financial / Value Deviation"),
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
                    "label": "High Value Payments",
                    "agg": "sum",
                    "source": "high_payment"
                },
                {
                    "id": "k4",
                    "label": "Duplicate Payments",
                    "agg": "sum",
                    "source": "duplicate_payment"
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
                    "label": "Average Payment Amount",
                    "agg": "avg",
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
                    "title": "Top Companies by High-Value Payments"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "clearing_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly High-Value Payment Trend"
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
                    "x": "duplicate_payment",
                    "agg": "count",
                    "title": "Duplicate Payment Analysis"
                }
            ]
        }
    ],
    "columns": {
        "company": [
            "Company Code"
        ],
        "vendor": [
            "Account Number vendor",
            "Name1",
            "Vendor account group"
        ],
        "plant": [
            "Plant"
        ],
        "amount": [
            "Amount in Local Currency",
            "Amount in document currency"
        ],
        "document": [
            "Accounting Document Number",
            "Purchasing Document Number"
        ],
        "date": [
            "Clearing Date",
            "Document Date in Document",
            "Posting Date in the Document",
            "Day  Acc. Doc. Entered"
        ],
        "clearing_date": [
            "Clearing Date"
        ],
        "account": [
            "General Ledger Account",
            "G/L Account Number"
        ],
        "duplicate_payment": [
            "Duplicate-flag",
            "Duplicate_Flag_Num"
        ],
        "high_payment": [
            "High_Payment_Flag"
        ],
        "delay": [
            "Diff_Days"
        ],
        "reference": [
            "Reference Key"
        ],
        "transaction_code": [
            "Transaction Code"
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
        f"data_files/SJPA52_Exception0{exc_id}.csv",
        f"data_files/SJPA52_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
