# Finance/Accounting/FJAC8.py — Non-usage GL Accounts
# -------------------------------------------------------------------------

import pandas as pd
import os
import numpy as np
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC8",
    "name": "Non-usage GL Accounts",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Non-usage GL Accounts"),
            "cards": [
                {"id": "k1", "label": "Total GL Accounts", "agg": "total_rows"},
                {"id": "k2", "label": "Non-Usage Accounts", "agg": "sum", "source": "is_not_used"},
                {"id": "k3", "label": "Non-Usage %", "agg": "percentage", "source": "is_not_used"},
                {"id": "k4", "label": "Used Accounts", "agg": "sum", "source": "is_used"},
                {"id": "k5", "label": "Recent Unused", "agg": "sum", "source": "recent_unused"},
                {"id": "k6", "label": "Groups Impacted", "agg": "unique", "source": "acc_group"}
            ],
            "filters": [
                {"id": "f1", "label": "Chart of Accounts", "source": "coa"},
                {"id": "f2", "label": "G/L Account Group", "source": "acc_group"},
                {"id": "f3", "label": "Created By", "source": "created_by"}
            ],
            "charts": [
                {
                    "id": "c1", "type": "pie", "x": "usage_label", "agg": "count",
                    "title": get_chart_title("Overall Usage Status")
                },
                {
                    "id": "c2", "type": "bar", "x": "acc_group", "y": "is_not_used", "agg": "sum", "top_n": 10,
                    "title": get_chart_title("Risk by Account Group", "Non-Usage")
                },
                {
                    "id": "c3", "type": "line", "x": "created_on", "y": "is_not_used", "agg": "sum", "time_group": "month",
                    "title": get_chart_title("Creation Trend (Unused)", "Monthly")
                },
                {
                    "id": "c4", "type": "doughnut", "x": "account_type", "y": "is_not_used", "agg": "sum",
                    "title": get_chart_title("Dist. by Statement Type", "Non-Usage")
                },
                {
                    "id": "c5", "type": "bar", "x": "created_by", "y": "is_not_used", "agg": "sum", "top_n": 10,
                    "title": get_chart_title("Top 10 Created By", "Non-Usage")
                }
            ]
        }
    ],
    "columns": {
        "coa": ["Chart of Accounts", "KTOPL"],
        "gl": ["G/L Account Number", "SAKNR"],
        "acc_group": ["G/L Account Group", "KTOKS"],
        "created_by": ["Created By", "ERNAM"],
        "created_on": ["Created On", "ERDAT"],
        "is_bs": ["Balance Sheet Account Indicator", "XBILK"],
        "del_flag": ["Indicator: Account marked for deletion", "LOEVM"],
        "block_flag": ["Indicator: Is Account Blocked for Posting", "SPERR"],
        "status": ["GL Status", "Status"],
        "is_not_used": ["is_not_used"],
        "is_used": ["is_used"],
        "usage_label": ["usage_label"],
        "account_type": ["account_type"],
        "recent_unused": ["recent_unused"],
        "date": ["Created On", "ERDAT"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    path = rf"D:\off\JKC Dashboard\output\FJAC8_Exception{int(exc_id):02}.csv"
    if not os.path.exists(path): return None
    
    df = pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    if df.empty: return df

    # Helper to find column by label
    def find_col(key):
        cands = CONFIG["columns"].get(key, [])
        for c in df.columns:
            if c.strip() in cands: return c
        return None

    status_c = find_col("status")
    del_c = find_col("del_flag")
    block_c = find_col("block_flag")
    bs_c = find_col("is_bs")
    date_c = find_col("created_on")

    # Critical Logic
    # Flag if (Not in Use) AND (NOT Deleted) AND (NOT Blocked)
    def is_not_used(row):
        in_use_str = str(row[status_c]).strip() if status_c else ""
        deleted = str(row[del_c]).strip() == 'X' if del_c else False
        blocked = str(row[block_c]).strip() == 'X' if block_c else False
        
        if in_use_str == 'Not in Use' and not deleted and not blocked:
            return 1
        return 0

    df['is_not_used'] = df.apply(is_not_used, axis=1)
    df['is_used'] = df[status_c].apply(lambda x: 1 if str(x).strip() == 'In Use' else 0) if status_c else 0
    
    def get_usage_label(row):
        if row['is_not_used']: return "Non-Usage"
        if row['is_used']: return "Used"
        return "Blocked/Deleted"
    
    df['usage_label'] = df.apply(get_usage_label, axis=1)
    
    # Account Type (BS vs P&L)
    if bs_c:
        df['account_type'] = df[bs_c].apply(lambda x: "Balance Sheet" if str(x).strip() == 'X' else "P&L")
    else:
        df['account_type'] = "Unknown"

    # Recent Unused
    if date_c:
        df['dt'] = pd.to_datetime(df[date_c], errors='coerce')
        # Arbitrary "Recent" = 2024 or later
        df['recent_unused'] = np.where((df['is_not_used'] == 1) & (df['dt'].dt.year >= 2024), 1, 0)
    else:
        df['recent_unused'] = 0

    return df
