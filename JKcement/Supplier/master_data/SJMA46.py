# Supplier/master_data/SJMA46.py
import pandas as pd
import os

CONFIG = {
    "id": "SJMA46",
    "name": "Identify Duplicate Vendors in the System",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Vendor Name Appearing as Invalid / \"Do Not Use\" and None of the Codes are Blocked",
            "cards": [
                {"id": "k1", "label": "Duplicate Vendors", "agg": "unique", "source": "vendor"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Active Vendor Codes", "agg": "unique", "source": "vendor"},
                {"id": "k4", "label": "Total Transaction Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Vendors Not Blocked", "agg": "unique", "source": "vendor"},
                {"id": "k6", "label": "Duplicate Vendor Records", "agg": "total_rows"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor Account Group", "source": "vendor_group"},
                {"id": "f3", "label": "Country", "source": "country"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Duplicate Vendors by Company"},
                {"id": "c2", "type": "bar", "x": "vendor", "y": "amount_lc", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors by Transaction Amount"},
                {"id": "c3", "type": "doughnut", "x": "vendor_group", "agg": "count", "title": "Vendor Account Group Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "y": "amount_lc", "agg": "sum", "time_group": "month", "title": "Monthly Duplicate Vendor Transactions"},
                {"id": "c5", "type": "bar", "x": "country", "agg": "count", "title": "Country-wise Duplicate Vendors"}
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": "More Than Two Vendor Codes Created for the Same Vendor",
            "cards": [
                {"id": "k1", "label": "Duplicate Vendors", "agg": "unique", "source": "vendor_name"},
                {"id": "k2", "label": "Vendor Codes", "agg": "unique", "source": "vendor"},
                {"id": "k3", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k4", "label": "Total Transaction Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Average Vendor Codes", "agg": "avg", "source": "vendorcode_count"},
                {"id": "k6", "label": "Duplicate Groups", "agg": "unique", "source": "base_key"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor Account Group", "source": "vendor_group"},
                {"id": "f3", "label": "Country", "source": "country"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise Duplicate Vendors"},
                {"id": "c2", "type": "bar", "x": "vendor_name", "y": "vendorcode_count", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Vendors with Highest Duplicate Codes"},
                {"id": "c3", "type": "doughnut", "x": "vendor_group", "agg": "count", "title": "Vendor Account Group Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Monthly Duplicate Vendor Trend"},
                {"id": "c5", "type": "bar", "x": "country", "agg": "count", "title": "Country-wise Duplicate Vendors"}
            ]
        },
        {
            "id": "3",
            "label": "Exception 03",
            "title": "More Than Two Vendor Codes Created and None of the Codes are Blocked",
            "cards": [
                {"id": "k1", "label": "Duplicate Vendors", "agg": "unique", "source": "vendor_name"},
                {"id": "k2", "label": "Active Vendor Codes", "agg": "unique", "source": "vendor"},
                {"id": "k3", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k4", "label": "Total Transaction Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Unblocked Vendors", "agg": "unique", "source": "vendor"},
                {"id": "k6", "label": "High Risk Vendors", "agg": "unique", "source": "base_key"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor Account Group", "source": "vendor_group"},
                {"id": "f3", "label": "Country", "source": "country"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise Unblocked Duplicate Vendors"},
                {"id": "c2", "type": "bar", "x": "vendor_name", "y": "vendor_count2", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Vendors with Multiple Active Codes"},
                {"id": "c3", "type": "doughnut", "x": "vendor_group", "agg": "count", "title": "Vendor Account Group Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": "Monthly Duplicate Vendor Activity"},
                {"id": "c5", "type": "bar", "x": "blocked_flag", "agg": "count", "title": "Block Status Analysis"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Code"],
        "vendor_group": ["Vendor account group"],
        "country": ["Country Key"],
        "vendor": ["Vendor code ", "Vendor code", " Vendor code"],
        "vendor_name": ["NAME1_Ven"],
        "amount": ["Amount_LC", "Amount in Local Currency", "Sum(Amount_LC)"],
        "amount_lc": ["Amount_LC", "Amount in Local Currency"],
        "date": ["Posting Date in the Document"],
        "blocked_flag": ["BLOCKED_FLAG"],
        "vendorcode_count": ["Vendorcode_count"],
        "vendor_count2": ["Vendor_Count2"],
        "base_key": ["Base_Key"]
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
        f"data_files/SJMA46_Exception0{exc_id}.csv",
        f"data_files/SJMA46_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
