# Supplier/invoice/SJIN30.py
import pandas as pd
import os

CONFIG = {
    "id": "SJIN30",
    "name": "PO Items Where GR Based IV Indicator is Not Activated",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "GR Based IV Indicator is Not Activated or Invoice Processed Without GRN",
            "cards": [
                {"id": "k1", "label": "Exception Transactions", "agg": "total_rows"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Vendors Impacted", "agg": "unique", "source": "vendor"},
                {"id": "k4", "label": "Total PO Amount", "agg": "sum", "source": "po_amount", "format": "currency"},
                {"id": "k5", "label": "Total Invoice Amount", "agg": "sum", "source": "invoice_amount", "format": "currency"},
                {"id": "k6", "label": "POs without GR-Based IV", "agg": "unique", "source": "po_number"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant Code", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Vendor Code", "source": "vendor", "all_label": "All Vendors"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise GR Based IV Exceptions"},
                {"id": "c2", "type": "bar", "x": "vendor", "y": "invoice_amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors by Invoice Amount"},
                {"id": "c3", "type": "doughnut", "x": "plant", "agg": "count", "title": "Plant-wise Exception Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Monthly Exception Trend"},
                {"id": "c5", "type": "bar", "x": "purchasing_group", "y": "invoice_amount", "agg": "sum", "title": "Purchasing Group-wise Exception Analysis"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Name", "Company Code"],
        "vendor": ["Vendor Name", "Vendor Code"],
        "plant": ["Plant Name", "Plant Code"],
        "po_amount": ["PO Amount"],
        "invoice_amount": ["Invoice Amount"],
        "po_number": ["Purchasing Document Number"],
        "purchasing_group": ["Puchasing Group", "Purchasing Group"],
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
        f"data_files/SJIN30_Exception0{exc_id}.csv",
        f"data_files/SJIN30_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
