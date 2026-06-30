# Finance/Accounting/FJAC12.py — Unauthorised MIRO Entries
# -------------------------------------------------------------------------

import pandas as pd
import os
import numpy as np
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC12",
    "name": "Unauthorised MIRO Entries",
    "active_exceptions": [
        {
            "id": "1", 
            "label": "Exception 01", 
            "title": get_exception_title("Unauthorised MIRO Entries"),
            "cards": [
                {"id": "k1", "label": "Total MIRO Invoices", "agg": "sum", "source": "is_miro"},
                {"id": "k2", "label": "Unauthorized Entries", "agg": "sum", "source": "is_exception"},
                {"id": "k3", "label": "% Unauthorized", "agg": "percentage", "source": "is_exception"},
                {"id": "k4", "label": "Total Amt (Unauth)", "agg": "sum", "source": "affected_amount", "format": "currency"},
                {"id": "k5", "label": "Unauthorized Users", "agg": "unique", "source": "unauth_user"},
                {"id": "k6", "label": "Vendors Impacted", "agg": "unique", "source": "unauth_vendor"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company"},
                {"id": "f2", "label": "Fiscal Year", "source": "year"},
                {"id": "f3", "label": "MIRO Created User", "source": "miro_user"}
            ],
            "charts": [
                {
                    "id": "c1", "type": "pie", "x": "status_label", "agg": "count",
                    "title": get_chart_title("Control Breach Overview", "Ratio")
                },
                {
                    "id": "c2", "type": "bar", "x": "miro_user", "y": "is_exception", "agg": "sum", "top_n": 10,
                    "title": get_chart_title("Risky Users", "Unauthorized Count", top_n=10)
                },
                {
                    "id": "c3", "type": "line", "x": "posting_date_dt", "y": "is_exception", "agg": "sum", "time_group": "month",
                    "title": get_chart_title("Violation Trend", "Monthly Count")
                },
                {
                    "id": "c4", "type": "doughnut", "x": "user_type_group", "y": "is_exception", "agg": "sum",
                    "title": get_chart_title("Segmentation by User Group")
                },
                {
                    "id": "c5", "type": "bar", "x": "vendor_name", "y": "affected_amount", "agg": "sum", "top_n": 10,
                    "title": get_chart_title("Financial Impact", "Amount by Vendor", top_n=10)
                }
            ]
        }
    ],
    "columns": {
        "amount":       ["Amount"],
        "vendor":       ["Vendor Name", "Vendor"],
        "vendor_name":  ["Vendor Name"],
        "date":         ["Posting Date"],
        "miro_user":    ["MIRO Created User"],
        "company":      ["Company Code"],
        "year":         ["Fiscal Year"],
        "tcode":        ["Transaction Code"],
        "valid_from":   ["User Valid From Date"],
        "valid_to":     ["User Valid To Date"],
        "user_type":    ["User Type"],
        "user_group":   ["User Group"],
        "is_miro":      ["is_miro"],
        "is_exception": ["is_exception"],
        "affected_amount": ["affected_amount"],
        "status_label": ["status_label"],
        "unauth_user":  ["unauth_user"],
        "unauth_vendor": ["unauth_vendor"],
        "posting_date_dt": ["Posting Date"],
        "user_type_group": ["user_type_group"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    path = rf"D:\off\JKC Dashboard\output\FJAC12_Exception{int(exc_id):02}.csv"
    if not os.path.exists(path):
        return None
    
    df = pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    if df.empty:
        return df

    # Column Mapping Helpers
    def find_col(key):
        cands = CONFIG["columns"].get(key, [])
        for c in df.columns:
            if str(c).strip() in cands: return c
        return None

    col_amt = find_col("amount")
    col_tcode = find_col("tcode")
    col_post_dt = find_col("date")
    col_from_dt = find_col("valid_from")
    col_to_dt = find_col("valid_to")
    col_user = find_col("miro_user")
    col_vend = find_col("vendor")
    col_utype = find_col("user_type")
    col_ugroup = find_col("user_group")

    # Step 1: Detect MIRO transactions
    if col_tcode:
        df['is_miro'] = (df[col_tcode].astype(str).str.strip() == "MIRO").astype(int)
    else:
        df['is_miro'] = 1 # Assume all are MIRO if column missing in exception file

    # Step 2: Check user validity
    if all([col_post_dt, col_from_dt, col_to_dt]):
        p_dt = pd.to_datetime(df[col_post_dt], errors='coerce')
        f_dt = pd.to_datetime(df[col_from_dt], errors='coerce')
        t_dt = pd.to_datetime(df[col_to_dt], errors='coerce')
        
        # Valid if Posting Date is between From and To
        # Unauthorized if NOT valid (and is MIRO)
        df['is_valid_user'] = ((p_dt >= f_dt) & (p_dt <= t_dt)).astype(int)
        df['is_exception'] = ((df['is_miro'] == 1) & (df['is_valid_user'] == 0)).astype(int)
    else:
        df['is_exception'] = 0
    
    # Amount cleaning
    if col_amt:
        amt_val = pd.to_numeric(df[col_amt].astype(str).str.replace(r'[^\d.-]', '', regex=True), errors='coerce').fillna(0)
        df['affected_amount'] = np.where(df['is_exception'] == 1, amt_val, 0)
    else:
        df['affected_amount'] = 0
            
    # Status Label
    df['status_label'] = np.where(df['is_exception'] == 1, "Unauthorized MIRO", "Authorized MIRO")
    
    # Helpers for unique count
    df['unauth_user'] = np.where(df['is_exception'] == 1, df[col_user].astype(str) if col_user else "", "")
    df['unauth_vendor'] = np.where(df['is_exception'] == 1, df[col_vend].astype(str) if col_vend else "", "")
    
    # Formatting for trend
    if col_post_dt:
        df['posting_date_dt'] = pd.to_datetime(df[col_post_dt], errors='coerce').dt.strftime('%Y-%m-%d').fillna('')
    else:
        df['posting_date_dt'] = ''

    # User Type / Group combined for Chart 4
    if col_utype and col_ugroup:
        df['user_type_group'] = df[col_utype].astype(str) + " / " + df[col_ugroup].astype(str)
    elif col_utype:
        df['user_type_group'] = df[col_utype].astype(str)
    else:
        df['user_type_group'] = "Unknown"

    return df
