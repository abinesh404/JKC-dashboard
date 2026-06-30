# Supplier/master_data/SJMA16.py
import pandas as pd
import os

CONFIG = {
    "id": "SJMA16",
    "name": "Vendor Name and Customer Name is Same",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Vendor and Customer Name Match – Neither Account is Blocked",
            "cards": [
                {"id": "k1", "label": "Matching Vendor-Customer Pairs", "agg": "unique", "source": "customer"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Active Vendor Accounts", "agg": "unique", "source": "vendor"},
                {"id": "k4", "label": "Active Customer Accounts", "agg": "unique", "source": "customer"},
                {"id": "k5", "label": "Total Transaction Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k6", "label": "Total Exceptions", "agg": "total_rows"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company"},
                {"id": "f2", "label": "Region", "source": "region"},
                {"id": "f3", "label": "Currency", "source": "currency"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company_cus", "agg": "count", "title": "Company-wise Matching Records"},
                {"id": "c2", "type": "bar", "x": "customer_name", "agg": "count", "top_n": 10, "horizontal": True, "title": "Top Customer Names"},
                {"id": "c3", "type": "doughnut", "x": "region", "agg": "count", "title": "Region-wise Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Monthly Posting Trend"},
                {"id": "c5", "type": "bar", "x": "company_cus", "y": "amount", "agg": "sum", "title": "Amount by Company"}
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": "Vendor & Customer Match in Same Company Code with Outstanding Balance",
            "cards": [
                {"id": "k1", "label": "Matching Pairs", "agg": "unique", "source": "customer"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Outstanding Transactions", "agg": "unique", "source": "doc_num"},
                {"id": "k4", "label": "Total Outstanding Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Same Company Matches", "agg": "unique", "source": "customer"},
                {"id": "k6", "label": "Total Exceptions", "agg": "total_rows"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company"},
                {"id": "f2", "label": "Region", "source": "region"},
                {"id": "f3", "label": "Currency", "source": "currency"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company_cus", "agg": "count", "title": "Company-wise Outstanding Matches"},
                {"id": "c2", "type": "bar", "x": "customer_name", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Customer Names by Amount"},
                {"id": "c3", "type": "doughnut", "x": "region", "agg": "count", "title": "Region-wise Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": "Monthly Posting Trend"},
                {"id": "c5", "type": "bar", "x": "payment_terms", "agg": "count", "title": "Terms of Payment Key"}
            ]
        },
        {
            "id": "3",
            "label": "Exception 03",
            "title": "Vendor & Customer Match in Different Company Codes with Outstanding Balance",
            "cards": [
                {"id": "k1", "label": "Matching Pairs", "agg": "unique", "source": "customer"},
                {"id": "k2", "label": "Different Company Matches", "agg": "unique", "source": "customer"},
                {"id": "k3", "label": "Outstanding Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k4", "label": "Active Accounts", "agg": "unique", "source": "customer"},
                {"id": "k5", "label": "Regions Impacted", "agg": "unique", "source": "region"},
                {"id": "k6", "label": "Total Exceptions", "agg": "total_rows"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company"},
                {"id": "f2", "label": "Region", "source": "region"},
                {"id": "f3", "label": "Currency", "source": "currency"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company_cus", "agg": "count", "title": "Company-wise Matches"},
                {"id": "c2", "type": "bar", "x": "customer_name", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Customer Names by Amount"},
                {"id": "c3", "type": "doughnut", "x": "region", "agg": "count", "title": "Region-wise Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "y": "amount", "agg": "sum", "time_group": "month", "title": "Monthly Posting Trend"},
                {"id": "c5", "type": "bar", "x": "posting_block_ven", "agg": "count", "title": "Posting Block for Company Code"}
            ]
        },
        {
            "id": "4",
            "label": "Exception 04",
            "title": "Vendor & Customer Match Across Company Codes with Outstanding Balance",
            "cards": [
                {"id": "k1", "label": "Matching Vendor-Customer Pairs", "agg": "unique", "source": "customer"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Outstanding Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k4", "label": "Customer Company Count", "agg": "unique", "source": "company_cus"},
                {"id": "k5", "label": "Vendor Company Count", "agg": "unique", "source": "company_ven"},
                {"id": "k6", "label": "Total Exceptions", "agg": "total_rows"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company"},
                {"id": "f2", "label": "Region", "source": "region"},
                {"id": "f3", "label": "Currency", "source": "currency"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company_ven", "agg": "count", "title": "Company-wise Records (Vendor)"},
                {"id": "c2", "type": "bar", "x": "vendor_name", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors by Amount"},
                {"id": "c3", "type": "doughnut", "x": "region", "agg": "count", "title": "Region-wise Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Monthly Posting Trend"},
                {"id": "c5", "type": "bar", "x": "payment_terms", "agg": "count", "title": "Terms of Payment Key"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Code_Cus", "Company Code_ven", "Company Code_Ven", "Customer code_ven"],
        "company_cus": ["Company Code_Cus"],
        "company_ven": ["Company Code_ven", "Company Code_Ven", "Customer code_ven"],
        "region": ["Region"],
        "currency": ["Currency Key"],
        "amount": ["Amount in Local Currency"],
        "amount_doc": ["Amount in document currency"],
        "vendor": ["Account Number of Vendor or Creditor"],
        "vendor_name": ["NAME1_Vendor"],
        "customer": ["Customer Number"],
        "customer_name": ["NAME1_Customer"],
        "date": ["Posting Date in the Document"],
        "doc_num": ["Accounting Document Number"],
        "payment_terms": ["Terms of Payment Key"],
        "posting_block_ven": ["Posting block for company code_Ven", "Posting Block for Company Code"],
        "cust_company_count": ["Cust_Company_Count"],
        "vend_company_count": ["Vend_Company_Count"]
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
        f"data_files/SJMA16_Exception0{exc_id}.csv",
        f"data_files/SJMA16_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
