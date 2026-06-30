# Supplier/invoice/SJIN40.py
import pandas as pd
import os

CONFIG = {
    "id": "SJIN40",
    "name": "Single Source Vendor - Company Level",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Single Source Vendor - Company Level",
            "cards": [
                {"id": "k1", "label": "Single Source Vendors", "agg": "unique", "source": "vendor"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Materials Impacted", "agg": "unique", "source": "material"},
                {"id": "k4", "label": "Total Purchase Value", "agg": "sum", "source": "net_price", "format": "currency"},
                {"id": "k5", "label": "Total Purchase Quantity", "agg": "sum", "source": "po_qty"},
                {"id": "k6", "label": "Vendor Dependency Ratio", "agg": "ratio", "source": "net_price", "format": "percentage"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company", "all_label": "All Companies"},
                {"id": "f2", "label": "Vendor Code", "source": "vendor", "all_label": "All Vendors"},
                {"id": "f3", "label": "Material Group", "source": "material_group", "all_label": "All Material Groups"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise Single Source Vendors"},
                {"id": "c2", "type": "bar", "x": "vendor_name", "y": "net_price", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Single Source Vendors by Purchase Value"},
                {"id": "c3", "type": "doughnut", "x": "material_group", "agg": "count", "title": "Material Group Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "y": "po_qty", "agg": "sum", "time_group": "month", "title": "Monthly Single Source Procurement Trend"},
                {"id": "c5", "type": "bar", "x": "purchasing_group", "agg": "count", "title": "Purchasing Group Analysis"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Name", "Company Code"],
        "vendor": ["Vendor Code"],
        "vendor_name": ["Vendor Name"],
        "material": ["Material Number"],
        "material_group": ["Material Group"],
        "net_price": ["Net Price in Purchasing Document (in Document Currency)"],
        "po_qty": ["Purchase Order Quantity"],
        "purchasing_group": ["Purchasing Group"],
        "date": ["Purchasing Document Date"],
        "amount": ["Net Price in Purchasing Document (in Document Currency)"]
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
        f"data_files/SJIN40_Exception0{exc_id}.csv",
        f"data_files/SJIN40_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
