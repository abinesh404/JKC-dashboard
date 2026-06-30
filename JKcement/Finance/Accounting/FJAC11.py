# Finance/Accounting/FJAC11.py — Cost Center not belonging to WBS structure
# -------------------------------------------------------------------------

import pandas as pd
import os
import numpy as np
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC11",
    "name": "Cost Center not belonging to WBS structure",
    "active_exceptions": [
        {
            "id": "1", 
            "label": "Exception 01", 
            "title": get_exception_title("Cost Center does not belong to the WBS structure"),
            "cards": [
                {"id": "k1", "label": "Total Transactions", "agg": "total_rows"},
                {"id": "k2", "label": "Mismatch Count", "agg": "sum", "source": "is_exception"},
                {"id": "k3", "label": "% Mismatch", "agg": "percentage", "source": "is_exception"},
                {"id": "k4", "label": "Total Amt (Mismatch)", "agg": "sum", "source": "affected_amount", "format": "currency"},
                {"id": "k5", "label": "Cost Centers Involved", "agg": "unique", "source": "mismatch_cc"},
                {"id": "k6", "label": "WBS Elements Impacted", "agg": "unique", "source": "mismatch_wbs"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company"},
                {"id": "f2", "label": "Controlling Area", "source": "ctrl_area"},
                {"id": "f3", "label": "WBS Element", "source": "wbs"}
            ],
            "charts": [
                {
                    "id": "c1", "type": "pie", "x": "status_label", "agg": "count",
                    "title": get_chart_title("Overall Mapping Status", "Ratio")
                },
                {
                    "id": "c2", "type": "bar", "x": "cost_center", "y": "is_exception", "agg": "sum", "top_n": 10,
                    "title": get_chart_title("Problematic Cost Centers", "Mismatch Count", top_n=10)
                },
                {
                    "id": "c3", "type": "line", "x": "period_year", "y": "is_exception", "agg": "sum", "time_group": "month",
                    "title": get_chart_title("Mismatch Trend", "Issue Count")
                },
                {
                    "id": "c4", "type": "doughnut", "x": "company", "y": "is_exception", "agg": "sum",
                    "title": get_chart_title("Segmentation by Company")
                },
                {
                    "id": "c5", "type": "bar", "x": "wbs", "y": "affected_amount", "agg": "sum", "top_n": 10,
                    "title": get_chart_title("High-Impact Areas", "Amount by WBS", top_n=10)
                }
            ]
        }
    ],
    "columns": {
        "amount":       ["Amount", "DMBTR"],
        "cost_center":  ["Cost Center", "KOSTL"],
        "wbs":          ["WBS Element", "PS_PSP_PNR"],
        "ctrl_area":    ["Controlling Area", "KOKRS"],
        "company":      ["Company Code", "BUKRS"],
        "period":       ["Period", "MONAT"],
        "year":         ["Fiscal Year", "Fisacl Year", "GJAHR"],
        "exception":    ["Exception"],
        "is_exception": ["is_exception"],
        "affected_amount": ["affected_amount"],
        "status_label": ["status_label"],
        "mismatch_cc":  ["mismatch_cc"],
        "mismatch_wbs": ["mismatch_wbs"],
        "period_year":  ["period_year"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    path = rf"D:\off\JKC Dashboard\output\FJAC11_Exception{int(exc_id):02}.csv"
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
    col_cc = find_col("cost_center")
    col_wbs = find_col("wbs")
    col_exc = find_col("exception")
    col_per = find_col("period")
    col_yr = find_col("year")

    # Mismatch Detection
    # Note: As per user request, we detect mismatches. 
    # Since mapping_df is missing in the environment, we rely on the pre-calculated 'Exception' column 
    # or detect potential anomalies if Exception column is absent.
    if col_exc:
        # Assume '1' or non-empty string in Exception column means mismatch
        df['is_exception'] = df[col_exc].apply(lambda x: 1 if str(x).strip() in ['1', 'Mismatch', 'X', 'True'] else 0)
    else:
        # Fallback: If no Exception column, we mark everything in this Exception file as mismatch 
        # (Assuming the CSV generation logic already filtered it)
        df['is_exception'] = 1

    # Amount cleaning
    if col_amt:
        df['amt_val'] = pd.to_numeric(df[col_amt].astype(str).str.replace(r'[^\d.-]', '', regex=True), errors='coerce').fillna(0)
    else:
        df['amt_val'] = 0
    
    df['affected_amount'] = np.where(df['is_exception'] == 1, df['amt_val'], 0)
    
    # Status Label
    df['status_label'] = np.where(df['is_exception'] == 1, "Mismatch Transactions", "Valid Mapping")
    
    # Unique Count helpers (return value only for exceptions, else empty string)
    if col_cc:
        df['mismatch_cc'] = np.where(df['is_exception'] == 1, df[col_cc].astype(str), "")
    else:
        df['mismatch_cc'] = ""
        
    if col_wbs:
        df['mismatch_wbs'] = np.where(df['is_exception'] == 1, df[col_wbs].astype(str), "")
    else:
        df['mismatch_wbs'] = ""

    # Period/Year for Trend
    if col_per and col_yr:
        # Create a date-like string for the line chart (Month 1, Year 2024 -> 2024-01-01)
        try:
            df['period_year'] = pd.to_datetime(
                df[col_yr].astype(str).str.split('.').str[0] + '-' + 
                df[col_per].astype(str).str.zfill(2) + '-01', 
                errors='coerce'
            ).dt.strftime('%Y-%m-%d').fillna('')
        except:
            df['period_year'] = df[col_yr].astype(str) + '-' + df[col_per].astype(str)
    else:
        df['period_year'] = ''

    return df
