# Supplier/invoice/SJIN13.py
import pandas as pd
import os

CONFIG = {
    "id": "SJIN13",
    "name": "Unplanned Delivery Cost More Than 5% of Gross Invoice Value",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Instances where Unplanned Delivery Cost is More Than 5% of Gross Invoice Value",
            "cards": [
                {"id": "k1", "label": "Total Exception Transactions", "agg": "total_rows"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Vendors Impacted", "agg": "unique", "source": "vendor"},
                {"id": "k4", "label": "Total Gross Invoice Amount", "agg": "sum", "source": "gross_invoice_amount", "format": "currency"},
                {"id": "k5", "label": "Total Unplanned Delivery Cost", "agg": "sum", "source": "unplanned_delivery_cost", "format": "currency"},
                {"id": "k6", "label": "Average Delivery Cost %", "agg": "avg", "source": "pct_unplanned_delivery_cost", "format": "percentage"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company", "all_label": "All Companies"},
                {"id": "f2", "label": "Vendor Number", "source": "vendor", "all_label": "All Vendors"},
                {"id": "f3", "label": "Plant", "source": "plant", "all_label": "All Plants"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "y": "unplanned_delivery_cost", "agg": "sum", "title": "Company-wise Unplanned Delivery Cost"},
                {"id": "c2", "type": "bar", "x": "vendor", "y": "unplanned_delivery_cost", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors by Unplanned Delivery Cost"},
                {"id": "c3", "type": "doughnut", "x": "plant", "y": "unplanned_delivery_cost", "agg": "sum", "title": "Plant-wise Delivery Cost Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "y": "unplanned_delivery_cost", "agg": "sum", "time_group": "month", "title": "Monthly Trend of Unplanned Delivery Cost"},
                {"id": "c5", "type": "bar", "x": "user_name", "agg": "count", "title": "User-wise Posting Analysis"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Code Name", "Company Code"],
        "vendor": ["Vendor Number"],
        "plant": ["Plant Name", "Plant"],
        "gross_invoice_amount": ["Gross Invoice Amount"],
        "unplanned_delivery_cost": ["Unplanned Delivery Cost"],
        "pct_unplanned_delivery_cost": ["% of Unplanned Delivery Cost"],
        "date": ["Posting Date"],
        "user_name": ["User Name (who posted)"],
        "po_number": ["PO Number"],
        "amount": ["Gross Invoice Amount"]
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
        f"data_files/SJIN13_Exception0{exc_id}.csv",
        f"data_files/SJIN13_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
