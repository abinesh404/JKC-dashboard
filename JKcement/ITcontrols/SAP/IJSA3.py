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
            "label": "Exception 01",
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
    paths = [
        rf"D:\off\JKC Dashboard\output\IJSA3_Exception01.csv",
        rf"D:\off\JKC Dashboard\output\IJSA3_Exception{int(exc_id):02}.csv",
        rf"data_files/IJSA3_Exception01.csv",
        rf"data_files/IJSA3_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    
    # Clean column whitespace
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to match Suggested Column Mapping exactly
    rename_map = {
        "Role Name assigned to user": "Role Name Assigned to User",
        "Role validity From": "Role Validity From",
        "Role validity To": "Role Validity To",
        "Role Change Date": "Role Change Date",
        "Role Change Time": "Role Change Time",
        "Collective Role Flag": "Collective Role Flag",
        "Inherited flag": "Inherited Flag",
        "Exclusion flag": "Exclusion Flag",
        "Authorization counter": "Authorization Counter",
        "User valid from": "User Valid From",
        "User valid to": "User Valid To",
        "User master record version": "User Master Record Version",
        "Creator of the User Master Record": "Creator of User Master Record",
        "Copied flag": "Copied Flag",
        "Newly created flag": "Newly Created Flag",
        "Indicator if record modified": "Indicator if Record Modified",
        "Indicator if deleted": "Indicator if Deleted"
    }
    df = df.rename(columns=rename_map)
    
    # Fallback/fill missing columns to prevent errors if not present
    required_cols = [
        "User Name", "Account ID", "User Type", "User Valid From", "User Valid To",
        "User Lock Status", "Creator of User Master Record", "User Master Record Version",
        "Role Name Assigned to User", "Role Validity From", "Role Validity To",
        "Collective Role Flag", "Role Change Date", "Role Change Time",
        "Transaction Code", "Tcode Description", "Program Name", "Critical_Access",
        "Inherited Flag", "Exclusion Flag", "Authorization Object", "Authorization Field Name",
        "Field Value", "Authorization Counter", "Folder Path", "Node ID",
        "Copied Flag", "Newly Created Flag", "Indicator if Record Modified", "Indicator if Deleted"
    ]
    for col in required_cols:
        if col not in df.columns:
            df[col] = ""
            
    # Calculate helper values for KPI cards
    today_str = datetime.date.today().strftime('%Y-%m-%d')
    
    def check_active(row):
        val = row.get("User Valid To")
        if pd.isna(val) or val == "":
            return True
        val_str = str(val).strip()
        if any(yr in val_str for yr in ["9999", "2200", "2999", "2099"]):
            return True
        return val_str >= today_str

    def check_locked(row):
        val = row.get("User Lock Status")
        if pd.isna(val) or val == "":
            return False
        val_str = str(val).strip().lower()
        return val_str not in ["0", "not locked", "active", "nan", ""]

    def check_critical(row):
        val = row.get("Critical_Access")
        if pd.isna(val) or val == "":
            return False
        val_str = str(val).strip().lower()
        return val_str in ["yes", "critical tcode access", "critical", "true", "1"]

    df["Active User Name"] = df.apply(lambda r: r["User Name"] if check_active(r) else "", axis=1)
    df["Locked User Name"] = df.apply(lambda r: r["User Name"] if check_locked(r) else "", axis=1)
    df["Critical Role Name"] = df.apply(lambda r: r["Role Name Assigned to User"] if check_critical(r) else "", axis=1)

    return df.fillna('')
