# Payroll/Payment/PJPA36.py - EDA on Employee Reimbursement Claims submitted
# INSIGHT CONFIG

import pandas as pd
import os
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "PJPA36",
    "name": "EDA on Employee Reimbursement Claims submitted",
    "active_exceptions": [{"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}],
    "columns": {
        "employee": ["Employee Number","Employee Name","Personnel Number"],
        "date": ["Submit Date","Approval Date","Travel Start Date","Travel End Date","Report Date"],
        "amount": ["Claim Amount","Approved Amount","Reimbursement Amount","Amount"],
        "company": ["Company Code","Company Name","Personnel Area"],
        "report": ["Report ID","Trip Number","Expense Type","Travel Mode"],
        "department": ["Department","Cost Center","Manager Name"]
    },
            "cards": [{'id': 'k1', 'label': 'Total Reimbursement Spend', 'agg': 'total_value', 'source': 'amount', 'format': 'currency'}, {'id': 'k2', 'label': 'Active Claimants', 'agg': 'unique', 'source': 'employee'}, {'id': 'k3', 'label': 'Total Claims Count', 'agg': 'total_rows'}, {'id': 'k4', 'label': 'Departments Count', 'agg': 'unique', 'source': 'department'}],
    "filters": [
        {"id": "f1", "label": "Companies", "source": "company"},
        {"id": "f2", "label": "Employees", "source": "employee"},
        {"id": "f3", "label": "Departments", "source": "department"}
    ],
    "charts": [{'id': 'c1', 'type': 'bar', 'x': 'department', 'y': 'amount', 'agg': 'sum', 'title': 'REIMBURSEMENT SPEND BY DEPARTMENT'}, {'id': 'c2', 'type': 'pie', 'x': 'employee', 'y': 'amount', 'agg': 'sum', 'top_n': 5, 'title': 'TOP 5 CLAIMANTS'}, {'id': 'c3', 'type': 'line', 'x': 'date', 'y': 'amount', 'agg': 'sum', 'time_group': 'month', 'title': 'REIMBURSEMENT SPEND TREND'}]
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Payment"}

def get_data(exc_id):
    paths = [
        rf"data_files/PJPA36_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
