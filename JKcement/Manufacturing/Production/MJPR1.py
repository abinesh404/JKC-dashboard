# Manufacturing/Production/MJPR1.py
import pandas as pd
import os

CONFIG = {
    "id": "MJPR1",
    "name": "Inventory Valuation - Zero/Negative Stock Value",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "Materials with Stock Quantity > 0 but Stock Value <= 0",
            "cards": [
                {"id": "k1", "label": "Exception Materials", "agg": "unique", "source": "material_number"},
                {"id": "k2", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k3", "label": "Material Groups Impacted", "agg": "unique", "source": "material_group"},
                {"id": "k4", "label": "Total Stock Quantity", "agg": "total_value", "source": "quantity"},
                {"id": "k5", "label": "Total Negative/Zero Stock Value", "agg": "total_value", "source": "stock_value", "format": "currency"},
                {"id": "k6", "label": "Average Stock Value per Material", "agg": "avg", "source": "stock_value", "format": "currency"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f2", "label": "Material Type", "source": "material_type", "all_label": "All Types"},
                {"id": "f3", "label": "Material Group", "source": "material_group", "all_label": "All Groups"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "plant",
                    "y": "stock_value",
                    "agg": "sum",
                    "title": "Plant-wise Negative Inventory Value"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "material_group",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Material Group-wise Exception Analysis"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "material_type",
                    "agg": "count",
                    "title": "Material Type Distribution"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "posting_date",
                    "y": "stock_value",
                    "agg": "sum",
                    "time_group": "month",
                    "title": "Inventory Value Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "storage_location",
                    "y": "quantity",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Storage Location Exposure"
                }
            ]
        }
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "plant": ["Plant"],
        "material_type": ["Material Type"],
        "material_group": ["Material Group"],
        "material_number": ["Material Number"],
        "quantity": ["Quantity"],
        "stock_value": ["Stock_Value"],
        "posting_date": ["Posting Date in the Document"],
        "storage_location": ["Storage Location"],
        "date": ["Posting Date in the Document"]
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