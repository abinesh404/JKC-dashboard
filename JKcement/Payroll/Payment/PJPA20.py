# Payroll/Payment/PJPA20.py - Odd Time Submission (8PM-8AM)
# INSIGHT CONFIG

import pandas as pd
import os
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "PJPA20",
    "name": "Odd Time Submission (8PM-8AM)",
    "active_exceptions": [{"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}],
    "columns": {
        "employee": ["Employee Number","Employee Name","Personnel Number"],
        "date": ["Submit Date","Approval Date","Travel Start Date","Travel End Date","Report Date"],
        "amount": ["Claim Amount","Approved Amount","Reimbursement Amount","Amount"],
        "company": ["Company Code","Company Name","Personnel Area"],
        "report": ["Report ID","Trip Number","Expense Type","Travel Mode"],
        "department": ["Department","Cost Center","Manager Name"]
    },
            "cards": [{'id': 'k1', 'label': 'Out-of-Hours Claim Vol', 'agg': 'total_value', 'source': 'amount', 'format': 'currency'}, {'id': 'k2', 'label': 'Off-Hour Submitters', 'agg': 'unique', 'source': 'employee'}, {'id': 'k3', 'label': 'Off-Hour Submissions', 'agg': 'total_rows'}, {'id': 'k4', 'label': 'Off-Hour Approvers', 'agg': 'unique', 'source': 'department'}],
    "filters": [
        {"id": "f1", "label": "Companies", "source": "company"},
        {"id": "f2", "label": "Employees", "source": "employee"},
        {"id": "f3", "label": "Departments", "source": "department"}
    ],
    "charts": [{'id': 'c1', 'type': 'bar', 'x': 'department', 'y': 'amount', 'agg': 'sum', 'title': 'OFF-HOUR CLAIM VALUE BY DEPARTMENT'}, {'id': 'c2', 'type': 'pie', 'x': 'employee', 'y': 'amount', 'agg': 'sum', 'top_n': 5, 'title': 'TOP 5 OFF-HOUR SUBMITTERS'}, {'id': 'c3', 'type': 'line', 'x': 'date', 'y': 'amount', 'agg': 'sum', 'time_group': 'month', 'title': 'SUBMISSION TIMELINE'}]
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Payment"}

def get_data(exc_id):
    paths = [
        rf"data_files/PJPA20_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
