# Supplier/payment/SJPA7.py
import pandas as pd
import os
from .template import get_exception_title, get_chart_title

CONFIG = {
    "id": "SJPA7",
    "name": "Penalty Payment in Case of Delay in MSME Vendor Payment",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Penalty Payment in Case of Delay in MSME Vendor Payment"),
            "cards": [
                {
                    "id": "k1",
                    "label": "Companies",
                    "agg": "unique",
                    "source": "company"
                },
                {
                    "id": "k2",
                    "label": "MSME Vendors",
                    "agg": "unique",
                    "source": "vendor"
                },
                {
                    "id": "k3",
                    "label": "Accounting Documents",
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
                    "label": "Total Interest on Delayed Payment",
                    "agg": "sum",
                    "source": "interest",
                    "format": "currency"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "MSME Category", "source": "msme_category"},
                {"id": "f4", "label": "Age Bucket", "source": "age_bucket"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "pie",
                    "x": "vendor",
                    "y": "interest",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top 5 MSME Vendors by Interest Amount"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "company",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Companies by Delayed Payment Amount"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Delayed Payment Trend"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "company",
                    "y": "amount",
                    "agg": "sum",
                    "title": "Company-wise Delayed Payment Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "age_bucket",
                    "y": "amount",
                    "agg": "sum",
                    "title": "Age Bucket-wise Delayed Payments"
                }
            ]
        }
    ],
    "columns": {
        "company": [
            "COMPANY_CODE",
            "COMPANY_NAME",
            "COMPANY_CITY"
        ],
        "vendor": [
            "VENDOR_CODE",
            "VENDOR_NAME",
            "CITY",
            "DISTRICT",
            "UDYAM_NUMBER"
        ],
        "msme_category": [
            "MSME_(MICRO,SMALL,MEDIUM)_OR_NOT"
        ],
        "document": [
            "DOCUMENT_NUMBER",
            "DOCUMENT_TYPE",
            "FISCAL_YEAR",
            "DOCUMENT_NUMBER_OF_CLEARING_DOCUMENT"
        ],
        "amount": [
            "AMOUNT"
        ],
        "interest": [
            "INTEREST_ON_DELAYED_PAYMENT_TO_MSME_(@3 TIMES THE BANK RATE)"
        ],
        "date": [
            "CLEARING_DATE",
            "DOCUMENT_DATE",
            "POSTING_DATE_IN_DOCUMENT",
            "BASELINE_DATE",
            "DUE_DATE_AS_PER_MSME_ACT",
            "CLEARING_ENTRY_DATE"
        ],
        "delay": [
            "DIFFERENCE_IN_BASELINE_DATES_AND_PAYMENT_DATE_(DAYS)"
        ],
        "age_bucket": [
            "AGE_BUCKET"
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
        f"data_files/SJPA7_Exception0{exc_id}.csv",
        f"data_files/SJPA7_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
