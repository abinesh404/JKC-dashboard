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
        {
            "id": "1", 
            "label": "Exception 01", 
            "title": get_exception_title("Digit Level Outlier Detection"),
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company"},
                {"id": "f2", "label": "Posting Date", "source": "date"},
                {"id": "f3", "label": "First Digit", "source": "digit"}
            ],
            "cards": [
                {"id": "k1", "label": "Flagged Digits", "agg": "unique", "source": "digit"},
                {"id": "k2", "label": "Max Deviation (%)", "agg": "total_value", "source": "deviation"},
                {"id": "k3", "label": "Max Deviation Digit", "agg": "unique", "source": "digit"},
                {"id": "k4", "label": "Flagged Trans Count", "agg": "row_count"},
                {"id": "k5", "label": "% Trans Flagged", "agg": "row_count"},
                {"id": "k6", "label": "Max Z-Score", "agg": "total_value", "source": "z_score"}
            ],
            "charts": [
                {
                    "id": "c1", "type": "pie", "x": "digit", "agg": "count", "title": get_chart_title("Flagged vs Non-Flagged Digits")
                },
                {
                    "id": "c2", "type": "bar", "x": "digit", "y": "deviation", "agg": "sum", "title": get_chart_title("First Digit", "Deviation")
                },
                {
                    "id": "c3", "type": "line", "x": "digit", "y": "z_score", "agg": "sum", "title": get_chart_title("First Digit", "Z-Score")
                },
                {
                    "id": "c4", "type": "doughnut", "x": "digit", "agg": "count", "title": get_chart_title("Share of Transactions")
                },
                {
                    "id": "c5", "type": "bar", "x": "digit", "y": "digit_count", "agg": "sum", "title": get_chart_title("First Digit", "Count of Digit")
                }
            ]
        },
        {
            "id": "2", 
            "label": "Exception 02", 
            "title": get_exception_title("Overall Benford Compliance"),
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company"},
                {"id": "f2", "label": "Fiscal Year", "source": "year"},
                {"id": "f3", "label": "Posting Date", "source": "date"}
            ],
            "cards": [
                {"id": "k1", "label": "Overall Chi-Square", "agg": "total_value", "source": "chi_square"},
                {"id": "k2", "label": "Critical Val (df=8)", "agg": "total_value", "source": "chi_square"},
                {"id": "k3", "label": "Compliance Status", "agg": "row_count"},
                {"id": "k4", "label": "Total Transactions", "agg": "row_count"},
                {"id": "k5", "label": "Total Amount (Local)", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k6", "label": "Avg Deviation (%)", "agg": "total_value", "source": "deviation"}
            ],
            "charts": [
                {
                    "id": "c1", "type": "pie", "x": "digit", "y": "actual", "agg": "sum", "title": get_chart_title("First Digit Distribution (Actual %)")
                },
                {
                    "id": "c2", "type": "bar", "x": "digit", "y": "actual", "agg": "sum", "title": get_chart_title("First Digit", "Actual Percent")
                },
                {
                    "id": "c3", "type": "line", "x": "date", "y": "chi_square", "agg": "sum", "time_group": "month", "title": get_chart_title("Posting Date", "Chi-Square Total")
                },
                {
                    "id": "c4", "type": "doughnut", "x": "digit", "agg": "count", "title": get_chart_title("Compliance Distribution")
                },
                {
                    "id": "c5", "type": "bar", "x": "digit", "y": "chi_square", "agg": "sum", "title": get_chart_title("First Digit", "Chi-Square Val")
                }
            ]
        },
        {
            "id": "3", 
            "label": "Exception 03", 
            "title": get_exception_title("Root Cause Analysis"),
            "filters": [
                {"id": "f1", "label": "First Digit", "source": "digit"},
                {"id": "f2", "label": "Posting Date", "source": "date"},
                {"id": "f3", "label": "Company Code", "source": "company"}
            ],
            "cards": [
                {"id": "k1", "label": "Abnormal Trans Count", "agg": "row_count"},
                {"id": "k2", "label": "Abnormal Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k3", "label": "Top User (Trans)", "agg": "unique", "source": "user"},
                {"id": "k4", "label": "Top Vendor (Amt)", "agg": "unique", "source": "vendor"},
                {"id": "k5", "label": "Top GL Account", "agg": "unique", "source": "gl"},
                {"id": "k6", "label": "Peak Posting Date", "agg": "unique", "source": "date"}
            ],
            "charts": [
                {
                    "id": "c1", "type": "pie", "x": "user", "agg": "count", "title": get_chart_title("Distribution by Username")
                },
                {
                    "id": "c2", "type": "bar", "x": "vendor", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": get_chart_title("Vendor Name", "Total Transaction Amount", top_n=10)
                },
                {
                    "id": "c3", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": get_chart_title("Posting Date", "Count of Transactions")
                },
                {
                    "id": "c4", "type": "doughnut", "x": "gl", "agg": "count", "title": get_chart_title("Distribution by GL Account")
                },
                {
                    "id": "c5", "type": "bar", "x": "user", "agg": "count", "top_n": 10, "title": get_chart_title("Username", "Count of Transactions", top_n=10)
                }
            ]
        }
    ],
    "columns": {
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
        rf"D:\off\JKC Dashboard\output\FJAC17_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
