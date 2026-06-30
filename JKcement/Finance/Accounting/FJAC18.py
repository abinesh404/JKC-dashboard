# Finance/Accounting/FJAC18.py — Statistical Model for Expenses
# -------------------------------------------------------------------------

import pandas as pd
import os
import numpy as np
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC18",
    "name": "Statistical Model_Expense",
    "active_exceptions": [
        {
            "id": "1", 
            "label": "Exception 01", 
            "title": get_exception_title("Digit Level Outlier Detection"),
            "cards": [
                {"id": "k1", "label": "Flagged Digits", "agg": "unique", "source": "flagged_digit"},
                {"id": "k2", "label": "Max Deviation (%)", "agg": "max", "source": "deviation"},
                {"id": "k3", "label": "Max Devaition Digits", "agg": "unique", "source": "digit"},
                {"id": "k4", "label": "Total Amount (Flagged)", "agg": "sum", "source": "flagged_amount", "format": "currency"},
                {"id": "k5", "label": "% Trans Flagged", "agg": "percentage", "source": "is_exception"},
                {"id": "k6", "label": "Max Z-Score", "agg": "max", "source": "z_score"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company"},
                {"id": "f2", "label": "Fiscal Year", "source": "year"},
                {"id": "f3", "label": "GL Account", "source": "gl"}
            ],
            "charts": [
                {
                    "id": "c1", "type": "pie", "x": "status_label", "agg": "count",
                    "title": get_chart_title("Flagged vs Non-Flagged Digits")
                },
                {
                    "id": "c2", "type": "bar", "x": "digit", "y": "deviation", "agg": "sum",
                    "title": get_chart_title("First Digit", "Deviation")
                },
                {
                    "id": "c3", "type": "line", "x": "digit", "y": "z_score", "agg": "sum",
                    "title": get_chart_title("First Digit", "Z-Score")
                },
                {
                    "id": "c4", "type": "doughnut", "x": "digit", "y": "flagged_amount", "agg": "sum",
                    "title": get_chart_title("Flagged Digits Contribution", "Amount %")
                },
                {
                    "id": "c5", "type": "bar", "x": "digit", "y": "digit_count", "agg": "sum",
                    "title": get_chart_title("First Digit", "Count of Digit")
                }
            ]
        },
        {
            "id": "2", 
            "label": "Exception 02", 
            "title": get_exception_title("Overall Benford Compliance"),
            "cards": [
                {"id": "k1", "label": "Overall Chi-Square", "agg": "sum", "source": "chi_square"},
                {"id": "k2", "label": "Critical Val (df=8)", "agg": "max", "source": "crit_val"},
                {"id": "k3", "label": "Compliance Status", "agg": "row_count"},
                {"id": "k4", "label": "Total Transactions", "agg": "total_rows"},
                {"id": "k5", "label": "Total Expense Amt", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k6", "label": "Avg Deviation (%)", "agg": "avg", "source": "deviation"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company"},
                {"id": "f2", "label": "Fiscal Year", "source": "year"},
                {"id": "f3", "label": "Cost Center", "source": "cost_center"}
            ],
            "charts": [
                {
                    "id": "c1", "type": "pie", "x": "digit", "y": "actual_pct", "agg": "sum",
                    "title": get_chart_title("First Digit Distribution", "Actual %")
                },
                {
                    "id": "c2", "type": "bar", "x": "digit", "y": "actual_pct", "agg": "sum",
                    "title": get_chart_title("Actual vs Benford", "Percent")
                },
                {
                    "id": "c3", "type": "line", "x": "posting_date_dt", "y": "chi_square", "agg": "sum", "time_group": "month",
                    "title": get_chart_title("Trend", "Chi-Square Total")
                },
                {
                    "id": "c4", "type": "doughnut", "x": "digit", "agg": "count",
                    "title": get_chart_title("Compliance Distribution")
                },
                {
                    "id": "c5", "type": "bar", "x": "digit", "y": "chi_square", "agg": "sum",
                    "title": get_chart_title("First Digit", "Chi-Square Val")
                }
            ]
        },
        {
            "id": "3", 
            "label": "Exception 03", 
            "title": get_exception_title("Root Cause Analysis"),
            "cards": [
                {"id": "k1", "label": "Abnormal Transactions", "agg": "row_count"},
                {"id": "k2", "label": "Abnormal Expense Amt", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k3", "label": "Unique Users", "agg": "unique", "source": "user"},
                {"id": "k4", "label": "Unique Vendors", "agg": "unique", "source": "vendor_code"},
                {"id": "k5", "label": "Unique Cost Centers", "agg": "unique", "source": "cost_center"},
                {"id": "k6", "label": "Unique Profit Centers", "agg": "unique", "source": "profit_center"}
            ],
            "filters": [
                {"id": "f1", "label": "First Digit", "source": "digit"},
                {"id": "f2", "label": "Company Code", "source": "company"},
                {"id": "f3", "label": "Posting Date", "source": "posting_date_dt"}
            ],
            "charts": [
                {
                    "id": "c1", "type": "pie", "x": "user", "agg": "count",
                    "title": get_chart_title("Distribution by Username")
                },
                {
                    "id": "c2", "type": "bar", "x": "vendor_name", "y": "amount", "agg": "sum", "top_n": 10,
                    "title": get_chart_title("High-Value Vendors", "Amount", top_n=10)
                },
                {
                    "id": "c3", "type": "line", "x": "posting_date_dt", "agg": "count", "time_group": "month",
                    "title": get_chart_title("Transaction Trend", "Count")
                },
                {
                    "id": "c4", "type": "doughnut", "x": "cost_center", "agg": "count", "top_n": 10,
                    "title": get_chart_title("Distribution by Cost Center")
                },
                {
                    "id": "c5", "type": "bar", "x": "profit_center", "y": "amount", "agg": "sum", "top_n": 10,
                    "title": get_chart_title("High-Value Profit Centers", "Amount", top_n=10)
                }
            ]
        }
    ],
    "columns": {
        "amount":       ["Amount in Local Currency", "DMBTR"],
        "digit":        ["First_Digit"],
        "digit_count":  ["Count_of_Digit"],
        "deviation":    ["Deviation"],
        "z_score":      ["Z_Score"],
        "chi_square":   ["Chi_Square_Val"],
        "actual_pct":   ["Actual_percent"],
        "benford_prob": ["Benford_Prob"],
        "company":      ["Company Code", "BUKRS"],
        "year":         ["Fiscal Year", "GJAHR"],
        "gl":           ["General Ledger Account", "HKONT"],
        "cost_center":  ["Cost Center", "KOSTL"],
        "profit_center":["Profit Center", "PRCTR"],
        "user":         ["Username"],
        "vendor_code":  ["Vendor Code"],
        "vendor_name":  ["Vendor Name"],
        "posting_date_dt": ["Posting Date"],
        "is_exception": ["is_exception"],
        "status_label": ["status_label"],
        "flagged_amount":["flagged_amount"],
        "flagged_digit":["flagged_digit"],
        "crit_val":     ["crit_val"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    path = rf"D:\off\JKC Dashboard\output\FJAC18_Exception{int(exc_id):02}.csv"
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
    col_dev = find_col("deviation")
    col_z = find_col("z_score")
    col_digit = find_col("digit")
    col_post = find_col("posting_date_dt")

    # Data Cleaning and Calculations
    if col_amt:
        df['amt_val'] = pd.to_numeric(df[col_amt].astype(str).str.replace(r'[^\d.-]', '', regex=True), errors='coerce').fillna(0)
    else:
        df['amt_val'] = 0

    if col_dev and col_z:
        dev_val = pd.to_numeric(df[col_dev], errors='coerce').fillna(0)
        z_val = pd.to_numeric(df[col_z], errors='coerce').fillna(0)
        
        # Exception 01 Logic: Deviation > 5% or |Z| > 1.96
        df['is_exception'] = ((dev_val.abs() > 0.05) | (z_val.abs() > 1.96)).astype(int)
    else:
        df['is_exception'] = 0

    # Status Label
    df['status_label'] = np.where(df['is_exception'] == 1, "Flagged Digit", "Normal Digit")
    
    # Flagged helpers
    df['flagged_amount'] = np.where(df['is_exception'] == 1, df['amt_val'], 0)
    df['flagged_digit'] = np.where(df['is_exception'] == 1, df[col_digit].astype(str) if col_digit else "", "")
    df['crit_val'] = 15.51 # Critical value for Chi-Square with df=8 (alpha=0.05)

    # Date formatting
    if col_post:
        df['posting_date_dt'] = pd.to_datetime(df[col_post], errors='coerce').dt.strftime('%Y-%m-%d').fillna('')
    else:
        df['posting_date_dt'] = ''

    return df
