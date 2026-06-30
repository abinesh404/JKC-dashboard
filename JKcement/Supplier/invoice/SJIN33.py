# Supplier/invoice/SJIN33.py
import pandas as pd
import os

CONFIG = {
    "id": "SJIN33",
    "name": "IV Quantity Exceeds GRN Quantity",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "IV Quantity Exceeds GRN Quantity",
            "cards": [
                {"id": "k1", "label": "Exception Transactions", "agg": "total_rows"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Vendors Impacted", "agg": "unique", "source": "vendor"},
                {"id": "k4", "label": "Total Invoice Amount", "agg": "sum", "source": "invoice_amount", "format": "currency"},
                {"id": "k5", "label": "Total Excess Quantity", "agg": "sum", "source": "excess_qty"},
                {"id": "k6", "label": "Total Local Currency Exposure", "agg": "sum", "source": "amount_lc", "format": "currency"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant Code", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Vendor Code", "source": "vendor", "all_label": "All Vendors"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise Excess IV Quantity"},
                {"id": "c2", "type": "bar", "x": "vendor", "y": "invoice_amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors by Excess Invoice Amount"},
                {"id": "c3", "type": "doughnut", "x": "plant", "agg": "count", "title": "Plant-wise Exception Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Monthly Exception Trend"},
                {"id": "c5", "type": "bar", "x": "purchasing_group", "y": "amount_lc", "agg": "sum", "title": "Purchasing Group-wise Exposure"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Name", "Company Code"],
        "vendor": ["Vendor Name1", "Vendor Code"],
        "plant": ["Plant Name", "Plant Code"],
        "invoice_amount": ["Invoice Amount"],
        "excess_qty": ["(IV Qty - GR Qty)"],
        "amount_lc": ["Amount in Local Currency"],
        "po_number": ["Purchasing Document Number"],
        "purchasing_group": ["Purchasing Group"],
        "date": ["Posting Date"],
        "amount": ["Invoice Amount"]
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
        f"data_files/SJIN33_Exception0{exc_id}.csv",
        f"data_files/SJIN33_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
