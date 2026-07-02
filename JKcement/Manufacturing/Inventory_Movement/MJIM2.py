# Manufacturing/Inventory_Movement/MJIM2.py
import pandas as pd
import os

CONFIG = {
    "id": "MJIM2",
    "name": "Idle Inventory Ageing at Source Batch Level",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "Batches Idle More Than 90 Days (Idle Days > 90)",
            "cards": [
                {"id": "k1", "label": "Idle Batches (>90 Days)", "agg": "unique", "source": "batch_number"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k4", "label": "Total Inventory Value", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Total Idle Quantity", "agg": "total_value", "source": "quantity"},
                {"id": "k6", "label": "Average Idle Days", "agg": "avg", "source": "idle_days"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Material Group", "source": "material_group", "all_label": "All Groups"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "company_code",
                    "y": "amount",
                    "agg": "sum",
                    "title": "Company-wise Idle Inventory Value"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "material_number",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Top Materials by Idle Inventory Value"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "ageing_bucket",
                    "agg": "count",
                    "title": "Ageing Bucket Distribution"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "plant",
                    "y": "quantity",
                    "agg": "sum",
                    "title": "Plant-wise Idle Inventory"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "storage_location",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Storage Location Analysis"
                }
            ]
        }],
    "columns": {
        "exception_type": ["Exception Type"],
        "company_code": ["Company Code"],
        "material_number": ["Material Number"],
        "material_group": ["Material Group"],
        "batch_number": ["Batch Number"],
        "quantity": ["Quantity"],
        "plant": ["Plant"],
        "storage_location": ["Storage Location"],
        "warehouse_storage_condition": ["Warehouse Storage Condition"],
        "amount": ["Amount in Local Currency"],
        "idle_days": ["Idle_Days"],
        "ageing_bucket": ["Ageing_Bucket"],
        "date": ["Posting Date in the Document"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Inventory_Movement"
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