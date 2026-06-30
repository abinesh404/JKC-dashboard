# Finance/Spend_Analysis/FJSP19.py — Spend analysis_Overall
# -----------------------------------------------------
# AXIS ACCESS:
#   Pie    -> X: Vendor Name              | Y: Sum(Net Order Value)
#   Bar    -> X: Company Code             | Y: Count of rows
#   Line   -> X: Purchasing Doc Date (Mo.)| Y: Sum(Net Order Value)
#   Donut  -> X: Purchasing Doc Type      | Y: Count of rows
#   Column -> X: Purchasing Organization  | Y: Sum(Net Order Value)
# -----------------------------------------------------

import pandas as pd
import os
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJSP19",
    "name": "Spend analysis_Overall",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")},
        {"id": "3", "label": "Exception 03", "title": get_exception_title("Exception 03")}
    ],
    "columns": {
        "amount":   ["Net Order Value in PO Currency", "Net Price in Purchasing Document", "Amount in Local Currency", "Amount"],
        "vendor":   ["Vendor Name", "Vendor Account Number", "Name 1"],
        "date":     ["Purchasing Document Date", "Date on Which Record Was Created", "Posting Date"],
        "gl":       ["Purchasing Organization", "Purchasing Group"],
        "company":  ["Company Code", "Name of Company"],
        "document": ["Purchasing Document Number", "Purchase Requisition Number"],
        "doctype":  ["Purchasing Document Type", "Purchasing Document Category", "Control indicator for purchasing document type"]
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
        {"id": "c2", "type": "bar", "x": "company", "agg": "count", "top_n": 10, "horizontal": True, "title": get_chart_title("Company", "Count", top_n=10)},
        {"id": "c3", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": get_chart_title("Month", "Amount")},
        {"id": "c4", "type": "doughnut", "x": "gl", "agg": "count", "title": get_chart_title("Purchasing Org")},
        {"id": "c5", "type": "bar", "x": "gl", "y": "amount", "agg": "sum", "top_n": 10, "title": get_chart_title("Purchasing Org", "Amount", top_n=10)}
    ]
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Spend_Analysis"}

def get_data(exc_id):
    paths = [
        f"data_files/FJSP19_Exception0{exc_id}.csv",
        f"data_files/FJSP19_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
