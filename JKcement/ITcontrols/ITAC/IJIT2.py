# ITcontrols/ITAC/IJIT2.py
import pandas as pd
import os

CONFIG = {
    "id": "IJIT2",
    "name": "Tolerance Limit Unauthorized Changes",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "Unauthorized Changes to Tolerance Limits",
            "cards": [
                {"id": "k1", "label": "Tolerance Changes", "agg": "unique", "source": "change_doc_number"},
                {"id": "k2", "label": "Users Making Changes", "agg": "unique", "source": "user"},
                {"id": "k3", "label": "Tables Modified", "agg": "unique", "source": "table_name"},
                {"id": "k4", "label": "Fields Modified", "agg": "unique", "source": "field_name_changed"},
                {"id": "k5", "label": "Transaction Codes Used", "agg": "unique", "source": "transaction_code"},
                {"id": "k6", "label": "High Risk Changes", "agg": "unique", "source": "high_risk_change"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "User", "source": "user", "all_label": "All Users"},
                {"id": "f2", "label": "Transaction Code", "source": "transaction_code", "all_label": "All T-Codes"},
                {"id": "f3", "label": "Table Name", "source": "table_name", "all_label": "All Tables"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "user",
                    "agg": "count",
                    "title": "User-wise Tolerance Changes"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "table_name",
                    "agg": "count",
                    "horizontal": True,
                    "top_n": 10,
                    "title": "Most Modified Tables"
                },
                {
                    "id": "c3",
                    "type": "doughnut",
                    "x": "change_indicator",
                    "agg": "count",
                    "legend": True,
                    "title": "Change Indicator Distribution"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "change_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Change Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "transaction_code",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Transaction Code Analysis"
                }
            ]
        }
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "user": ["User"],
        "transaction_code": ["Transaction Code"],
        "table_name": ["Table Name"],
        "change_doc_number": ["Change Document Number"],
        "change_indicator": ["Change Indicator"],
        "change_date": ["Change Date"],
        "field_name_changed": ["Field Name Changed"],
        "date": ["Change Date"],
        # KPI helper
        "high_risk_change": ["High Risk Change"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "ITAC"
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