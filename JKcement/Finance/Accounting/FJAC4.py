# Finance/Accounting/FJAC4.py — Documents Posted in Prior Reporting Period
# -------------------------------------------------------------------------

import pandas as pd
import os
import numpy as np
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC4",
    "name": "Documents Posted in Prior Reporting Period",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Customer Documents Posted in Prior Reporting Period"),
            "cards": [
                {"id": "k1", "label": "Total Customer Docs", "agg": "total_rows"},
                {"id": "k2", "label": "Prior Period Entries", "agg": "sum", "source": "is_exception"},
                {"id": "k3", "label": "Prior Period %", "agg": "percentage", "source": "is_exception"},
                {"id": "k4", "label": "Total Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Avg Days Diff", "agg": "avg", "source": "days_diff"},
                {"id": "k6", "label": "Company Codes", "agg": "unique", "source": "company"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company"},
                {"id": "f2", "label": "Fiscal Year", "source": "fiscal_year"},
                {"id": "f3", "label": "Customer Number", "source": "customer"}
            ],
            "charts": [
                {
                    "id": "c1", "type": "pie", "x": "status_label", "agg": "count",
                    "title": get_chart_title("Overall Exception Ratio")
                },
                {
                    "id": "c2", "type": "bar", "x": "company", "y": "is_exception", "agg": "sum", "top_n": 10,
                    "horizontal": True, "title": get_chart_title("Company-wise Risk", "Exceptions")
                },
                {
                    "id": "c3", "type": "line", "x": "entry_date", "y": "is_exception", "agg": "sum", "time_group": "month",
                    "title": get_chart_title("Issue Trend", "Monthly")
                },
                {
                    "id": "c4", "type": "doughnut", "x": "posting_key_name", "y": "is_exception", "agg": "sum",
                    "title": get_chart_title("Dist. by Posting Key")
                },
                {
                    "id": "c5", "type": "bar", "x": "cust_name", "y": "amount", "agg": "sum", "top_n": 10,
                    "title": get_chart_title("High-Value Impact", "Customer")
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": get_exception_title("Vendor Documents Posted in Prior Reporting Period"),
            "cards": [
                {"id": "k1", "label": "Total Vendor Docs", "agg": "total_rows"},
                {"id": "k2", "label": "Prior Period Entries", "agg": "sum", "source": "is_exception"},
                {"id": "k3", "label": "Prior Period %", "agg": "percentage", "source": "is_exception"},
                {"id": "k4", "label": "Total Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Avg Days Diff", "agg": "avg", "source": "days_diff"},
                {"id": "k6", "label": "Company Codes", "agg": "unique", "source": "company"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company"},
                {"id": "f2", "label": "Fiscal Year", "source": "fiscal_year"},
                {"id": "f3", "label": "Vendor Number", "source": "vendor"}
            ],
            "charts": [
                {
                    "id": "c1", "type": "pie", "x": "status_label", "agg": "count",
                    "title": get_chart_title("Overall Exception Ratio")
                },
                {
                    "id": "c2", "type": "bar", "x": "company", "y": "is_exception", "agg": "sum", "top_n": 10,
                    "horizontal": True, "title": get_chart_title("Company-wise Risk", "Exceptions")
                },
                {
                    "id": "c3", "type": "line", "x": "entry_date", "y": "is_exception", "agg": "sum", "time_group": "month",
                    "title": get_chart_title("Issue Trend", "Monthly")
                },
                {
                    "id": "c4", "type": "doughnut", "x": "posting_key_name", "y": "is_exception", "agg": "sum",
                    "title": get_chart_title("Dist. by Posting Key")
                },
                {
                    "id": "c5", "type": "bar", "x": "vend_name", "y": "amount", "agg": "sum", "top_n": 10,
                    "title": get_chart_title("High-Value Impact", "Vendor")
                }
            ]
        }
    ],
    "columns": {
        "company": ["Company Code", "BUKRS"],
        "fiscal_year": ["Fiscal Year", "GJAHR"],
        "customer": ["Customer Number", "KUNNR"],
        "cust_name": ["Customer Name", "NAME1_C"],
        "vendor": ["Vendor Number", "LIFNR", "Customer Number"],
        "vend_name": ["Vendor Name", "NAME1_V", "Customer Name"],
        "date": ["Accounting Document Entry Date", "CPUDT", "Posting Date in Document"],
        "posting_date": ["Posting Date in Document", "BUDAT"],
        "entry_date": ["Accounting Document Entry Date", "CPUDT"],
        "posting_period": ["Fiscal period", "MONAT"],
        "posting_key_name": ["Posting Key Name", "PTEXT"],
        "amount": ["Amount in Local Currency", "DMBTR"],
        "is_exception": ["is_exception"],
        "status_label": ["status_label"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    path = rf"D:\off\JKC Dashboard\output\FJAC4_Exception{int(exc_id):02}.csv"
    if not os.path.exists(path): return None
    
    df = pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    if df.empty: return df

    # Helper to find column by label
    def find_col(key):
        cands = CONFIG["columns"].get(key, [])
        for c in df.columns:
            if c.strip() in cands: return c
        return None

    post_c = find_col("posting_date")
    entry_c = find_col("entry_date")
    per_c = find_col("posting_period")

    if post_c and entry_c:
        df['post_dt'] = pd.to_datetime(df[post_c], errors='coerce')
        df['ent_dt'] = pd.to_datetime(df[entry_c], errors='coerce')
        
        # Derive Entry Period (Approximate as Month)
        df['ent_per'] = df['ent_dt'].dt.month
        df['post_per_val'] = pd.to_numeric(df[per_c] if per_c else 0, errors='coerce').fillna(0)

        # Critical Logic: (Posting Date < Entry Date) OR (Posting Period < Entry Period)
        df['is_exception'] = (df['post_dt'] < df['ent_dt']) | (df['post_per_val'] < df['ent_per'])
        df['is_exception'] = df['is_exception'].astype(int)
        
        # Days Difference
        df['days_diff'] = (df['ent_dt'] - df['post_dt']).dt.days.fillna(0)
        df['status_label'] = df['is_exception'].apply(lambda x: "Prior Period" if x == 1 else "Normal")
    else:
        df['is_exception'] = 0
        df['days_diff'] = 0
        df['status_label'] = "Normal"

    return df
