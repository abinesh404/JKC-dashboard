# ITcontrols/SAP/IJSA5.py
import pandas as pd
import os

CONFIG = {
    "id": "IJSA5",
    "name": "Direct Changes to SAP",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "Direct Changes to SAP Tables",
            "cards": [
                {"id": "k1", "label": "Direct Table Changes", "agg": "unique", "source": "change_number"},
                {"id": "k2", "label": "Users Performing Changes", "agg": "unique", "source": "user_name"},
                {"id": "k3", "label": "SAP Tables Modified", "agg": "unique", "source": "table_name"},
                {"id": "k4", "label": "Fields Changed", "agg": "unique", "source": "field_name"},
                {"id": "k5", "label": "Clients Impacted", "agg": "unique", "source": "client_number"},
                {"id": "k6", "label": "High Risk Changes", "agg": "unique", "source": "high_risk_change"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "Client Number", "source": "client_number", "all_label": "All Clients"},
                {"id": "f2", "label": "User Name", "source": "user_name", "all_label": "All Users"},
                {"id": "f3", "label": "Table Name", "source": "table_name", "all_label": "All Tables"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "table_name",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Top Modified SAP Tables"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "user_name",
                    "agg": "count",
                    "horizontal": True,
                    "top_n": 10,
                    "title": "User-wise Direct Changes"
                },
                {
                    "id": "c3",
                    "type": "doughnut",
                    "x": "object_class",
                    "agg": "count",
                    "legend": True,
                    "title": "Object Class Distribution"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "date_of_change",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Direct Change Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "field_name",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Frequently Changed Fields"
                }
            ]
        }
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "client_number": ["Client Number"],
        "user_name": ["User Name"],
        "table_name": ["Table Name"],
        "change_number": ["Change Number"],
        "object_class": ["Object Class"],
        "date_of_change": ["Date of Change"],
        "field_name": ["Field Name"],
        "date": ["Date of Change"],
        # KPI helpers
        "high_risk_change": ["High Risk Change"]
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