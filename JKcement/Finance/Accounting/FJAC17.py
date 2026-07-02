# Finance/Accounting/FJAC17.py — Statistical Model Vouchers
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------
# CSV COLUMNS: Vendor Code, Vendor Name, Vendor Account Group, City, Plant,
#   Region, Country Key, Company Code, Company City, Company Country Key,
#   Accounting Document Number, Document Type, Amount in Local Currency,
#   First_Digit, Count of Digit, Benford_Prob, Actual_percent, Deviation,
#   Expected_Count, Chi_Square_Val, Z_Score, Posting Date, Fiscal Year,
#   Username, GL Account, Cost Center, Profit Center, Item Text, Amount in Doc Currency
# -----------------------------------------------------
# AXIS ACCESS:
#   Pie    -> X: Vendor Name              | Y: Sum(Amount in Local Currency)
#   Bar    -> X: Company Code             | Y: Count of rows
#   Line   -> X: Posting Date (Monthly)   | Y: Sum(Amount in Local Currency)
#   Donut  -> X: Document Type            | Y: Count of rows
#   Column -> X: GL Account               | Y: Sum(Amount in Local Currency)
# -----------------------------------------------------

import pandas as pd
import os
from .template import get_chart_title, get_exception_title

CONFIG = {
    "id": "FJAC17",
    "name": "Statistical Model_Vouchers",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")},
        {"id": "3", "label": "Exception 03", "title": get_exception_title("Exception 03")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "amount": ["Amount in Local Currency", "Amount", "Total_Transaction_Amount"],
        "vendor": ["Vendor Name", "Vendor Code"],
        "date": ["Posting Date"],
        "gl": ["GL Account"],
        "company": ["Company Code"],
        "document": ["Accounting Document Number", "Document Number"],
        "digit": ["First_Digit"],
        "digit_count": ["Count of Digit"],
        "benford": ["Benford_Prob"],
        "actual": ["Actual_percent"],
        "deviation": ["Deviation"],
        "chi_square": ["Chi_Square_Val"],
        "z_score": ["Z_Score"],
        "user": ["Username"],
        "year": ["Fiscal Year"]
    }
}

def meta():
    return {"id": CONFIG["id"], "name": CONFIG["name"], "category": "Accounting"}

def get_data(exc_id):
    paths = [
        rf"data_files/FJAC17_Exception{int(exc_id):02}.csv",
        rf"data_files/FJAC17_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None