# Payroll/SoD/PJSO1.py - SoD Check_Category1 - LFA1 and EKKO
# INSIGHT CONFIG

import pandas as pd
import os
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "PJSO1",
    "name": "SoD Check_Category1 - LFA1 and EKKO",
    "active_exceptions": [{"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}],
    "columns": {
        "user": ["User ID","User Name","Employee Name"],
        "role": ["Role","Authorization","Transaction Code"],
        "date": ["Date","Valid From","Valid To"],
        "company": ["Company Code","Company Name"],
        "detail": ["Conflict Type","Table 1","Table 2","Risk Level"]
    },
                    "cards": [{'id': 'k1', 'label': 'Violator Count', 'agg': 'unique', 'source': 'user'}, {'id': 'k2', 'label': 'SoD Violations', 'agg': 'total_rows'}, {'id': 'k3', 'label': 'Impacted Companies', 'agg': 'unique', 'source': 'company'}, {'id': 'k4', 'label': 'Active Roles In Conflict', 'agg': 'unique', 'source': 'role'}],
    "filters": [
        {"id": "f1", "label": "Companies", "source": "company"},
        {"id": "f2", "label": "Users", "source": "user"},
        {"id": "f3", "label": "Roles", "source": "role"}
    ],
    "charts": [{'id': 'c1', 'type': 'bar', 'x': 'company', 'agg': 'count', 'title': 'SOD VIOLATIONS BY COMPANY'}, {'id': 'c2', 'type': 'pie', 'x': 'user', 'agg': 'count', 'top_n': 5, 'title': 'TOP 5 USER SOD VIOLATORS'}, {'id': 'c3', 'type': 'line', 'x': 'date', 'agg': 'count', 'time_group': 'month', 'title': 'SOD VIOLATIONS TREND'}]
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "SoD"}

def get_data(exc_id):
    paths = [
        rf"data_files/PJSO1_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
