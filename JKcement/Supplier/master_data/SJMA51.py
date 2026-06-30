# Supplier/master_data/SJMA51.py
import pandas as pd
import os

CONFIG = {
    "id": "SJMA51",
    "name": "Vendor Foreign Account",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Vendor Foreign Account",
            "cards": [
                {"id": "k1", "label": "Foreign Vendors", "agg": "unique", "source": "vendor"},
                {"id": "k2", "label": "Foreign Bank Accounts", "agg": "unique", "source": "bank_acct"},
                {"id": "k3", "label": "Countries Involved", "agg": "unique", "source": "bank_country"},
                {"id": "k4", "label": "Vendor Account Groups", "agg": "unique", "source": "vendor_group"},
                {"id": "k5", "label": "High Risk Vendors", "agg": "unique", "source": "vendor"},
                {"id": "k6", "label": "Vendors with Active Foreign Accounts", "agg": "unique", "source": "vendor"}
            ],
            "filters": [
                {"id": "f1", "label": "Vendor Country", "source": "vendor_country"},
                {"id": "f2", "label": "Vendor Bank Country", "source": "bank_country"},
                {"id": "f3", "label": "Vendor Account Group", "source": "vendor_group"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "vendor_country", "agg": "count", "title": "Vendor Country Distribution"},
                {"id": "c2", "type": "bar", "x": "bank_country", "agg": "count", "top_n": 10, "horizontal": True, "title": "Foreign Bank Country Distribution"},
                {"id": "c3", "type": "doughnut", "x": "vendor_group", "agg": "count", "title": "Vendor Account Group Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Foreign Vendor Creation Trend"},
                {"id": "c5", "type": "bar", "x": "created_by", "agg": "count", "title": "Vendors Created by User"}
            ]
        }
    ],
    "columns": {
        "vendor": ["Vendor code"],
        "vendor_country": ["Vendor Country"],
        "vendor_name": ["Vendor_Name"],
        "vendor_group": ["Vendor Account group"],
        "bank_country": ["Vendor Bank Country"],
        "bank_acct": ["Vendor Bank Account"],
        "date": ["Vendor Created on"],
        "created_by": ["Vendor Created by"]
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
        f"data_files/SJMA51_Exception0{exc_id}.csv",
        f"data_files/SJMA51_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
