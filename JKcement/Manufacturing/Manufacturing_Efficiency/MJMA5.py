# Manufacturing/Manufacturing_Efficiency/MJMA5.py
import pandas as pd
import os

CONFIG = {
    "id": "MJMA5",
    "name": "Missing Expiry Date",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "Manufacturing Date (HSDAT) and Expiry Date (VFDAT) Not Available",
            "cards": [
                {"id": "k1", "label": "Missing Expiry Date Records", "agg": "unique", "source": "message_row_id"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k4", "label": "Vendors Impacted", "agg": "unique", "source": "vendor_account_number"},
                {"id": "k5", "label": "Total Inventory Quantity", "agg": "total_value", "source": "quantity"},
                {"id": "k6", "label": "Total Inventory Value", "agg": "total_value", "source": "amount", "format": "currency"}
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
                    "x": "company_code",
                    "agg": "count",
                    "title": "Company-wise Missing Expiry Date Cases"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "plant",
                    "agg": "count",
                    "title": "Plant-wise Missing Expiry Date Cases"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "name1",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Vendor-wise Inventory Value Exposure"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "material_number",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Material-wise Missing Expiry Records"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "ekgrp",
                    "agg": "count",
                    "title": "Purchasing Group Analysis"
                }
            ]
        }
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company_code": ["Company Code"],
        "plant": ["Plant"],
        "vendor_account_number": ["Vendor Account Number"],
        "material_number": ["Material Number"],
        "batch_number": ["Batch Number"],
        "name1": ["NAME1"],
        "ekgrp": ["EKGRP"],
        "amount": ["Amount in Local Currency"],
        "quantity": ["Quantity"],
        # Helpers
        "message_row_id": ["Message Row ID"],
        "date": ["Posting Date in the Document"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Manufacturing_Efficiency"
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