# Payroll/SoD/PJSO2.py - SoD Check_Category2 - MARA and MSEG
# INSIGHT CONFIG

import pandas as pd
import os
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "PJSO2",
    "name": "SoD Check_Category2 - MARA and MSEG",
    "active_exceptions": [{"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}],
    "columns": {
        "user": ["User ID","User Name","Employee Name"],
        "role": ["Role","Authorization","Transaction Code"],
        "date": ["Date","Valid From","Valid To"],
        "company": ["Company Code","Company Name"],
        "detail": ["Conflict Type","Table 1","Table 2","Risk Level"]
    },
                    "cards": [
        {"id": "k1", "label": "Companies", "agg": "unique", "source": "company"},
        {"id": "k2", "label": "Users", "agg": "unique", "source": "user"},
        {"id": "k3", "label": "Records", "agg": "total_rows"},
        {"id": "k4", "label": "Total Occurrences", "agg": "total_rows"},
        {"id": "k5", "label": "Roles", "agg": "unique", "source": "role"},
        {"id": "k6", "label": "Issue Count", "agg": "row_count"}
    ],
    "filters": [
        {"id": "f1", "label": "Companies", "source": "company"},
        {"id": "f2", "label": "Users", "source": "user"},
        {"id": "f3", "label": "Roles", "source": "role"}
    ],
    "charts": [
        {"id": "c1", "type": "pie", "x": "user", "agg": "count", "top_n": 5, "title": get_chart_title("User", "Count", top_n=5)},
        {"id": "c2", "type": "bar", "x": "company", "agg": "count", "top_n": 10, "horizontal": True, "title": get_chart_title("Company", "Count", top_n=10)},
        {"id": "c3", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": get_chart_title("Month", "Count")},
        {"id": "c4", "type": "doughnut", "x": "role", "agg": "count", "title": get_chart_title("Role")},
        {"id": "c5", "type": "bar", "x": "role", "agg": "count", "top_n": 10, "title": get_chart_title("Role", "Count", top_n=10)}
    ]
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "SoD"}

def get_data(exc_id):
    paths = [
        rf"D:\off\JKC Dashboard\output\PJSO2_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
