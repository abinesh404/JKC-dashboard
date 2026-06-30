# Supplier/procurement/SJPR53.py — Same Transaction & Group PO and Non-PO Invoices Raised
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR53",
    "name": "Same Transaction & Group PO and Non-PO Invoices Raised",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("G/L Accounts for which PO and Non-PO Invoices have been Raised"),
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
                    "label": "G/L Accounts",
                    "agg": "unique",
                    "source": "gl"
                },
                {
                    "id": "k6",
                    "label": "Total Transaction Value",
                    "agg": "total_value",
                    "source": "amount",
                    "format": "currency"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "Purchasing Organization", "source": "purch_org"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "pie",
                    "x": "gl_group",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 5,
                    "title": "Top 5 G/L Account Groups by Transaction Value"
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
                    "x": "posting_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Exception Trend"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "company_desc",
                    "y": "amount",
                    "agg": "sum",
                    "title": "Company-wise Transaction Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "gl_desc",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Top G/L Accounts by Transaction Value"
                }
            ]
        }
    ],
    "columns": {
        "company": [
            "Company Code",
            "Company Description",
            "Company City"
        ],
        "company_desc": [
            "Company Description"
        ],
        "plant": [
            "Plant Code",
            "Plant Name"
        ],
        "vendor": [
            "Vendor Code"
        ],
        "invoice": [
            "Accounting document Number",
            "Fiscal Year",
            "Document Type"
        ],
        "po": [
            "Purchasing Organization",
            "Purchasing Document Number",
            "Item Number of Purchasing Document"
        ],
        "purch_org": [
            "Purchasing Organization"
        ],
        "gl": [
            "General Ledger Account",
            "G/L Account Number",
            "G/L Account Group",
            "G/L Account Long Text",
            "G/L Acct Long Text",
            "G/L Long Text",
            "GLACCOUNT_TYPE",
            "GLACCOUNT_SUBTYPE",
            "Derived_GL",
            "Cost Element"
        ],
        "gl_group": [
            "G/L Account Group"
        ],
        "gl_desc": [
            "G/L Account Long Text",
            "G/L Acct Long Text",
            "G/L Long Text"
        ],
        "amount": [
            "Amount in Local Currency"
        ],
        "date": [
            "Document Date in Document",
            "Posting Date in the Document",
            "Clearing Date"
        ],
        "posting_date": [
            "Posting Date in the Document"
        ],
        "user": [
            "User Name",
            "Name of Person who Created the Object"
        ],
        "item_details": [
            "Item Text",
            "Posting Key",
            "Number of Line Item Within Accounting Document",
            "Account Type",
            "DR/CR Indicator"
        ],
        "search_key": [
            "Search Term for Using Matchcode"
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
        f"data_files/SJPR53_Exception0{exc_id}.csv",
        f"data_files/SJPR53_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
