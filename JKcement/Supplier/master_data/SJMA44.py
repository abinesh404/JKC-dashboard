# Supplier/master_data/SJMA44.py
import pandas as pd
import os

CONFIG = {
    "id": "SJMA44",
    "name": "Payment by Creating One Time Vendor Account",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Payment by Creating One-Time Vendor",
            "cards": [
                {"id": "k1", "label": "One-Time Vendors", "agg": "unique", "source": "vendor_code"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Payments Processed", "agg": "unique", "source": "document"},
                {"id": "k4", "label": "Total Payment Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Average Payment Amount", "agg": "avg", "source": "amount", "format": "currency"},
                {"id": "k6", "label": "Plants Impacted", "agg": "unique", "source": "plant"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Plant", "source": "plant"},
                {"id": "f3", "label": "Vendor Account Group", "source": "account_group"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "y": "amount", "agg": "sum", "title": "Company-wise One-Time Vendor Payments"},
                {"id": "c2", "type": "bar", "x": "vendor", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top One-Time Vendors by Payment Amount"},
                {"id": "c3", "type": "doughnut", "x": "account_group_desc", "agg": "count", "title": "Vendor Account Group Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": "Monthly One-Time Vendor Payment Trend"},
                {"id": "c5", "type": "bar", "x": "user", "agg": "count", "title": "Payments by User"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Description", "Company Code"],
        "vendor": ["Vendor Name", "Vendor Code"],
        "vendor_code": ["Vendor Code"],
        "plant": ["Plant Code"],
        "account_group": ["Vendor account group"],
        "account_group_desc": ["Vendor Account Group Description"],
        "amount": ["Amount in Local Currency"],
        "date": ["Posting Date in the Document", "Document Date in Document", "Clearing Date"],
        "user": ["Name of Person who Created the Object"],
        "document": ["Accounting Document Number"]
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
        f"data_files/SJMA44_Exception0{exc_id}.csv",
        f"data_files/SJMA44_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
