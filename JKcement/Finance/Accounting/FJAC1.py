# Finance/Accounting/FJAC1.py — Direct Expense Payment
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------
# AXIS ACCESS:
#   Pie    -> X: Vendor Name              | Y: Sum(Amount in Local Currency)
#   Bar    -> X: Company Code             | Y: Count of rows
#   Line   -> X: Posting Date (Monthly)   | Y: Sum(Amount in Local Currency)
#   Donut  -> X: Document Type            | Y: Count of rows
#   Column -> X: General Ledger Account   | Y: Sum(Amount in Local Currency)
# -----------------------------------------------------

import pandas as pd
import os
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC1",
    "name": "Direct Expense Payment",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")},
        {"id": "3", "label": "Exception 03", "title": get_exception_title("Exception 03")}
    ],
    "columns": {
        "amount":   ["Amount in Local Currency", "Amount in Document Currency", "Amount"],
        "vendor":   ["Vendor Name", "Name 1", "Vendor Number", "Vendor Code"],
        "date":     ["Posting Date in the Document", "Posting Date", "Document Date"],
        "gl":       ["General Ledger Account", "GL Account", "G/L Account"],
        "company":  ["Company Code", "Company Name", "Name of Company Code or Company"],
        "document": ["Accounting Document Number", "Document Number"],
        "doctype":  ["Document Type", "Posting Key", "Posting Key Name", "Dr/Cr Indicator"]
    },
    "cards": [
        {"id": "k1", "label": "Companies", "agg": "unique", "source": "company"},
        {"id": "k2", "label": "Vendors", "agg": "unique", "source": "vendor"},
        {"id": "k3", "label": "Documents", "agg": "unique", "source": "document"},
        {"id": "k4", "label": "Total Value", "agg": "total_value", "source": "amount", "format": "currency"},
        {"id": "k5", "label": "GL Accounts", "agg": "unique", "source": "gl"},
        {"id": "k6", "label": "Issue Count", "agg": "row_count"}
    ],
    "filters": [
        {"id": "f1", "label": "Companies", "source": "company"},
        {"id": "f2", "label": "Vendors", "source": "vendor"},
        {"id": "f3", "label": "GL Accounts", "source": "gl"}
    ],
    "charts": [
        {"id": "c1", "type": "pie", "x": "vendor", "y": "amount", "agg": "sum", "top_n": 5, "title": get_chart_title("Vendor", "Amount", top_n=5)},
        {"id": "c2", "type": "bar", "x": "company", "agg": "count", "top_n": 10, "horizontal": True, "title": get_chart_title("Company", "Transaction Count", top_n=10)},
        {"id": "c3", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": get_chart_title("Month", "Amount")},
        {"id": "c4", "type": "doughnut", "x": "gl", "agg": "count", "title": get_chart_title("GL Account")},
        {"id": "c5", "type": "bar", "x": "gl", "y": "amount", "agg": "sum", "top_n": 10, "title": get_chart_title("GL Account", "Amount", top_n=10)}
    ]
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    paths = [
        rf"D:\off\JKC Dashboard\output\FJAC1_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None