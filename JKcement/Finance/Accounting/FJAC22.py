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
            "label": "All Exceptions", 
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
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
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
        "exception_type": ["Exception Type"],
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
    insight_id = CONFIG["id"]
    merged_df = pd.DataFrame()
    for i in range(1, 10):
        path1 = f"data_files/{insight_id}_Exception0{i}.csv"
        path2 = f"data_files/{insight_id}_Exception{i}.csv"
        path = next((p for p in [path1, path2] if os.path.exists(p)), None)
        if path:
            df = pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
            df['Exception Type'] = f"Exception {i}"
            merged_df = pd.concat([merged_df, df], ignore_index=True)
    if merged_df.empty:
        return None
    return merged_df