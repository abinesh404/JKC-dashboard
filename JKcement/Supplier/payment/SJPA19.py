# Supplier/payment/SJPA19.py
import pandas as pd
import os
from .template import get_exception_title, get_chart_title

CONFIG = {
    "id": "SJPA19",
    "name": "Payee Name in Cheque Payments is Different from Vendor Name or Alternate Payee",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Payee Name Does Not Match Vendor Name or Alternate Payee"),
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
                    "label": "Customers",
                    "agg": "unique",
                    "source": "customer"
                },
                {
                    "id": "k4",
                    "label": "Cheque Payments",
                    "agg": "total_rows"
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
                    "label": "Name Mismatch Exceptions",
                    "agg": "total_rows"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "Customer", "source": "customer"},
                {"id": "f4", "label": "Creation User", "source": "user"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "pie",
                    "x": "vendor",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top 5 Vendors with Payee Name Mismatches"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "company",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Companies by Mismatch Amount"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Cheque Payment Exception Trend"
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
                    "x": "user",
                    "agg": "count",
                    "title": "Top Creation Users by Exception Count"
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
        "vendor": [
            "Vendor Code",
            "Vendor Name1",
            "Vendor Name2"
        ],
        "customer": [
            "Customer Code",
            "Customer Name1",
            "Customer Name2"
        ],
        "payee": [
            "Name of the Payee1",
            "Name of the Payee2",
            "Account Number of Alternate Payee"
        ],
        "cheque_details": [
            "Check Number",
            "Check Number From",
            "Check Type",
            "Replacement Check Number"
        ],
        "amount": [
            "Amount",
            "Currency"
        ],
        "date": [
            "Print Date",
            "Print Time",
            "Probable Payment Date (Cash Discount 1 Due)"
        ],
        "user": [
            "Print User",
            "Creation User"
        ],
        "address": [
            "City",
            "Street"
        ],
        "master_data_status": [
            "Central Deletion Flag",
            "Central Posting Block",
            "Centrally Imposed Purchasing Block",
            "Payment Block",
            "Central Deletion Block for Master Record"
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
        f"data_files/SJPA19_Exception0{exc_id}.csv",
        f"data_files/SJPA19_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
