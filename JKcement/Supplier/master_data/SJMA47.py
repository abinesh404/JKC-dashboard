# Supplier/master_data/SJMA47.py
import pandas as pd
import os

CONFIG = {
    "id": "SJMA47",
    "name": "Excess Payment to Vendor with Unadjusted Advances",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Excess Payment to Vendor with Unadjusted Advances",
            "cards": [
                {"id": "k1", "label": "Vendors with Unadjusted Advances", "agg": "unique", "source": "vendor"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Total Excess Payment Amount", "agg": "total_value", "source": "invoice_amt", "format": "currency"},
                {"id": "k4", "label": "Total Unadjusted Advance Amount", "agg": "sum", "source": "advance_amt", "format": "currency"},
                {"id": "k5", "label": "Open Advance Documents", "agg": "unique", "source": "open_advance_docs"},
                {"id": "k6", "label": "Average Excess Payment", "agg": "avg", "source": "invoice_amt", "format": "currency"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "Special G/L Indicator", "source": "special_gl"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "y": "invoice_amt", "agg": "sum", "title": "Company-wise Excess Payments"},
                {"id": "c2", "type": "bar", "x": "vendor", "y": "invoice_amt", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors by Excess Payment"},
                {"id": "c3", "type": "doughnut", "x": "open_advance_count", "agg": "count", "title": "Unadjusted Advance Ageing", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "y": "invoice_amt", "agg": "sum", "time_group": "month", "title": "Monthly Excess Payment Trend"},
                {"id": "c5", "type": "bar", "x": "vendor", "y": "advance_amt", "agg": "sum", "top_n": 10, "title": "Vendors by Unadjusted Advance Amount"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Name"],
        "vendor": ["Vendor Name"],
        "special_gl": ["Special G/L Indicator"],
        "invoice_amt": ["Invoice Amount Paid"],
        "advance_amt": ["Total Unadjusted Advance Amount"],
        "open_advance_docs": ["Open Advance Document Numbers"],
        "open_advance_count": ["Count of Open Advance Posting Date"],
        "date": ["Date the Payment was Made"],
        "amount": ["Invoice Amount Paid"]
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
        f"data_files/SJMA47_Exception0{exc_id}.csv",
        f"data_files/SJMA47_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
