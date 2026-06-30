# Supplier/master_data/SJMA15.py
import pandas as pd
import os

CONFIG = {
    "id": "SJMA15",
    "name": "Dormant Vendor Accounts Not Blocked",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Dormant Vendors Not Blocked",
            "cards": [
                {
                    "id": "k1",
                    "label": "Dormant Vendors",
                    "agg": "unique",
                    "source": "vendor"
                },
                {
                    "id": "k2",
                    "label": "Companies Impacted",
                    "agg": "unique",
                    "source": "company"
                },
                {
                    "id": "k3",
                    "label": "Plants Impacted",
                    "agg": "unique",
                    "source": "plant"
                },
                {
                    "id": "k4",
                    "label": "Active Vendor Accounts",
                    "agg": "unique",
                    "source": "vendor"
                },
                {
                    "id": "k5",
                    "label": "Total Outstanding Amount",
                    "agg": "total_value",
                    "source": "net_outstanding",
                    "format": "currency"
                },
                {
                    "id": "k6",
                    "label": "Vendors with Posting Block = No",
                    "agg": "total_rows"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Plant", "source": "plant"},
                {"id": "f3", "label": "Vendor Account Group", "source": "account_group"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "company_name",
                    "agg": "count",
                    "title": "Dormant Vendors by Company"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "plant",
                    "agg": "count",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top Plants with Dormant Vendors"
                },
                {
                    "id": "c3",
                    "type": "doughnut",
                    "x": "status",
                    "agg": "count",
                    "title": "Dormant Vendor Status Distribution"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "account_group",
                    "agg": "count",
                    "title": "Dormant Vendors by Account Group"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "company_name",
                    "y": "net_outstanding",
                    "agg": "sum",
                    "title": "Outstanding Amount by Company"
                }
            ]
        }
    ],
    "columns": {
        "company": [
            "Company Code",
            "Company Name"
        ],
        "company_name": [
            "Company Name"
        ],
        "vendor": [
            "Vendor",
            "Vendor Name"
        ],
        "plant": [
            "Plant"
        ],
        "account_group": [
            "Account Group"
        ],
        "status": [
            "Status",
            "Posting Block",
            "Deletion Flag"
        ],
        "net_outstanding": [
            "Net_Outstanding",
            "Net Outstanding"
        ],
        "amount": [
            "Net_Outstanding",
            "Net Outstanding"
        ],
        "date": [
            "Created On"
        ]
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
        f"data_files/SJMA15_Exception0{exc_id}.csv",
        f"data_files/SJMA15_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
