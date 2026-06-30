# Finance/Accounting/FJAC22.py — Duplicate Payments
# -------------------------------------------------------------------------

import pandas as pd
import os
import numpy as np
import glob
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC22",
    "name": "Duplicate Payments Identification",
    "active_exceptions": [
        {
            "id": "1", 
            "label": "Exception 01", 
            "title": get_exception_title("Duplicate Payments (Same Invoice Ref, Vendor, Amount, Period)"),
            "cards": [
                {"id": "k1", "label": "Total Payments", "agg": "total_rows"},
                {"id": "k2", "label": "Duplicate Count", "agg": "sum", "source": "is_exception"},
                {"id": "k3", "label": "% Duplicate", "agg": "percentage", "source": "is_exception"},
                {"id": "k4", "label": "Total Dup Amt", "agg": "sum", "source": "affected_amount", "format": "currency"},
                {"id": "k5", "label": "Vendors Involved", "agg": "unique", "source": "dup_vendor"},
                {"id": "k6", "label": "Max Instances", "agg": "max", "source": "dup_count"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company"},
                {"id": "f2", "label": "Fiscal Year", "source": "year"},
                {"id": "f3", "label": "Vendor Code", "source": "vendor_code"}
            ],
            "charts": [
                {
                    "id": "c1", "type": "pie", "x": "status_label", "agg": "count",
                    "title": get_chart_title("Overall Duplicate Exposure", "Ratio")
                },
                {
                    "id": "c2", "type": "bar", "x": "vendor_name", "y": "is_exception", "agg": "sum", "top_n": 10,
                    "title": get_chart_title("Vendor Risk", "Duplicate Count", top_n=10)
                },
                {
                    "id": "c3", "type": "line", "x": "clearing_date_dt", "y": "is_exception", "agg": "sum", "time_group": "month",
                    "title": get_chart_title("Trend Over Time", "Duplicate Count")
                },
                {
                    "id": "c4", "type": "doughnut", "x": "doctype", "y": "is_exception", "agg": "sum",
                    "title": get_chart_title("Distribution by Doc Type")
                },
                {
                    "id": "c5", "type": "bar", "x": "ref_doc", "y": "affected_amount", "agg": "sum", "top_n": 10,
                    "title": get_chart_title("High-Impact Duplicates", "Amount", top_n=10)
                }
            ]
        }
    ],
    "columns": {
        "amount":       ["Amount in Local Currency", "Amount", "DMBTR"],
        "vendor_code":  ["Vendor Code", "LIFNR"],
        "vendor_name":  ["Vendor Name", "NAME1"],
        "ref_doc":      ["Reference Document Number", "XBLNR"],
        "clearing_month":["Clearing Month", "MONAT_AUG"],
        "clearing_year": ["Clearing Year", "GJAHR_AUG"],
        "clearing_date": ["Clearing Date", "AUGDT"],
        "company":      ["Company Code", "BUKRS"],
        "year":         ["Fiscal Year", "GJAHR"],
        "doctype":      ["Document Type", "BLART"],
        "is_exception": ["is_exception"],
        "affected_amount": ["affected_amount"],
        "status_label": ["status_label"],
        "dup_vendor":   ["dup_vendor"],
        "dup_count":    ["dup_count"],
        "clearing_date_dt": ["Clearing Date"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    # Filename is very long and has non-breaking spaces
    search_pattern = rf"D:\off\JKC Dashboard\Completed Output\FJAC22\Output\Exception01_FJAC22_*.csv"
    matches = glob.glob(search_pattern)
    
    # Fallback to output directory
    if not matches:
        matches = glob.glob(rf"D:\off\JKC Dashboard\output\FJAC22_Exception{int(exc_id):02}*.csv")
        
    if not matches:
        return None
        
    path = matches[0]
    
    # Large file optimization: only read some columns if possible, but we need several for logic.
    # The file has 5 lines of metadata/headers before the actual transaction headers.
    try:
        # Check first line for "Insight ID" to determine if we need to skip rows
        with open(path, 'r', encoding='latin1') as f:
            first_line = f.readline()
        
        skip = 0
        if "Insight ID" in first_line:
            skip = 4 # Skip 3 lines of metadata + 1 empty line
            
        df = pd.read_csv(path, encoding='latin1', low_memory=False, skiprows=skip).fillna('')
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return None
    if df.empty:
        return df

    # Column Mapping Helpers
    def find_col(key):
        cands = CONFIG["columns"].get(key, [])
        for c in df.columns:
            if str(c).strip() in cands: return c
        return None

    col_amt = find_col("amount")
    col_vend = find_col("vendor_code")
    col_ref = find_col("ref_doc")
    col_month = find_col("clearing_month")
    col_year = find_col("clearing_year")
    col_clr_dt = find_col("clearing_date")

    # Amount cleaning
    if col_amt:
        df['amt_val'] = pd.to_numeric(df[col_amt].astype(str).str.replace(r'[^\d.-]', '', regex=True), errors='coerce').fillna(0)
    else:
        df['amt_val'] = 0

    # Derived Logic: Duplicate payments
    group_cols = []
    if col_vend: group_cols.append(col_vend)
    if col_ref: group_cols.append(col_ref)
    if col_amt: group_cols.append(col_amt)
    if col_month: group_cols.append(col_month)
    if col_year: group_cols.append(col_year)

    if len(group_cols) >= 3:
        # Calculate counts per group
        df['dup_count'] = df.groupby(group_cols)[group_cols[0]].transform('count')
        df['is_exception'] = (df['dup_count'] > 1).astype(int)
    else:
        df['is_exception'] = 0
        df['dup_count'] = 1

    # Flagged helpers
    df['affected_amount'] = np.where(df['is_exception'] == 1, df['amt_val'], 0)
    df['status_label'] = np.where(df['is_exception'] == 1, "Duplicate Payments", "Valid Payments")
    
    if col_vend:
        df['dup_vendor'] = np.where(df['is_exception'] == 1, df[col_vend].astype(str), "")
    else:
        df['dup_vendor'] = ""

    # Date formatting for trend
    if col_clr_dt:
        df['clearing_date_dt'] = pd.to_datetime(df[col_clr_dt], errors='coerce').dt.strftime('%Y-%m-%d').fillna('')
    else:
        df['clearing_date_dt'] = ''

    return df
