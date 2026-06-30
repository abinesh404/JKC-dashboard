# Supplier/invoice/SJIN12.py
import pandas as pd
import os

CONFIG = {
    "id": "SJIN12",
    "name": "Processing Duplicate Invoice for Fraudulent Purposes",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Duplicate Invoice based on Reference Number + Document Date",
            "cards": [
                {"id": "k1", "label": "Duplicate Invoices", "agg": "total_rows"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Vendors Involved", "agg": "unique", "source": "vendor"},
                {"id": "k4", "label": "Total Duplicate Amount", "agg": "total_value", "source": "amount_lc", "format": "currency"},
                {"id": "k5", "label": "Duplicate Reference Numbers", "agg": "unique", "source": "reference_number"},
                {"id": "k6", "label": "Potential Fraud Cases", "agg": "total_rows"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company", "all_label": "All Companies"},
                {"id": "f2", "label": "Vendor", "source": "vendor", "all_label": "All Vendors"},
                {"id": "f3", "label": "Fiscal Year", "source": "fiscal_year", "all_label": "All Years"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise Duplicate Invoices"},
                {"id": "c2", "type": "bar", "x": "vendor", "y": "amount_lc", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors with Duplicate Invoices"},
                {"id": "c3", "type": "doughnut", "x": "region", "agg": "count", "title": "Duplicate Invoice Distribution by Region"},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Monthly Duplicate Invoice Trend"},
                {"id": "c5", "type": "bar", "x": "payment_method", "agg": "count", "title": "Payment Method Analysis"}
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": "Duplicate Invoice based on Reference Number + Document Date + Amount",
            "cards": [
                {"id": "k1", "label": "Exact Duplicate Invoices", "agg": "total_rows"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Vendors Involved", "agg": "unique", "source": "vendor"},
                {"id": "k4", "label": "Total Duplicate Amount", "agg": "total_value", "source": "amount_lc", "format": "currency"},
                {"id": "k5", "label": "Duplicate Reference Numbers", "agg": "unique", "source": "reference_number"},
                {"id": "k6", "label": "High Risk Cases", "agg": "total_rows"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company", "all_label": "All Companies"},
                {"id": "f2", "label": "Vendor", "source": "vendor", "all_label": "All Vendors"},
                {"id": "f3", "label": "Fiscal Year", "source": "fiscal_year", "all_label": "All Years"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise Exact Duplicates"},
                {"id": "c2", "type": "bar", "x": "vendor", "y": "amount_lc", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors by Duplicate Amount"},
                {"id": "c3", "type": "doughnut", "x": "country", "agg": "count", "title": "Duplicate Distribution by Country"},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Monthly Exact Duplicate Trend"},
                {"id": "c5", "type": "bar", "x": "user_name", "agg": "count", "title": "User-wise Duplicate Processing"}
            ]
        },
        {
            "id": "3",
            "label": "Exception 03",
            "title": "Duplicate Invoice based on Reference Number + Amount in Local Currency",
            "cards": [
                {"id": "k1", "label": "Duplicate Invoices", "agg": "total_rows"},
                {"id": "k2", "label": "Vendors Involved", "agg": "unique", "source": "vendor"},
                {"id": "k3", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k4", "label": "Total Duplicate Amount", "agg": "total_value", "source": "amount_lc", "format": "currency"},
                {"id": "k5", "label": "Reference Numbers Repeated", "agg": "unique", "source": "reference_number"},
                {"id": "k6", "label": "Potential Fraud Cases", "agg": "total_rows"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company", "all_label": "All Companies"},
                {"id": "f2", "label": "Vendor", "source": "vendor", "all_label": "All Vendors"},
                {"id": "f3", "label": "Fiscal Year", "source": "fiscal_year", "all_label": "All Years"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise Duplicate Invoices"},
                {"id": "c2", "type": "bar", "x": "vendor", "y": "amount_lc", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors with Duplicate Payments"},
                {"id": "c3", "type": "doughnut", "x": "country", "agg": "count", "title": "Country-wise Duplicate Distribution"},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Monthly Duplicate Invoice Trend"},
                {"id": "c5", "type": "bar", "x": "doc_type", "agg": "count", "title": "Document Type Analysis"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Name", "Company Code"],
        "vendor": ["Vendor Name1", "Vendor"],
        "fiscal_year": ["Fiscal Year"],
        "amount_lc": ["Amount LC"],
        "amount": ["Amount LC", "Amount"],
        "reference_number": ["Reference Number"],
        "region": ["REGION"],
        "country": ["Country"],
        "payment_method": ["Payment method"],
        "user_name": ["User Name"],
        "doc_type": ["Document Type", "Document type"],
        "date": ["Posting Date"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Supplier Invoice"
    }

def get_data(exc_id):
    paths = [
        f"data_files/SJIN12_Exception0{exc_id}.csv",
        f"data_files/SJIN12_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
