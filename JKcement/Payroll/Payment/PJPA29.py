# Payroll/Payment/PJPA29.py - New Joiner Early Claims
# INSIGHT CONFIG

import pandas as pd
import os
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "PJPA29",
    "name": "New Joiner Early Claims",
    "active_exceptions": [{"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}],
    "columns": {
        "employee": ["Employee Number","Employee Name","Personnel Number"],
        "date": ["Submit Date","Approval Date","Travel Start Date","Travel End Date","Report Date"],
        "amount": ["Claim Amount","Approved Amount","Reimbursement Amount","Amount"],
        "company": ["Company Code","Company Name","Personnel Area"],
        "report": ["Report ID","Trip Number","Expense Type","Travel Mode"],
        "department": ["Department","Cost Center","Manager Name"]
    },
            "cards": [
        {"id": "k1", "label": "Companies", "agg": "unique", "source": "company"},
        {"id": "k2", "label": "Employees", "agg": "unique", "source": "employee"},
        {"id": "k3", "label": "Records", "agg": "total_rows"},
        {"id": "k4", "label": "Total Value", "agg": "total_value", "source": "amount", "format": "currency"},
        {"id": "k5", "label": "Departments", "agg": "unique", "source": "department"},
        {"id": "k6", "label": "Issue Count", "agg": "row_count"}
    ],
    "filters": [
        {"id": "f1", "label": "Companies", "source": "company"},
        {"id": "f2", "label": "Employees", "source": "employee"},
        {"id": "f3", "label": "Departments", "source": "department"}
    ],
    "charts": [
        {"id": "c1", "type": "pie", "x": "employee", "y": "amount", "agg": "sum", "top_n": 5, "title": get_chart_title("Employee", "Amount", top_n=5)},
        {"id": "c2", "type": "bar", "x": "company", "agg": "count", "top_n": 10, "horizontal": True, "title": get_chart_title("Company", "Count", top_n=10)},
        {"id": "c3", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": get_chart_title("Month", "Amount")},
        {"id": "c4", "type": "doughnut", "x": "department", "agg": "count", "title": get_chart_title("Department")},
        {"id": "c5", "type": "bar", "x": "department", "y": "amount", "agg": "sum", "top_n": 10, "title": get_chart_title("Department", "Amount", top_n=10)}
    ]
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Payment"}

def get_data(exc_id):
    paths = [
        rf"D:\off\JKC Dashboard\output\PJPA29_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
