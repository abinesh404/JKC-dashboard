# ITcontrols/SAP/IJSA4.py
import pandas as pd
import os
import datetime

CONFIG = {
    "id": "IJSA4",
    "name": "Client Set to Modifiable",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "Client Set to Modifiable",
            "cards": [
                {"id": "k1", "label": "Modifiable Clients", "agg": "unique", "source": "client_number"},
                {"id": "k2", "label": "Production Clients Impacted", "agg": "unique", "source": "prod_client_number"},
                {"id": "k3", "label": "Users with Change Access", "agg": "unique", "source": "user_name"},
                {"id": "k4", "label": "Client Changes Made", "agg": "unique", "source": "change_id"},
                {"id": "k5", "label": "Last Modified Clients", "agg": "unique", "source": "last_mod_client"},
                {"id": "k6", "label": "High Risk Clients", "agg": "unique", "source": "high_risk_client"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "Client Number", "source": "client_number", "all_label": "All Clients"},
                {"id": "f2", "label": "Client Role", "source": "client_role", "all_label": "All Roles"},
                {"id": "f3", "label": "User Name", "source": "user_name", "all_label": "All Users"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "doughnut",
                    "x": "client_role",
                    "agg": "count",
                    "legend": True,
                    "title": "Client Role Distribution"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "user_name",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Users Modifying Clients"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "client_name",
                    "agg": "count",
                    "title": "Client-wise Modification Analysis"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "last_changed_on",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Client Modification Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "client_number",
                    "agg": "count",
                    "title": "Client Number Distribution"
                }
            ]
        }
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "client_number": ["Client Number"],
        "client_role": ["Client Role"],
        "user_name": ["User Name"],
        "client_name": ["Client Name"],
        "last_changed_on": ["Last Changed On"],
        "date": ["Last Changed On"],
        # KPI helpers
        "prod_client_number": ["Prod Client Number"],
        "change_id": ["Change ID"],
        "last_mod_client": ["Last Mod Client"],
        "high_risk_client": ["High Risk Client"]
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
    import re
    m = re.search(r'([A-Za-z]+)(\d+)', insight_id)
    padded_id = f"{m.group(1)}0{m.group(2)}" if m and len(m.group(2)) == 1 else insight_id
    merged_df = pd.DataFrame()
    file_found = False
    for i in range(1, 10):
        paths = [
            f"data_files/{insight_id}_Exception0{i}.csv",
            f"data_files/{insight_id}_Exception{i}.csv",
            f"data_files/{padded_id}_Exception0{i}.csv",
            f"data_files/{padded_id}_Exception{i}.csv"
        ]
        path = next((p for p in paths if os.path.exists(p)), None)
        if path:
            file_found = True
            df = pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
            df['Exception Type'] = f"Exception {i}"
            merged_df = pd.concat([merged_df, df], ignore_index=True)
    if not file_found:
        return None
    return merged_df