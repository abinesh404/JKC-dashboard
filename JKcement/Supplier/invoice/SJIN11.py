# Supplier/invoice/SJIN11.py
import pandas as pd
import os

CONFIG = {
    "id": "SJIN11",
    "name": "Mismatch Invoice and PO Quantity and Amount",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Mismatch Invoice and PO Quantity and Amount",
            "cards": [
                {"id": "k1", "label": "Mismatch Transactions", "agg": "total_rows"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Vendors Impacted", "agg": "unique", "source": "invoice_vendor"},
                {"id": "k4", "label": "Total PO Amount", "agg": "sum", "source": "po_amt", "format": "currency"},
                {"id": "k5", "label": "Total Invoice Amount", "agg": "total_value", "source": "invoice_amt", "format": "currency"},
                {"id": "k6", "label": "Total Variance Amount", "agg": "sum", "source": "variance_amt", "format": "currency"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "PO Vendor", "source": "po_vendor", "all_label": "All PO Vendors"},
                {"id": "f4", "label": "Purchasing Organization", "source": "purchasing_org", "all_label": "All Purchasing Orgs"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise Quantity/Amount Mismatch"},
                {"id": "c2", "type": "bar", "x": "invoice_vendor", "y": "variance_amt", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Vendors by Variance Amount"},
                {"id": "c3", "type": "doughnut", "x": "plant", "y": "invoice_amt", "agg": "sum", "title": "Plant-wise Variance Exposure", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Monthly Mismatch Trend"},
                {"id": "c5", "type": "bar", "x": "purchasing_group", "y": "variance_amt", "agg": "sum", "title": "Purchasing Group-wise Variance"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Name", "Company Code"],
        "plant": ["Plant"],
        "po_vendor": ["PO_Vendor"],
        "invoice_vendor": ["Invoice_Vendor"],
        "purchasing_org": ["Purchasing Organization"],
        "purchasing_group": ["Purchasing Group"],
        "po_amt": ["PO_Amt"],
        "invoice_amt": ["Invoice_Amt"],
        "variance_amt": ["variance_amt"],
        "date": ["Posting Date"],
        "amount": ["Invoice_Amt"]
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
        f"data_files/SJIN11_Exception0{exc_id}.csv",
        f"data_files/SJIN11_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    df = pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    df.columns = [str(c).strip() for c in df.columns]
    
    if "Invoice_Amt" in df.columns and "PO_Amt" in df.columns:
        invoice_val = pd.to_numeric(df["Invoice_Amt"].astype(str).str.replace(r'[^\d.-]', '', regex=True), errors='coerce').fillna(0)
        po_val = pd.to_numeric(df["PO_Amt"].astype(str).str.replace(r'[^\d.-]', '', regex=True), errors='coerce').fillna(0)
        df["variance_amt"] = invoice_val - po_val
        
    return df
