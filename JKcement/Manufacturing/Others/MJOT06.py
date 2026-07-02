# Manufacturing/Others/MJOT06.py
import pandas as pd
import os

CONFIG = {
    "id": "MJOT06",
    "name": "Actual Yield Loss vis-a-vis Standard Yield Loss",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "Actual Yield Loss Exceeds Standard Yield Loss Percentage",
            "cards": [
                {"id": "k1", "label": "Production Orders with Yield Loss", "agg": "unique", "source": "order_number"},
                {"id": "k2", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k3", "label": "Work Centers Impacted", "agg": "unique", "source": "work_center_id"},
                {"id": "k4", "label": "Total Planned Output Quantity", "agg": "total_value", "source": "planned_qty"},
                {"id": "k5", "label": "Total Actual Yield Quantity", "agg": "total_value", "source": "actual_yield"},
                {"id": "k6", "label": "Average Yield Loss %", "agg": "avg", "source": "actual_loss_percent"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f2", "label": "Work Center ID", "source": "work_center_id", "all_label": "All Work Centers"},
                {"id": "f3", "label": "MRP Controller", "source": "mrp_controller", "all_label": "All Controllers"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "plant",
                    "y": "actual_loss_percent",
                    "agg": "avg",
                    "title": "Plant-wise Yield Loss Analysis"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "work_center_id",
                    "y": "actual_loss_percent",
                    "agg": "avg",
                    "top_n": 10,
                    "title": "Work Center-wise Yield Loss"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "material_number",
                    "y": "actual_loss_percent",
                    "agg": "avg",
                    "top_n": 10,
                    "title": "Material-wise Yield Loss"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "posting_date",
                    "y": "actual_yield_percent",
                    "agg": "avg",
                    "time_group": "month",
                    "title": "Production Trend Analysis"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "mrp_controller",
                    "y": "yield_variance",
                    "agg": "avg",
                    "title": "MRP Controller-wise Yield Variance"
                }
            ]
        }
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "plant": ["Plant"],
        "work_center_id": ["Work Center ID"],
        "mrp_controller": ["MRP Controller"],
        "order_number": ["Order Number"],
        "planned_qty": ["Planned output quantity"],
        "actual_yield": ["Actual yield (confirmed)"],
        "actual_loss_percent": ["Actual_Loss_Percent"],
        "actual_yield_percent": ["Actual_Yield_Percent"],
        "yield_variance": ["Yield Variance"],
        "material_number": ["Material Number"],
        "posting_date": ["Posting Date"],
        "date": ["Posting Date"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Others"
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