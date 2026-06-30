# ITcontrols/ITAC/IJIT2.py
import pandas as pd
import os

CONFIG = {
    "id": "IJIT2",
    "name": "Tolerance Limit Unauthorized Changes",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
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
    paths = [
        rf"D:\off\JKC Dashboard\output\IJIT2_Exception{int(exc_id):02}.csv",
        rf"data_files/IJIT2_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename fields to match Suggested Column Mapping exactly
    rename_map = {
        "Table key": "Table Key",
        "Field Name changed": "Field Name Changed",
        "VERSION": "Version"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    required_cols = [
        "Change Document Number", "Change Indicator", "Change Date", "Change Time", "Planned Change Number",
        "OBJECTCLAS", "OBJECTID", "Table Name", "Table Key", "Field Name Changed", "Version",
        "User", "Transaction Code", "Language Key"
    ]
    for col in required_cols:
        if col not in df.columns:
            df[col] = ""
            
    # Check if change is critical/high-risk
    def is_high_risk(table, field):
        t_str = str(table).strip().upper() if pd.notna(table) else ""
        f_str = str(field).strip().upper() if pd.notna(field) else ""
        critical_tables = ["T169G", "T043G", "T043T", "T169F", "T169V", "T030"]
        critical_fields = ["TOLERANCE", "LIMIT", "VALUE", "PERCENT", "MAX", "MIN", "AMOUNT"]
        return t_str in critical_tables or any(x in f_str for x in critical_fields)

    # Build KPI helper for High Risk Changes
    high_risk = []
    for idx, row in df.iterrows():
        tbl = row.get("Table Name", "")
        fld = row.get("Field Name Changed", "")
        chg_num = str(row.get("Change Document Number", "")).strip()
        if is_high_risk(tbl, fld) and chg_num:
            high_risk.append(chg_num)
        else:
            high_risk.append("")
            
    df["High Risk Change"] = high_risk
    
    return df.fillna('')
