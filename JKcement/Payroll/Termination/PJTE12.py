# Payroll/Termination/PJTE12.py - Relieved Employee with SAP Access
# INSIGHT CONFIG

import pandas as pd
import os
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "PJTE12",
    "name": "Relieved Employee with SAP Access",
    "active_exceptions": [{"id": "1", "label": "All Exceptions", "title": get_exception_title("Exception 01")}],
    "columns": {
        "exception_type": ["Exception Type"],
        "employee": ["Employee Number","Employee Name","Personnel Number"],
        "date": ["Termination Date","Last Working Day","Relieving Date"],
        "amount": ["Balance Amount","Debit Balance","Outstanding Amount"],
        "company": ["Company Code","Company Name","Personnel Area"],
        "detail": ["Status","SAP Access","Department"]
    },
                    "cards": [{'id': 'k1', 'label': 'Active SAP Accounts', 'agg': 'total_rows'}, {'id': 'k2', 'label': 'Relieved Users', 'agg': 'unique', 'source': 'employee'}, {'id': 'k3', 'label': 'Impacted Companies', 'agg': 'unique', 'source': 'company'}, {'id': 'k4', 'label': 'Impacted Cost Centers', 'agg': 'unique', 'source': 'detail'}],
    "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
        {"id": "f1", "label": "Companies", "source": "company"},
        {"id": "f2", "label": "Employees", "source": "employee"},
        {"id": "f3", "label": "Details", "source": "detail"}
    ],
    "charts": [{'id': 'c1', 'type': 'bar', 'x': 'detail', 'agg': 'count', 'title': 'ACTIVE SAP ACCOUNTS BY DEPARTMENT/DETAIL'}, {'id': 'c2', 'type': 'pie', 'x': 'employee', 'agg': 'count', 'top_n': 5, 'title': 'TOP 5 ACTIVE SAP ACCESS ACCOUNTS'}, {'id': 'c3', 'type': 'line', 'x': 'date', 'agg': 'count', 'time_group': 'month', 'title': 'ACCESS REVOCATION GAP TIMELINE'}]
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Termination"}

def get_data(exc_id):
    insight_id = CONFIG["id"]
    merged_df = pd.DataFrame()
    for i in range(1, 10):
        path1 = f"data_files/{insight_id}_Exception0{i}.csv"
        path2 = f"data_files/{insight_id}_Exception{i}.csv"
        path = next((p for p in [path1, path2] if os.path.exists(p)), None)
        if path:
            df = pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
            df['Exception Type'] = f"Exception {i}"
            merged_df = pd.concat([merged_df, df], ignore_index=True)
    if merged_df.empty:
        return None
    return merged_df