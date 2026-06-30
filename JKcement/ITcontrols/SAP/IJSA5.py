# ITcontrols/SAP/IJSA5.py
import pandas as pd
import os

CONFIG = {
    "id": "IJSA5",
    "name": "Direct Changes to SAP",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
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
    paths = [
        rf"D:\off\JKC Dashboard\output\IJSA05_Exception01.csv",
        rf"D:\off\JKC Dashboard\output\IJSA5_Exception{int(exc_id):02}.csv",
        rf"data_files/IJSA05_Exception01.csv",
        rf"data_files/IJSA5_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename UserName to User Name to standardise
    if "UserName" in df.columns:
        df = df.rename(columns={"UserName": "User Name"})
        
    # Ensure standard columns are present
    required_cols = [
        "Client Name", "Client Number", "Change Number", "Object Class", "Object ID",
        "User Name", "Date of Change", "Time of Change", "Old Value", "New Value",
        "Table Name", "Field Name"
    ]
    for col in required_cols:
        if col not in df.columns:
            df[col] = ""
            
    # Check if table is critical/high-risk
    def is_high_risk(table):
        if pd.isna(table) or table == "":
            return False
        t_str = str(table).strip().upper()
        critical_tables = [
            "USR02", "T000", "AGR_USERS", "PA0008", "V_T000", "TABLOG", "DBTABLOG", 
            "PROT", "CDHDR", "CDPOS", "RFBLG", "BSEG", "BKPF"
        ]
        return t_str in critical_tables or any(x in t_str for x in ["USER", "AUTH", "PASS", "SALARY", "PAYROLL"])

    # Build KPI helper for High Risk Changes
    high_risk = []
    for idx, row in df.iterrows():
        tbl = row.get("Table Name", "")
        chg_num = str(row.get("Change Number", "")).strip()
        if is_high_risk(tbl) and chg_num:
            high_risk.append(chg_num)
        else:
            high_risk.append("")
            
    df["High Risk Change"] = high_risk
    
    return df.fillna('')
