# Manufacturing/Production/MJPR9.py
import pandas as pd
import os

CONFIG = {
    "id": "MJPR9",
    "name": "Receipt of Low Shelf Life Material",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "Remaining Shelf Life Less Than 50% at the Time of GRN",
            "cards": [
                {"id": "k1", "label": "Low Shelf Life GRNs", "agg": "unique", "source": "material_doc_id"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Vendors Impacted", "agg": "unique", "source": "vendor_account_number"},
                {"id": "k4", "label": "Total Quantity Received", "agg": "total_value", "source": "quantity"},
                {"id": "k5", "label": "Inventory Value at Risk", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k6", "label": "Average Remaining Shelf Life %", "agg": "avg", "source": "remaining_percent", "format": "percentage"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Vendor Account Number", "source": "vendor_account_number", "all_label": "All Vendors"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "name1",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Vendor-wise Low Shelf Life Receipts"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "plant",
                    "y": "amount",
                    "agg": "sum",
                    "title": "Plant-wise Inventory Value at Risk"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "material_number",
                    "y": "quantity",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Material-wise Quantity Received"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "posting_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Low Shelf Life Receipt Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "purchasing_group",
                    "agg": "count",
                    "title": "Purchasing Group Analysis"
                }
            ]
        }],
    "columns": {
        "exception_type": ["Exception Type"],
        "company_code": ["Company Code"],
        "plant": ["Plant"],
        "vendor_account_number": ["Vendor Account Number"],
        "purchasing_group": ["Purchasing Group"],
        "material_number": ["Material Number"],
        "name1": ["NAME1"],
        "quantity": ["Quantity"],
        "amount": ["Amount in Local Currency"],
        "remaining_percent": ["Remaining_Percent"],
        "remaining_shelf_life_days": ["Remaining Shelf Life Days"],
        "posting_date": ["Posting Date in the Document"],
        "date": ["Posting Date in the Document"],
        # Helpers
        "material_doc_id": ["Material Doc ID"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Production"
    }

def get_data(exc_id):
    insight_id = CONFIG["id"]
    merged_df = pd.DataFrame()
    for i in range(1, 10):
        path1 = f"data_files/{insight_id}_Exception0{i}.csv"
        path2 = f"data_files/{insight_id}_Exception{i}.csv"
        path = next((p for p in [path1, path2] if os.path.exists(p)), None)
        if path:
            df = pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
            df['Exception Type'] = f"Exception {i}"
            merged_df = pd.concat([merged_df, df], ignore_index=True)
    if merged_df.empty:
        return None
    return merged_df