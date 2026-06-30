# Manufacturing/ITAC/MJIT4.py
import pandas as pd
import os

CONFIG = {
    "id": "MJIT4",
    "name": "Message Configuration Check for Validity Period",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
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
    paths = [
        rf"D:\off\JKC Dashboard\output\MJIT4_Exception{int(exc_id):02}.csv",
        rf"data_files/MJIT4_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to match standard schema
    rename_map = {
        "Message Version": "Message Version",
        "Application Area": "Application Area",
        "Message number": "Message Number",
        "Message Type": "Message Type",
        "Message Type for “Warning/Suppress”": "Message Type for Warning/Suppress",
        "Industry-specific version": "Industry-specific Version",
        "Language Key": "Language Key",
        "Message Text": "Message Text"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = ""
            
    # Build helpers for KPI cards
    row_ids = []
    warning_ids = []
    suppressed_ids = []
    high_risk_ids = []
    
    for idx, row in df.iterrows():
        msg_num = str(row.get("Message Number", "")).strip()
        msg_type = str(row.get("Message Type", "")).strip().lower()
        warn_supp = str(row.get("Message Type for Warning/Suppress", "")).strip().lower()
        
        # Raw count helper
        row_ids.append(f"Msg_{idx}")
        
        # Warning Messages count
        if "warning" in msg_type or msg_type == "w":
            warning_ids.append(f"Warn_{idx}")
        else:
            warning_ids.append("")
            
        # Suppressed Messages count
        if "suppress" in msg_type or msg_type == "s":
            suppressed_ids.append(f"Supp_{idx}")
        else:
            suppressed_ids.append("")
            
        # High Risk Configurations (where warning_suppress is Suppress)
        if "suppress" in warn_supp or warn_supp == "s":
            high_risk_ids.append(f"Risk_{idx}")
        else:
            high_risk_ids.append("")
            
    df["Message Row ID"] = row_ids
    df["Warning Msg ID"] = warning_ids
    df["Suppressed Msg ID"] = suppressed_ids
    df["High Risk Config ID"] = high_risk_ids
    
    return df.fillna('')
