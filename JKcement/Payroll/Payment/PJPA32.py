# Payroll/Payment/PJPA32.py - Weekend or Holiday Travel
# INSIGHT CONFIG

import pandas as pd
import os
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "PJPA32",
    "name": "Weekend or Holiday Travel",
    "active_exceptions": [{"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}],
    "columns": {
        "employee": ["Employee Number","Employee Name","Personnel Number"],
        "date": ["Submit Date","Approval Date","Travel Start Date","Travel End Date","Report Date"],
        "amount": ["Claim Amount","Approved Amount","Reimbursement Amount","Amount"],
        "company": ["Company Code","Company Name","Personnel Area"],
        "report": ["Report ID","Trip Number","Expense Type","Travel Mode"],
        "department": ["Department","Cost Center","Manager Name"]
    },
            "cards": [{'id': 'k1', 'label': 'Weekend / Holiday Spend', 'agg': 'total_value', 'source': 'amount', 'format': 'currency'}, {'id': 'k2', 'label': 'Weekend Claimants', 'agg': 'unique', 'source': 'employee'}, {'id': 'k3', 'label': 'Weekend Claims Count', 'agg': 'total_rows'}, {'id': 'k4', 'label': 'Affected Cost Centers', 'agg': 'unique', 'source': 'department'}],
    "filters": [
        {"id": "f1", "label": "Companies", "source": "company"},
        {"id": "f2", "label": "Employees", "source": "employee"},
        {"id": "f3", "label": "Departments", "source": "department"}
    ],
    "charts": [{'id': 'c1', 'type': 'bar', 'x': 'department', 'y': 'amount', 'agg': 'sum', 'title': 'WEEKEND SPEND BY DEPARTMENT'}, {'id': 'c2', 'type': 'doughnut', 'x': 'company', 'agg': 'count', 'title': 'WEEKEND TRAVEL BY COMPANY AREA'}, {'id': 'c3', 'type': 'line', 'x': 'date', 'y': 'amount', 'agg': 'sum', 'time_group': 'month', 'title': 'WEEKEND SPEND TREND'}]
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Payment"}

def get_data(exc_id):
    paths = [
        rf"data_files/PJPA32_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
