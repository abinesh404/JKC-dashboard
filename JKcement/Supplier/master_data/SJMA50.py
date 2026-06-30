# Supplier/master_data/SJMA50.py
import pandas as pd
import os

CONFIG = {
    "id": "SJMA50",
    "name": "Vendor Employee Name & Address Check",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Vendor with Same Name as Employee",
            "cards": [
                {"id": "k1", "label": "Matching Vendors", "agg": "unique", "source": "vendor"},
                {"id": "k2", "label": "Matching Employees", "agg": "unique", "source": "employee_code"},
                {"id": "k3", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k4", "label": "Vendor Account Groups", "agg": "unique", "source": "vendor_group"},
                {"id": "k5", "label": "Countries Impacted", "agg": "unique", "source": "vendor_country"},
                {"id": "k6", "label": "High Risk Matches", "agg": "total_rows"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor Country", "source": "vendor_country"},
                {"id": "f3", "label": "Vendor Account Group", "source": "vendor_group"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise Name Matches"},
                {"id": "c2", "type": "bar", "x": "vendor_group", "agg": "count", "title": "Vendor Account Group Distribution"},
                {"id": "c3", "type": "doughnut", "x": "vendor_country", "agg": "count", "title": "Country-wise Name Matches", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Vendor Creation Trend"},
                {"id": "c5", "type": "bar", "x": "created_by", "agg": "count", "title": "Top Vendor Creators"}
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": "Vendor with Same Address as Employee",
            "cards": [
                {"id": "k1", "label": "Address Matches", "agg": "total_rows"},
                {"id": "k2", "label": "Matching Vendors", "agg": "unique", "source": "vendor"},
                {"id": "k3", "label": "Matching Employees", "agg": "unique", "source": "employee_code"},
                {"id": "k4", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k5", "label": "Countries Impacted", "agg": "unique", "source": "vendor_country"},
                {"id": "k6", "label": "High Risk Matches", "agg": "total_rows"}
            ],
            "filters": [
                {"id": "f1", "label": "Vendor Country", "source": "vendor_country"},
                {"id": "f2", "label": "Employee Country", "source": "employee_country"},
                {"id": "f3", "label": "Vendor Account Group", "source": "vendor_group"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "vendor_country", "agg": "count", "title": "Country-wise Address Matches"},
                {"id": "c2", "type": "bar", "x": "vendor_city", "agg": "count", "title": "City-wise Address Matches"},
                {"id": "c3", "type": "doughnut", "x": "vendor_group", "agg": "count", "title": "Vendor Account Group Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Address Match Creation Trend"},
                {"id": "c5", "type": "bar", "x": "created_by", "agg": "count", "title": "Top Vendor Creators"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Name", "Company Code"],
        "vendor": ["Vendor code"],
        "employee_code": ["Employee code"],
        "vendor_group": ["Vendor Account group"],
        "vendor_country": ["Vendor Country"],
        "employee_country": ["Employee Country"],
        "vendor_city": ["Vendor City"],
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
        f"data_files/SJMA50_Exception0{exc_id}.csv",
        f"data_files/SJMA50_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
