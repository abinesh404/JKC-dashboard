# Supplier/payment/SJPA23.py
import pandas as pd
import os
from .template import get_exception_title, get_chart_title

CONFIG = {
    "id": "SJPA23",
    "name": "Delayed & Early Payment to Vendors from Due Date",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Delayed Payment to Vendors from Due Date"),
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
                    "label": "Average Delay (Days)",
                    "agg": "avg",
                    "source": "delay"
                },
                {
                    "id": "k6",
                    "label": "Delayed Payments",
                    "agg": "total_rows"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "Payment Method", "source": "payment_method"}
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
                    "title": "Top Companies by Delayed Payments"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "clearing_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Delayed Payment Trend"
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
                    "x": "age_bucket",
                    "agg": "count",
                    "title": "Age Bucket Distribution"
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": get_exception_title("Early Payment to Vendors from Due Date"),
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
                    "label": "Average Early Days",
                    "agg": "avg",
                    "source": "delay"
                },
                {
                    "id": "k6",
                    "label": "Early Payments",
                    "agg": "total_rows"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "Payment Method", "source": "payment_method"}
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
                    "title": "Top Companies by Early Payments"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "clearing_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Early Payment Trend"
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
            "Company Name",
            "Company City"
        ],
        "company_name": [
            "Company Name"
        ],
        "vendor": [
            "Vendor Code",
            "Vendor Name1",
            "Vendor Name2",
            "Vendor City",
            "Vendor District",
            "Vendor account group",
            "Vendor Account Group Description"
        ],
        "amount": [
            "Amount in Local Currency",
            "Amount in Document Currency",
            "Currency"
        ],
        "document": [
            "Accounting Document Number",
            "Document Number of the Clearing Document",
            "Document Type",
            "Fiscal Yaer",
            "Number of Line Item Within Accounting Document",
            "Clearing Item"
        ],
        "date": [
            "Clearing Date",
            "Document Date in Document",
            "Posting Date",
            "Due Date",
            "Clearing Entry Date",
            "Baseline Date for Due Date Calculation"
        ],
        "clearing_date": [
            "Clearing Date"
        ],
        "delay": [
            "Difference Clearing Date and Due Date"
        ],
        "payment": [
            "Payment Method",
            "Payment Block Key",
            "List of the Payment Methods to be Considered"
        ],
        "payment_method": [
            "Payment Method"
        ],
        "business": [
            "Type of Business",
            "Type of Industry"
        ],
        "age_bucket": [
            "Age Bucket"
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
        f"data_files/SJPA23_Exception0{exc_id}.csv",
        f"data_files/SJPA23_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
