# ITcontrols/SAP/IJSA7.py - Configuration of Document Type in SAP
# INSIGHT CONFIG

import pandas as pd
import os
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "IJSA7",
    "name": "Configuration of Document Type in SAP",
    "active_exceptions": [{"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}],
    "columns": {
        "user": ["User Name","User ID","Changed By","Created By"],
        "tcode": ["Transaction Code","TCode","Authorization Object"],
        "date": ["Change Date","Date","Created On","Last Changed On"],
        "company": ["Company Code","Client","Company Name"],
        "detail": ["Change Type","Field Name","Old Value","New Value","Description"]
    },
        "cards": [
        {"id": "k1", "label": "Companies", "agg": "unique", "source": "company"},
        {"id": "k2", "label": "Users", "agg": "unique", "source": "user"},
        {"id": "k3", "label": "Records", "agg": "total_rows"},
        {"id": "k4", "label": "Total Occurrences", "agg": "total_rows"},
        {"id": "k5", "label": "T-Codes", "agg": "unique", "source": "tcode"},
        {"id": "k6", "label": "Issue Count", "agg": "row_count"}
    ],
    "filters": [
        {"id": "f1", "label": "Companies", "source": "company"},
        {"id": "f2", "label": "Users", "source": "user"},
        {"id": "f3", "label": "T-Codes", "source": "tcode"}
    ],
    "charts": [
        {"id": "c1", "type": "pie", "x": "user", "agg": "count", "top_n": 5, "title": get_chart_title("User", top_n=5)},
        {"id": "c2", "type": "bar", "x": "company", "agg": "count", "top_n": 10, "horizontal": True, "title": get_chart_title("Company", "Count", top_n=10)},
        {"id": "c3", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": get_chart_title("Month", "Count")},
        {"id": "c4", "type": "doughnut", "x": "tcode", "agg": "count", "title": get_chart_title("T-Code")},
        {"id": "c5", "type": "bar", "x": "tcode", "agg": "count", "top_n": 10, "title": get_chart_title("T-Code", "Count", top_n=10)}
    ]
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "SAP"}

def get_data(exc_id):
    paths = [
        rf"D:\off\JKC Dashboard\output\IJSA7_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
