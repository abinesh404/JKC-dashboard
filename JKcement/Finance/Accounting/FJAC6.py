# Finance/Accounting/FJAC6.py — Missing & Backdated Invoicing
# -------------------------------------------------------------------------

import pandas as pd
import os
import numpy as np
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC6",
    "name": "Missing & Backdated Invoicing",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Missing Date Invoicing"),
            "cards": [
                {"id": "k1", "label": "Total Invoices", "agg": "total_rows"},
                {"id": "k2", "label": "Missing Billing Date", "agg": "sum", "source": "missing_billing"},
                {"id": "k3", "label": "Missing Posting Date", "agg": "sum", "source": "missing_posting"},
                {"id": "k4", "label": "Missing Doc Date", "agg": "sum", "source": "missing_doc"},
                {"id": "k5", "label": "Missing Date %", "agg": "percentage", "source": "is_missing"},
                {"id": "k6", "label": "Total Net Value", "agg": "total_value", "source": "missing_val", "format": "currency"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company"},
                {"id": "f2", "label": "Fiscal Year", "source": "fiscal_year"},
                {"id": "f3", "label": "Billing Type", "source": "billing_type"}
            ],
            "charts": [
                {
                    "id": "c1", "type": "pie", "x": "missing_type", "agg": "count",
                    "title": get_chart_title("Dist. of Missing Date Type")
                },
                {
                    "id": "c2", "type": "bar", "x": "company", "y": "is_missing", "agg": "sum", "top_n": 10,
                    "title": get_chart_title("Invoices with Missing Dates", "Count")
                },
                {
                    "id": "c3", "type": "line", "x": "entry_date", "y": "is_missing", "agg": "sum", "time_group": "month",
                    "title": get_chart_title("Trend", "Monthly")
                },
                {
                    "id": "c4", "type": "doughnut", "x": "completeness_status", "agg": "count",
                    "title": get_chart_title("Missing vs Complete Invoices")
                },
                {
                    "id": "c5", "type": "bar", "x": "user", "y": "is_missing", "agg": "sum", "top_n": 10,
                    "title": get_chart_title("Top 10 Users", "Missing Dates")
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": get_exception_title("Backdated Invoicing"),
            "cards": [
                {"id": "k1", "label": "Total Invoices", "agg": "total_rows"},
                {"id": "k2", "label": "Backdated Invoices", "agg": "sum", "source": "is_backdated"},
                {"id": "k3", "label": "Backdated %", "agg": "percentage", "source": "is_backdated"},
                {"id": "k4", "label": "Avg Backdating Days", "agg": "avg", "source": "backdate_days"},
                {"id": "k5", "label": "Max Backdating Days", "agg": "max", "source": "backdate_days"},
                {"id": "k6", "label": "Total Net Value", "agg": "total_value", "source": "backdated_val", "format": "currency"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company"},
                {"id": "f2", "label": "Fiscal Year", "source": "fiscal_year"},
                {"id": "f3", "label": "Sales Organization", "source": "sales_org"}
            ],
            "charts": [
                {
                    "id": "c1", "type": "pie", "x": "backdated_status", "agg": "count",
                    "title": get_chart_title("Backdated vs Normal Ratio")
                },
                {
                    "id": "c2", "type": "bar", "x": "company", "y": "is_backdated", "agg": "sum", "top_n": 10,
                    "title": get_chart_title("Backdated Invoices by Company")
                },
                {
                    "id": "c3", "type": "line", "x": "posting_date", "y": "is_backdated", "agg": "sum", "time_group": "month",
                    "title": get_chart_title("Trend", "Monthly")
                },
                {
                    "id": "c4", "type": "doughnut", "x": "sales_org", "y": "is_backdated", "agg": "sum",
                    "title": get_chart_title("Dist. by Sales Org")
                },
                {
                    "id": "c5", "type": "bar", "x": "user", "y": "backdate_days", "agg": "avg", "top_n": 10,
                    "title": get_chart_title("User-wise Avg Backdating", "Days")
                }
            ]
        }
    ],
    "columns": {
        "company": ["Company Code", "BUKRS"],
        "fiscal_year": ["Fiscal Year", "GJAHR"],
        "billing_type": ["Billing Type", "FKART"],
        "sales_org": ["Sales Organization", "VKORG"],
        "user": ["User", "ERNAM"],
        "billing_date": ["Billing Date", "FKDAT"],
        "posting_date": ["Posting Date", "BUDAT"],
        "created_on": ["Created On (Document Date)", "ERDAT"],
        "entry_date": ["Entry Date", "CPUDT"],
        "amount": ["Net Value", "NETWR"],
        "is_missing": ["is_missing"],
        "missing_billing": ["missing_billing"],
        "missing_posting": ["missing_posting"],
        "missing_doc": ["missing_doc"],
        "is_backdated": ["is_backdated"],
        "backdate_days": ["backdate_days"],
        "missing_type": ["missing_type"],
        "completeness_status": ["completeness_status"],
        "backdated_status": ["backdated_status"],
        "missing_val": ["missing_val"],
        "backdated_val": ["backdated_val"],
        "date": ["Entry Date", "Posting Date", "Created On (Document Date)"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    path = rf"D:\off\JKC Dashboard\output\FJAC6_Exception{int(exc_id):02}.csv"
    if not os.path.exists(path): return None
    
    df = pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')

    # Helper to find column by label
    def find_col(key):
        cands = CONFIG["columns"].get(key, [])
        for c in df.columns:
            if c.strip() in cands: return c
        return None

    bil_c = find_col("billing_date")
    pos_c = find_col("posting_date")
    doc_c = find_col("created_on")
    ent_c = find_col("entry_date")
    amt_c = find_col("amount")

    def to_dt(s): return pd.to_datetime(s, errors='coerce')

    df['bil_dt'] = to_dt(df[bil_c]) if bil_c else pd.NaT
    df['pos_dt'] = to_dt(df[pos_c]) if pos_c else pd.NaT
    df['doc_dt'] = to_dt(df[doc_c]) if doc_c else pd.NaT
    df['ent_dt'] = to_dt(df[ent_c]) if ent_c else pd.NaT

    # Exception 1 Logic: Missing Dates
    df['missing_billing'] = df['bil_dt'].isna().astype(int)
    df['missing_posting'] = df['pos_dt'].isna().astype(int)
    df['missing_doc'] = df['doc_dt'].isna().astype(int)
    df['is_missing'] = ((df['missing_billing'] == 1) | (df['missing_posting'] == 1) | (df['missing_doc'] == 1)).astype(int)
    
    def get_missing_type(row):
        if row['missing_billing']: return "Billing Date"
        if row['missing_posting']: return "Posting Date"
        if row['missing_doc']: return "Document Date"
        return "Complete"
    
    df['missing_type'] = df.apply(get_missing_type, axis=1)
    df['completeness_status'] = df['is_missing'].apply(lambda x: "Missing Dates" if x == 1 else "Complete")
    
    # Amount for Missing Date Invoices
    if amt_c:
        v = pd.to_numeric(df[amt_c].astype(str).str.replace(r'[^\d.-]', '', regex=True), errors='coerce').fillna(0)
        df['missing_val'] = np.where(df['is_missing'] == 1, v, 0)
    else:
        df['missing_val'] = 0

    # Exception 2 Logic: Backdated
    # Logic: Posting Date < Created On OR Billing Date < Entry Date (fallback for Delivery Date)
    df['is_back_p'] = (df['pos_dt'] < df['doc_dt']).astype(int)
    df['is_back_b'] = (df['bil_dt'] < df['ent_dt']).astype(int)
    df['is_backdated'] = ((df['is_back_p'] == 1) | (df['is_back_b'] == 1)).astype(int)
    
    # Backdating Days (diff between Entry/Created and Billing/Posting)
    d1 = (df['doc_dt'] - df['pos_dt']).dt.days.fillna(0)
    d2 = (df['ent_dt'] - df['bil_dt']).dt.days.fillna(0)
    df['backdate_days'] = np.maximum(d1, d2)
    df['backdate_days'] = np.where(df['is_backdated'] == 1, df['backdate_days'], 0)
    
    df['backdated_status'] = df['is_backdated'].apply(lambda x: "Backdated" if x == 1 else "Normal")

    if amt_c:
        v = pd.to_numeric(df[amt_c].astype(str).str.replace(r'[^\d.-]', '', regex=True), errors='coerce').fillna(0)
        df['backdated_val'] = np.where(df['is_backdated'] == 1, v, 0)
    else:
        df['backdated_val'] = 0

    return df
