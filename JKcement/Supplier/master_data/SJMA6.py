# Supplier/master_data/SJMA6.py
import pandas as pd
import os

CONFIG = {
    "id": "SJMA6",
    "name": "Detect the Inactive Vendors",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Inactive Vendors",
            "cards": [
                {
                    "id": "k1",
                    "label": "Inactive Vendors",
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
                    "label": "Total Inactive Vendor Value",
                    "agg": "total_value",
                    "source": "amount",
                    "format": "currency"
                },
                {
                    "id": "k5",
                    "label": "Average Months Inactive",
                    "agg": "avg",
                    "source": "months_inactive"
                },
                {
                    "id": "k6",
                    "label": "Transaction Count",
                    "agg": "sum",
                    "source": "transaction_count"
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
                    "x": "inactivity_aging",
                    "agg": "count",
                    "title": "Inactive Vendors by Inactivity Aging"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "company",
                    "agg": "count",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top Companies with Inactive Vendors"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Vendor Activity Trend"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "account_group",
                    "agg": "count",
                    "title": "Vendor Account Group Distribution"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "plant",
                    "agg": "count",
                    "title": "Top Plants with Inactive Vendors"
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": "Inactive Vendors with Outstanding Balance",
            "cards": [
                {
                    "id": "k1",
                    "label": "Inactive Vendors with Open Balance",
                    "agg": "unique",
                    "source": "vendor"
                },
                {
                    "id": "k2",
                    "label": "Outstanding Balance",
                    "agg": "sum",
                    "source": "open_balance",
                    "format": "currency"
                },
                {
                    "id": "k3",
                    "label": "Companies Impacted",
                    "agg": "unique",
                    "source": "company"
                },
                {
                    "id": "k4",
                    "label": "Average Months Inactive",
                    "agg": "avg",
                    "source": "months_inactive"
                },
                {
                    "id": "k5",
                    "label": "Total Open Balance",
                    "agg": "total_value",
                    "source": "open_balance",
                    "format": "currency"
                },
                {
                    "id": "k6",
                    "label": "Vendors with High Outstanding Balance",
                    "agg": "unique",
                    "source": "vendor"
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
                    "x": "vendor",
                    "y": "open_balance",
                    "agg": "sum",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top Vendors by Outstanding Balance"
                },
                {
                    "id": "c2",
                    "type": "doughnut",
                    "x": "company",
                    "y": "open_balance",
                    "agg": "sum",
                    "title": "Outstanding Balance by Company"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "inactivity_aging",
                    "agg": "count",
                    "title": "Inactivity Aging Distribution"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "plant",
                    "agg": "count",
                    "title": "Top Plants with Outstanding Vendors"
                },
                {
                    "id": "c5",
                    "type": "pie",
                    "x": "account_group",
                    "agg": "count",
                    "title": "Vendor Account Group Distribution"
                }
            ]
        }
    ],
    "columns": {
        "company": [
            "Company Code",
            "Company Name"
        ],
        "vendor": [
            "Vendor",
            "Vendor Name"
        ],
        "plant": [
            "Plant"
        ],
        "location": [
            "Company City",
            "Vendor City",
            "Vendor Country",
            "Vendor Region"
        ],
        "amount": [
            "Total_Amount",
            "Open_Balance"
        ],
        "open_balance": [
            "Open_Balance"
        ],
        "activity": [
            "Transaction_Count",
            "Last_Posting_Date",
            "Posting Date",
            "Document Date"
        ],
        "transaction_count": [
            "Transaction_Count"
        ],
        "date": [
            "Clearing Date",
            "Posting Date",
            "Document Date",
            "Last_Posting_Date"
        ],
        "months_inactive": [
            "Months_Inactive"
        ],
        "inactivity_aging": [
            "Inactivity Aging"
        ],
        "account_group": [
            "Account Group"
        ],
        "vendor_details": [
            "Account Group",
            "Search Term 1",
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
        f"data_files/SJMA6_Exception0{exc_id}.csv",
        f"data_files/SJMA6_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
