# ITcontrols/SAP/IJSA3.py
import pandas as pd
import os
import datetime

CONFIG = {
    "id": "IJSA3",
    "name": "Critical T-Code Access",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "Users Having Access to One or More Critical Transaction Codes Through Assigned Roles",
            "cards": [
                {"id": "k1", "label": "Users with Critical Access", "agg": "unique", "source": "user_name"},
                {"id": "k2", "label": "Critical Transaction Codes", "agg": "unique", "source": "transaction_code"},
                {"id": "k3", "label": "Roles Assigned", "agg": "unique", "source": "role_name"},
                {"id": "k4", "label": "Active Users", "agg": "unique", "source": "active_user_name"},
                {"id": "k5", "label": "Critical Access Roles", "agg": "unique", "source": "critical_role_name"},
                {"id": "k6", "label": "Locked Users with Critical Access", "agg": "unique", "source": "locked_user_name"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "User Name", "source": "user_name", "all_label": "All Users"},
                {"id": "f2", "label": "Transaction Code", "source": "transaction_code", "all_label": "All T-Codes"},
                {"id": "f3", "label": "Role Name Assigned to User", "source": "role_name", "all_label": "All Roles"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "transaction_code",
                    "agg": "count",
                    "title": "Critical Access by Transaction Code"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "role_name",
                    "agg": "count",
                    "horizontal": True,
                    "top_n": 10,
                    "title": "Roles Granting Critical Access"
                },
                {
                    "id": "c3",
                    "type": "doughnut",
                    "x": "user_type",
                    "agg": "count",
                    "legend": True,
                    "title": "User Type Distribution"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "role_change_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Role Assignment Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "user_lock_status",
                    "agg": "count",
                    "title": "User Lock Status Analysis"
                }
            ]
        }
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "user_name": ["User Name"],
        "transaction_code": ["Transaction Code"],
        "role_name": ["Role Name Assigned to User"],
        "user_type": ["User Type"],
        "role_change_date": ["Role Change Date"],
        "user_lock_status": ["User Lock Status"],
        "date": ["Role Change Date"],
        # KPI helpers
        "active_user_name": ["Active User Name"],
        "locked_user_name": ["Locked User Name"],
        "critical_role_name": ["Critical Role Name"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "SAP"
    }

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