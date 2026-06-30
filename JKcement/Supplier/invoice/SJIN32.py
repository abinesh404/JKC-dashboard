# Supplier/invoice/SJIN32.py
import pandas as pd
import os

CONFIG = {
    "id": "SJIN32",
    "name": "IV Quantity Exceeds GRN Quantity and Payment Done",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "IV Quantity Exceeds GRN Quantity and Payment is Done",
            "cards": [
                {"id": "k1", "label": "Exception Transactions", "agg": "total_rows"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Vendors Impacted", "agg": "unique", "source": "vendor"},
                {"id": "k4", "label": "Total Invoice Amount", "agg": "sum", "source": "amount_lc", "format": "currency"},
                {"id": "k5", "label": "Total GRN Quantity", "agg": "sum", "source": "grn_qty"},
                {"id": "k6", "label": "Total Excess Invoice Quantity", "agg": "sum", "source": "excess_qty"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Vendor Account Number", "source": "vendor", "all_label": "All Vendors"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise Excess Invoice Quantity"},
                {"id": "c2", "type": "bar", "x": "vendor", "y": "amount_lc", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors by Excess Invoice Amount"},
                {"id": "c3", "type": "doughnut", "x": "plant", "agg": "count", "title": "Plant-wise Exception Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Monthly Excess Invoice Trend"},
                {"id": "c5", "type": "bar", "x": "po_type", "y": "amount_lc", "agg": "sum", "title": "Purchasing Document Type Analysis"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Code"],
        "vendor": ["Vendor Account Number"],
        "plant": ["Plant"],
        "amount_lc": ["Amount in Local Currency"],
        "grn_qty": ["Q+Sum(Derived_Quantity)"],
        "excess_qty": ["excess_qty"],
        "po_number": ["Purchasing Document Number"],
        "po_type": ["Purchasing Document Type"],
        "date": ["Posting Date in the Document"],
        "amount": ["Amount in Local Currency"]
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
        f"data_files/SJIN32_Exception0{exc_id}.csv",
        f"data_files/SJIN32_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    
    # Calculate excess_qty dynamically
    if 'E+Sum(Derived_Quantity)' in df.columns and 'Q+Sum(Derived_Quantity)' in df.columns:
        e_qty = pd.to_numeric(df['E+Sum(Derived_Quantity)'], errors='coerce').fillna(0)
        q_qty = pd.to_numeric(df['Q+Sum(Derived_Quantity)'], errors='coerce').fillna(0)
        df['excess_qty'] = e_qty - q_qty
    else:
        df['excess_qty'] = 0.0
        
    return df.fillna('')
