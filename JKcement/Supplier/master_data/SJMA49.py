# Supplier/master_data/SJMA49.py
import pandas as pd
import os

CONFIG = {
    "id": "SJMA49",
    "name": "Duplicate Vendor with Outstanding and Opposite Balance",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Vendors with Same Name and Address",
            "cards": [
                {"id": "k1", "label": "Duplicate Vendors", "agg": "unique", "source": "vendor"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Total Debit", "agg": "sum", "source": "total_debit", "format": "currency"},
                {"id": "k4", "label": "Total Credit", "agg": "sum", "source": "total_credit", "format": "currency"},
                {"id": "k5", "label": "Net Outstanding", "agg": "sum", "source": "net_outstanding", "format": "currency"},
                {"id": "k6", "label": "Active Vendor Accounts", "agg": "unique", "source": "vendor"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Country", "source": "country"},
                {"id": "f3", "label": "Account Group", "source": "account_group"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Duplicate Vendors by Company"},
                {"id": "c2", "type": "bar", "x": "vendor_name", "y": "net_outstanding", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors by Outstanding Amount"},
                {"id": "c3", "type": "doughnut", "x": "country", "agg": "count", "title": "Country-wise Duplicate Vendors", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Vendor Creation Trend"},
                {"id": "c5", "type": "bar", "x": "account_group", "agg": "count", "title": "Account Group Analysis"}
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": "Vendors with Same PAN Number",
            "cards": [
                {"id": "k1", "label": "Duplicate PAN Vendors", "agg": "unique", "source": "vendor"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Total Debit", "agg": "sum", "source": "total_debit", "format": "currency"},
                {"id": "k4", "label": "Total Credit", "agg": "sum", "source": "total_credit", "format": "currency"},
                {"id": "k5", "label": "Net Outstanding", "agg": "sum", "source": "net_outstanding", "format": "currency"},
                {"id": "k6", "label": "Active Vendor Accounts", "agg": "unique", "source": "vendor"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "PAN Number", "source": "pan_number"},
                {"id": "f3", "label": "Account Group", "source": "account_group"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "pan_number", "agg": "count", "title": "Vendors by PAN Number"},
                {"id": "c2", "type": "bar", "x": "vendor_name", "y": "net_outstanding", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors by Outstanding Amount"},
                {"id": "c3", "type": "doughnut", "x": "country", "agg": "count", "title": "Country-wise Duplicate Vendors", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Vendor Creation Trend"},
                {"id": "c5", "type": "bar", "x": "account_group", "agg": "count", "title": "Account Group Analysis"}
            ]
        },
        {
            "id": "3",
            "label": "Exception 03",
            "title": "Vendors with Same Tax Number",
            "cards": [
                {"id": "k1", "label": "Duplicate Tax Vendors", "agg": "unique", "source": "vendor"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Total Debit", "agg": "sum", "source": "total_debit", "format": "currency"},
                {"id": "k4", "label": "Total Credit", "agg": "sum", "source": "total_credit", "format": "currency"},
                {"id": "k5", "label": "Net Outstanding", "agg": "sum", "source": "net_outstanding", "format": "currency"},
                {"id": "k6", "label": "Active Vendor Accounts", "agg": "unique", "source": "vendor"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Tax Number", "source": "tax_number"},
                {"id": "f3", "label": "Account Group", "source": "account_group"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "tax_number", "agg": "count", "title": "Vendors by Tax Number"},
                {"id": "c2", "type": "bar", "x": "vendor_name", "y": "net_outstanding", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors by Outstanding Amount"},
                {"id": "c3", "type": "doughnut", "x": "country", "agg": "count", "title": "Country-wise Duplicate Vendors", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Vendor Creation Trend"},
                {"id": "c5", "type": "bar", "x": "account_group", "agg": "count", "title": "Account Group Analysis"}
            ]
        },
        {
            "id": "4",
            "label": "Exception 04",
            "title": "Vendors with Same Bank Account",
            "cards": [
                {"id": "k1", "label": "Duplicate Bank Accounts", "agg": "unique", "source": "bank_acct"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Total Debit", "agg": "sum", "source": "total_debit", "format": "currency"},
                {"id": "k4", "label": "Total Credit", "agg": "sum", "source": "total_credit", "format": "currency"},
                {"id": "k5", "label": "Net Outstanding", "agg": "sum", "source": "net_outstanding", "format": "currency"},
                {"id": "k6", "label": "Active Vendor Accounts", "agg": "unique", "source": "vendor"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Bank Account Number", "source": "bank_acct"},
                {"id": "f3", "label": "Account Group", "source": "account_group"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "bank_acct", "agg": "count", "title": "Vendors by Bank Account"},
                {"id": "c2", "type": "bar", "x": "vendor_name", "y": "net_outstanding", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors by Outstanding Amount"},
                {"id": "c3", "type": "doughnut", "x": "bank_country", "agg": "count", "title": "Bank Country Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Vendor Creation Trend"},
                {"id": "c5", "type": "bar", "x": "account_group", "agg": "count", "title": "Account Group Analysis"}
            ]
        },
        {
            "id": "5",
            "label": "Exception 05",
            "title": "Unique Vendors",
            "cards": [
                {"id": "k1", "label": "Unique Vendors", "agg": "unique", "source": "vendor"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Total Debit", "agg": "sum", "source": "total_debit", "format": "currency"},
                {"id": "k4", "label": "Total Credit", "agg": "sum", "source": "total_credit", "format": "currency"},
                {"id": "k5", "label": "Net Outstanding", "agg": "sum", "source": "net_outstanding", "format": "currency"},
                {"id": "k6", "label": "Duplicate Groups", "agg": "unique", "source": "pan_number"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Exception Type", "source": "exception_type"},
                {"id": "f3", "label": "Account Group", "source": "account_group"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "exception_type", "agg": "count", "title": "Unique Vendors by Exception Type"},
                {"id": "c2", "type": "bar", "x": "vendor_name", "y": "net_outstanding", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors by Outstanding Amount"},
                {"id": "c3", "type": "doughnut", "x": "country", "agg": "count", "title": "Country Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Vendor Creation Trend"},
                {"id": "c5", "type": "bar", "x": "account_group", "agg": "count", "title": "Account Group Analysis"}
            ]
        },
        {
            "id": "6",
            "label": "Exception 06",
            "title": "Outstanding in Vendor Account",
            "cards": [
                {"id": "k1", "label": "Vendors with Outstanding", "agg": "unique", "source": "vendor"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Total Outstanding", "agg": "sum", "source": "net_outstanding", "format": "currency"},
                {"id": "k4", "label": "Total Debit", "agg": "sum", "source": "total_debit", "format": "currency"},
                {"id": "k5", "label": "Total Credit", "agg": "sum", "source": "total_credit", "format": "currency"},
                {"id": "k6", "label": "Active Vendors", "agg": "unique", "source": "vendor"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "Account Group", "source": "account_group"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "vendor_name", "y": "net_outstanding", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors by Outstanding Amount"},
                {"id": "c2", "type": "bar", "x": "company", "y": "net_outstanding", "agg": "sum", "title": "Company-wise Outstanding Amount"},
                {"id": "c3", "type": "doughnut", "x": "country", "agg": "count", "title": "Country Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "y": "net_outstanding", "agg": "sum", "time_group": "month", "title": "Monthly Outstanding Trend"},
                {"id": "c5", "type": "bar", "x": "account_group", "y": "net_outstanding", "agg": "sum", "title": "Account Group Outstanding Analysis"}
            ]
        },
        {
            "id": "7",
            "label": "Exception 07",
            "title": "Debit in One Account and Credit in Another Account",
            "cards": [
                {"id": "k1", "label": "Opposite Balance Vendors", "agg": "unique", "source": "vendor"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Total Debit", "agg": "sum", "source": "debit", "format": "currency"},
                {"id": "k4", "label": "Total Credit", "agg": "sum", "source": "credit", "format": "currency"},
                {"id": "k5", "label": "Net Outstanding", "agg": "sum", "source": "net_outstanding", "format": "currency"},
                {"id": "k6", "label": "Vendor Pairs", "agg": "total_rows"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "Account Group", "source": "account_group"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "vendor_name", "y": "debit", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors by Debit Balance"},
                {"id": "c2", "type": "bar", "x": "vendor_code_right", "y": "credit", "agg": "sum", "top_n": 10, "title": "Top Credit Vendors"},
                {"id": "c3", "type": "doughnut", "x": "exception_type", "agg": "count", "title": "Pairs by Exception Type", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Vendor Creation Trend"},
                {"id": "c5", "type": "bar", "x": "account_group", "agg": "count", "title": "Account Group Analysis"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Name", "Company Code"],
        "vendor": ["Vendor Name", "Vendor Code"],
        "vendor_code": ["Vendor Code"],
        "vendor_code_right": ["Vendor Code (Right)"],
        "vendor_name": ["Vendor Name"],
        "account_group": ["Account group"],
        "country": ["Country"],
        "pan_number": ["PAN Number"],
        "tax_number": ["Tax Registration No.", "Tax Number"],
        "bank_acct": ["Bank Account Number"],
        "bank_country": ["Bank Country"],
        "exception_type": ["Exception"],
        "date": ["Created On"],
        "debit": ["Debit"],
        "credit": ["Credit"],
        "total_debit": ["Total Debit"],
        "total_credit": ["Total Credit"],
        "net_outstanding": ["Net Outstanding"],
        "amount": ["Net Outstanding"]
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
        f"data_files/SJMA49_Exception0{exc_id}.csv",
        f"data_files/SJMA49_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
