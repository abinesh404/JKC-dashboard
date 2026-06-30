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
            "label": "Exception 01",
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
    paths = [
        rf"D:\off\JKC Dashboard\output\IJSA04_Exception01.csv",
        rf"D:\off\JKC Dashboard\output\IJSA4_Exception{int(exc_id):02}.csv",
        rf"data_files/IJSA04_Exception01.csv",
        rf"data_files/IJSA4_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Ensure standard columns are present
    required_cols = ["Client Name", "Client Number", "Client Role", "Change Option", "User Name", "Last Changed On"]
    for col in required_cols:
        if col not in df.columns:
            df[col] = ""
            
    # Check if a client configuration allows modification
    def is_modifiable(val):
        if pd.isna(val) or val == "":
            return False
        val_str = str(val).strip().lower()
        return any(x in val_str for x in ["allow", "modifiable", "change", "yes", "x", "1"])
        
    # Check if client role is Production
    def is_production(val):
        if pd.isna(val) or val == "":
            return False
        val_str = str(val).strip().lower()
        return val_str in ["production", "prod", "p", "prd"]

    # Build helpers for KPI cards
    prod_clients = []
    change_ids = []
    last_mod_clients = []
    high_risk_clients = []
    
    for idx, row in df.iterrows():
        c_num = str(row.get("Client Number", "")).strip()
        role = row.get("Client Role", "")
        opt = row.get("Change Option", "")
        uname = row.get("User Name", "")
        chg_on = row.get("Last Changed On", "")
        
        # Prod Clients Impacted (Production role)
        if is_production(role) and c_num:
            prod_clients.append(c_num)
        else:
            prod_clients.append("")
            
        # Changes Made (Has Last Changed On entry)
        if pd.notna(chg_on) and str(chg_on).strip() != "":
            change_ids.append(f"Chg_{idx}")
            last_mod_clients.append(c_num)
        else:
            change_ids.append("")
            last_mod_clients.append("")
            
        # High Risk Clients (Production AND modifiable status)
        if is_production(role) and is_modifiable(opt) and c_num:
            high_risk_clients.append(c_num)
        else:
            high_risk_clients.append("")
            
    df["Prod Client Number"] = prod_clients
    df["Change ID"] = change_ids
    df["Last Mod Client"] = last_mod_clients
    df["High Risk Client"] = high_risk_clients
    
    return df.fillna('')
