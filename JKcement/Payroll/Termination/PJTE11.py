# Payroll/Termination/PJTE11.py - Relieved Employee with open debit balance
# INSIGHT CONFIG

import pandas as pd
import os
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "PJTE11",
    "name": "Relieved Employee with open debit balance",
    "active_exceptions": [{"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}],
    "columns": {
        "employee": ["Employee Number","Employee Name","Personnel Number"],
        "date": ["Termination Date","Last Working Day","Relieving Date"],
        "amount": ["Balance Amount","Debit Balance","Outstanding Amount"],
        "company": ["Company Code","Company Name","Personnel Area"],
        "detail": ["Status","SAP Access","Department"]
    },
                    "cards": [
        {"id": "k1", "label": "Companies", "agg": "unique", "source": "company"},
        {"id": "k2", "label": "Employees", "agg": "unique", "source": "employee"},
        {"id": "k3", "label": "Records", "agg": "total_rows"},
        {"id": "k4", "label": "Total Value", "agg": "total_value", "source": "amount", "format": "currency"},
        {"id": "k5", "label": "Details", "agg": "unique", "source": "detail"},
        {"id": "k6", "label": "Issue Count", "agg": "row_count"}
    ],
    "filters": [
        {"id": "f1", "label": "Companies", "source": "company"},
        {"id": "f2", "label": "Employees", "source": "employee"},
        {"id": "f3", "label": "Details", "source": "detail"}
    ],
    "charts": [
        {"id": "c1", "type": "pie", "x": "employee", "y": "amount", "agg": "sum", "top_n": 5, "title": get_chart_title("Employee", "Amount", top_n=5)},
        {"id": "c2", "type": "bar", "x": "company", "agg": "count", "top_n": 10, "horizontal": True, "title": get_chart_title("Company", "Count", top_n=10)},
        {"id": "c3", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": get_chart_title("Month", "Amount")},
        {"id": "c4", "type": "doughnut", "x": "detail", "agg": "count", "title": get_chart_title("Detail")},
        {"id": "c5", "type": "bar", "x": "detail", "y": "amount", "agg": "sum", "top_n": 10, "title": get_chart_title("Detail", "Amount", top_n=10)}
    ]
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Termination"}

def get_data(exc_id):
    paths = [
        rf"D:\off\JKC Dashboard\output\PJTE11_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
