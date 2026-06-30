# Supplier/master_data/SJMA20.py
import pandas as pd
import os

CONFIG = {
    "id": "SJMA20",
    "name": "To identify transactions where Vendor to Vendor & Vendor to customer Transfers have been made",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Vendor to Vendor Transfers",
            "cards": [
                {"id": "k1", "label": "Vendor Transfers", "agg": "total_rows"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Vendors Involved", "agg": "unique", "source": "vendor"},
                {"id": "k4", "label": "Total Transfer Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Clearing Documents", "agg": "unique", "source": "clearing_doc"},
                {"id": "k6", "label": "High Value Transfers", "agg": "total_rows"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "Fiscal Year", "source": "fiscal_year"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Vendor Transfers by Company"},
                {"id": "c2", "type": "bar", "x": "vendor", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors by Transfer Amount"},
                {"id": "c3", "type": "doughnut", "x": "offacc_grp_desc", "agg": "count", "title": "Vendor Account Group Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": "Monthly Vendor Transfer Trend"},
                {"id": "c5", "type": "bar", "x": "user", "agg": "count", "title": "Top Users Performing Vendor Transfers"}
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": "Vendor to Customer Transfers",
            "cards": [
                {"id": "k1", "label": "Vendor to Customer Transfers", "agg": "total_rows"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Vendors Involved", "agg": "unique", "source": "vendor"},
                {"id": "k4", "label": "Customers Involved", "agg": "unique", "source": "customer"},
                {"id": "k5", "label": "Total Transfer Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k6", "label": "High Value Transfers", "agg": "total_rows"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "Fiscal Year", "source": "fiscal_year"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Vendor to Customer Transfers by Company"},
                {"id": "c2", "type": "bar", "x": "customer", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Customers by Transfer Amount"},
                {"id": "c3", "type": "doughnut", "x": "cust_acct_grp", "agg": "count", "title": "Customer Account Group Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": "Monthly Vendor to Customer Transfer Trend"},
                {"id": "c5", "type": "bar", "x": "user", "agg": "count", "title": "Top Users Performing Transfers"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Code"],
        "vendor": ["Vendor", "OffAccNo"],
        "customer": ["Customer Number"],
        "fiscal_year": ["Fiscal Year"],
        "amount": ["Amount_LC_Converted", "Amount in LC", "Amount"],
        "date": ["Posting Date", "Document Date", "Clearing Date", "Created On"],
        "user": ["User Name", "Created By"],
        "clearing_doc": ["Clearing Document"],
        "offacc_grp_desc": ["OffAcc_Grp_Desc"],
        "cust_acct_grp": ["Cust Account Group", "Cust Account group"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Supplier Master Data"
    }

def get_data(exc_id):
    paths = [
        f"data_files/SJMA20_Exception0{exc_id}.csv",
        f"data_files/SJMA20_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
