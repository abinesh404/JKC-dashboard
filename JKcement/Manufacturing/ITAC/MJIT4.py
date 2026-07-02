# Manufacturing/ITAC/MJIT4.py
import pandas as pd
import os

CONFIG = {
    "id": "MJIT4",
    "name": "Message Configuration Check for Validity Period",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "Message Configuration Check for Validity Period",
            "cards": [
                {"id": "k1", "label": "Total Message Configurations", "agg": "unique", "source": "message_row_id"},
                {"id": "k2", "label": "Warning Messages", "agg": "unique", "source": "warning_msg_id"},
                {"id": "k3", "label": "Suppressed Messages", "agg": "unique", "source": "suppressed_msg_id"},
                {"id": "k4", "label": "Applications Impacted", "agg": "unique", "source": "application_area"},
                {"id": "k5", "label": "Message Numbers Impacted", "agg": "unique", "source": "message_number"},
                {"id": "k6", "label": "High Risk Configurations", "agg": "unique", "source": "high_risk_config_id"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "Application Area", "source": "application_area", "all_label": "All Areas"},
                {"id": "f2", "label": "Message Type", "source": "message_type", "all_label": "All Types"},
                {"id": "f3", "label": "Industry-specific Version", "source": "industry_version", "all_label": "All Versions"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "application_area",
                    "agg": "count",
                    "title": "Application Area Wise Message Configuration"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "message_type",
                    "agg": "count",
                    "title": "Message Type Distribution"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "warning_suppress_type",
                    "agg": "count",
                    "title": "Warning vs Suppress Configuration"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "industry_version",
                    "agg": "count",
                    "title": "Industry Version Analysis"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "language_key",
                    "agg": "count",
                    "title": "Language-wise Configuration Distribution"
                }
            ]
        }
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "application_area": ["Application Area"],
        "message_type": ["Message Type"],
        "industry_version": ["Industry-specific Version"],
        "language_key": ["Language Key"],
        "message_number": ["Message Number"],
        "warning_suppress_type": ["Message Type for Warning/Suppress"],
        # Helpers
        "message_row_id": ["Message Row ID"],
        "warning_msg_id": ["Warning Msg ID"],
        "suppressed_msg_id": ["Suppressed Msg ID"],
        "high_risk_config_id": ["High Risk Config ID"]
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