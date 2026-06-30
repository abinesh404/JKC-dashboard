# Supplier/invoice/SJIN10.py
import pandas as pd
import os

CONFIG = {
    "id": "SJIN10",
    "name": "Mismatch Invoice and PO Vendor",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Mismatch Invoice and PO Vendor",
            "cards": [
                {"id": "k1", "label": "Mismatch Transactions", "agg": "total_rows"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k4", "label": "PO Vendors Involved", "agg": "unique", "source": "po_vendor"},
                {"id": "k5", "label": "Invoice Vendors Involved", "agg": "unique", "source": "invoice_vendor"},
                {"id": "k6", "label": "Total Invoice Amount", "agg": "total_value", "source": "amount", "format": "currency"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "PO Vendor", "source": "po_vendor", "all_label": "All PO Vendors"},
                {"id": "f4", "label": "Invoice Vendor", "source": "invoice_vendor", "all_label": "All Invoice Vendors"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise Vendor Mismatch"},
                {"id": "c2", "type": "bar", "x": "po_vendor", "y": "amount_doc", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top PO Vendors with Mismatch Transactions"},
                {"id": "c3", "type": "bar", "x": "invoice_vendor", "y": "amount_doc", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Invoice Vendors with Mismatch Transactions"},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Monthly Vendor Mismatch Trend"},
                {"id": "c5", "type": "doughnut", "x": "plant", "y": "amount_doc", "agg": "sum", "title": "Plant-wise Vendor Mismatch Exposure", "legend": True}
            ]
        }
    ],
    "columns": {
        "company": ["Company Name", "Company Code"],
        "plant": ["Plant"],
        "po_vendor": ["PO Vendor"],
        "invoice_vendor": ["Invoice Vendor"],
        "date": ["Document Date"],
        "amount_doc": ["Amount in Document Currency"],
        "amount": ["Amount in Document Currency"]
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
        f"data_files/SJIN10_Exception0{exc_id}.csv",
        f"data_files/SJIN10_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
