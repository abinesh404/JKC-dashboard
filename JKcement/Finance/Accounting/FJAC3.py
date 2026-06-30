# Finance/Accounting/FJAC3.py — Vendor recon account not defined
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC3",
    "name": "Vendor recon account not defined",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Active vendors missing reconciliation account"),
            "cards": [
                {"id": "k1", "label": "Total Active Vendors", "agg": "total_rows"},
                {"id": "k2", "label": "Missing Recon Account", "agg": "total_value", "source": "recon_issue"},
                {"id": "k3", "label": "Impact %", "agg": "percentage", "source": "recon_issue"},
                {"id": "k4", "label": "Affected Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Company Codes", "agg": "unique", "source": "company"},
                {"id": "k6", "label": "Vendors w/ Usage", "agg": "unique", "source": "vendor"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company"},
                {"id": "f2", "label": "Account Group", "source": "acc_group"},
                {"id": "f3", "label": "Country", "source": "country"}
            ],
            "charts": [
                {
                    "id": "c1", "type": "pie", "x": "recon_status", "agg": "count",
                    "title": get_chart_title("Overall Issue Visibility")
                },
                {
                    "id": "c2", "type": "bar", "x": "company", "y": "recon_issue", "agg": "sum", "top_n": 10,
                    "horizontal": True, "title": get_chart_title("Top 10 High-Risk Companies", "Exceptions")
                },
                {
                    "id": "c3", "type": "line", "x": "created_on", "y": "recon_issue", "agg": "sum", "time_group": "month",
                    "title": get_chart_title("Issue Creation Trend", "Monthly")
                },
                {
                    "id": "c4", "type": "doughnut", "x": "acc_group", "y": "recon_issue", "agg": "sum",
                    "title": get_chart_title("Dist. by Account Group")
                },
                {
                    "id": "c5", "type": "bar", "x": "created_by", "y": "recon_issue", "agg": "sum", "top_n": 10,
                    "title": get_chart_title("Top 10 Created By", "Issue Count")
                }
            ]
        }
    ],
    "columns": {
        "company": ["Company Code", "BUKRS", "Name of Company Code or Company"],
        "vendor": ["Account Number of Vendor or Creditor", "Vendor Name", "LIFNR"],
        "recon": ["Reconciliation Account in General Ledger", "HKONT"],
        "acc_group": ["Vendor account group", "KTOKK"],
        "country": ["Country Key", "LAND1"],
        "created_by": ["Name of Person who Created the Object", "ERNAM"],
        "created_on": ["Date on which the Record Was Created", "ERDAT"],
        "del_flag": ["Deletion Flag for Master Record (Company Code Level)", "LOEVM"],
        "post_block": ["Posting block for company code", "SPERR"],
        "pay_block": ["Block Key for Payment", "SPERM"],
        "amount": ["Amount in Local Currency", "DMBTR"],
        "recon_issue": ["recon_issue"],
        "recon_status": ["recon_status"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    path = rf"D:\off\JKC Dashboard\output\FJAC3_Exception{int(exc_id):02}.csv"
    if not os.path.exists(path): return None
    
    df = pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')

    # Helper to find column by label
    def find_col(key):
        cands = CONFIG["columns"].get(key, [])
        for c in df.columns:
            if c.strip() in cands: return c
        return None

    del_c = find_col("del_flag")
    pos_c = find_col("post_block")
    pay_c = find_col("pay_block")
    rec_c = find_col("recon")

    # Filter to only include Active Vendors (Population)
    if not df.empty:
        if del_c: df = df[df[del_c] != 'X']
        if pos_c: df = df[df[pos_c] != 'Blocked']
        if pay_c: df = df[df[pay_c] != 'Blocked']

    # Initialize columns even if empty
    df['recon_issue'] = 0
    df['recon_status'] = "With Recon Account"

    # Identify Recon Issue if not empty
    if not df.empty and rec_c:
        df['recon_issue'] = df[rec_c].apply(lambda x: 1 if str(x).strip() in ['', 'nan', '0'] else 0)
        df['recon_status'] = df['recon_issue'].apply(lambda x: "Missing Recon Account" if x == 1 else "With Recon Account")

    return df
