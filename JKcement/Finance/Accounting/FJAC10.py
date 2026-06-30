# Finance/Accounting/FJAC10.py — Documents of PY processed in CY with Ageing
# -------------------------------------------------------------------------

import pandas as pd
import os
import numpy as np
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC10",
    "name": "Vendor Documents of PY processed in CY with Ageing",
    "active_exceptions": [
        {
            "id": "1", 
            "label": "Exception 01", 
            "title": get_exception_title("Vendor Documents of PY processed in CY with Ageing"),
            "cards": [
                {"id": "k1", "label": "Total Vendor Docs (PY)", "agg": "total_rows"},
                {"id": "k2", "label": "Processed in CY Count", "agg": "sum", "source": "is_exception"},
                {"id": "k3", "label": "% Processed in CY", "agg": "percentage", "source": "is_exception"},
                {"id": "k4", "label": "Total Amt (Affected)", "agg": "sum", "source": "affected_amount", "format": "currency"},
                {"id": "k5", "label": "Avg Ageing (Days)", "agg": "avg", "source": "ageing_days_filtered"},
                {"id": "k6", "label": "Max Ageing (Days)", "agg": "max", "source": "ageing_days"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company"},
                {"id": "f2", "label": "Fiscal Year", "source": "fiscal_year"},
                {"id": "f3", "label": "Vendor Number", "source": "vendor"}
            ],
            "charts": [
                {
                    "id": "c1", "type": "pie", "x": "status_label", "agg": "count",
                    "title": get_chart_title("Overall Exception Visibility", "Ratio")
                },
                {
                    "id": "c2", "type": "bar", "x": "company", "y": "is_exception", "agg": "sum", "top_n": 10,
                    "horizontal": True, "title": get_chart_title("Company-wise Impact", "Exception Count", top_n=10)
                },
                {
                    "id": "c3", "type": "line", "x": "clr_dt", "y": "ageing_days_filtered", "agg": "avg", "time_group": "month",
                    "title": get_chart_title("Ageing Trend", "Avg Days (Monthly)")
                },
                {
                    "id": "c4", "type": "doughnut", "x": "doctype", "y": "is_exception", "agg": "sum",
                    "title": get_chart_title("Distribution by Doc Type")
                },
                {
                    "id": "c5", "type": "bar", "x": "vendor_name", "y": "affected_amount", "agg": "sum", "top_n": 10,
                    "title": get_chart_title("Risk Concentration", "Amount by Vendor", top_n=10)
                }
            ]
        }
    ],
    "columns": {
        "amount":   ["Amount in Local Currency", "Amount", "DMBTR"],
        "vendor":   ["Vendor Number", "LIFNR", "Account"],
        "vendor_name": ["Vendor Name", "NAME1"],
        "date":     ["Document Date", "BLDAT"],
        "clearing_date": ["Clearing Date", "AUGDT"],
        "company":  ["Company Code", "BUKRS"],
        "fiscal_year": ["Fiscal Year", "GJAHR"],
        "fiscal_year_clearing": ["Fiscal Year_Clearing Document", "GJAHR_AUG"],
        "doctype":  ["Document Type", "BLART"],
        "is_exception": ["is_exception"],
        "affected_amount": ["affected_amount"],
        "status_label": ["status_label"],
        "ageing_days": ["ageing_days"],
        "ageing_days_filtered": ["ageing_days_filtered"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    path = rf"D:\off\JKC Dashboard\output\FJAC10_Exception{int(exc_id):02}.csv"
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
    col_doc_dt = find_col("date")
    col_clr_dt = find_col("clearing_date")
    col_fy_doc = find_col("fiscal_year")
    col_fy_clr = find_col("fiscal_year_clearing")

    if all([col_doc_dt, col_clr_dt, col_fy_doc, col_fy_clr]):
        # Data Cleaning & Conversion
        df['doc_dt'] = pd.to_datetime(df[col_doc_dt], errors='coerce')
        df['clr_dt'] = pd.to_datetime(df[col_clr_dt], errors='coerce')
        
        fy_doc_val = pd.to_numeric(df[col_fy_doc], errors='coerce').fillna(0)
        fy_clr_val = pd.to_numeric(df[col_fy_clr], errors='coerce').fillna(0)
        
        # Derived Logic: (Clearing FY > Document FY)
        df['is_exception'] = (fy_doc_val < fy_clr_val).astype(int)
        
        # Ageing Calculation: Clearing Date - Document Date
        df['ageing_days'] = (df['clr_dt'] - df['doc_dt']).dt.days.fillna(0)
        
        # Prepare for charts (convert timestamps to string)
        df['clr_dt'] = df['clr_dt'].dt.strftime('%Y-%m-%d').fillna('')
        
        # Trick for average of ONLY exceptions in a population:
        # We use ageing_days_filtered for sum, but for average we have a problem.
        df['ageing_days_filtered'] = np.where(df['is_exception'] == 1, df['ageing_days'], 0)
        
        # Amount cleaning
        if col_amt:
            amt_val = pd.to_numeric(df[col_amt].astype(str).str.replace(r'[^\d.-]', '', regex=True), errors='coerce').fillna(0)
            df['affected_amount'] = np.where(df['is_exception'] == 1, amt_val, 0)
        else:
            df['affected_amount'] = 0
            
        # Status Label for Pie Chart
        df['status_label'] = np.where(df['is_exception'] == 1, "PY Processed in CY", "Normal Processing")
    else:
        df['is_exception'] = 0
        df['ageing_days'] = 0
        df['ageing_days_filtered'] = 0
        df['affected_amount'] = 0
        df['status_label'] = "Normal Processing"

    return df
