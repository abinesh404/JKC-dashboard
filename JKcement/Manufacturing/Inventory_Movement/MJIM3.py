# Manufacturing/Inventory_Movement/MJIM3.py
import pandas as pd
import os

CONFIG = {
    "id": "MJIM3",
    "name": "Lack of QA Testing",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "No Inspection Lot Was Created for the Original Document",
            "cards": [
                {"id": "k1", "label": "Materials Without QA Inspection", "agg": "unique", "source": "material_number"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k4", "label": "Total Inventory Value", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Total Quantity Without QA", "agg": "total_value", "source": "quantity"},
                {"id": "k6", "label": "Batches Without Inspection Lot", "agg": "unique", "source": "batch_number"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Material Number", "source": "material_number", "all_label": "All Materials"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "company_name",
                    "agg": "count",
                    "title": "Company-wise QA Exceptions"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "material_number",
                    "y": "amount",
                    "agg": "sum",
                    "horizontal": True,
                    "top_n": 10,
                    "title": "Top Materials Without QA Testing"
                },
                {
                    "id": "c3",
                    "type": "doughnut",
                    "x": "plant",
                    "agg": "count",
                    "legend": True,
                    "title": "Plant-wise QA Exception Distribution"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "manufacture_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly QA Exception Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "movement_type",
                    "agg": "count",
                    "title": "Movement Type Analysis"
                }
            ]
        }
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company_code": ["Company Code"],
        "company_name": ["Company Name"],
        "plant": ["Plant"],
        "material_number": ["Material Number"],
        "batch_number": ["Batch Number"],
        "amount": ["Amount"],
        "quantity": ["Quantity"],
        "manufacture_date": ["Manufacture Date"],
        "movement_type": ["Movement Type"],
        "date": ["Manufacture Date"]
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