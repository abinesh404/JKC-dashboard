# Manufacturing/Production/MJPR7.py
import pandas as pd
import os

CONFIG = {
    "id": "MJPR7",
    "name": "Difference in Shelf Life",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "Shelf Life Inconsistency (Expiry or Shelf Life Mismatch)",
            "cards": [
                {"id": "k1", "label": "Shelf Life Exceptions", "agg": "unique", "source": "material_row_id"},
                {"id": "k2", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k3", "label": "Materials Impacted", "agg": "unique", "source": "material_number"},
                {"id": "k4", "label": "Expired Inventory Quantity", "agg": "total_value", "source": "expired_qty_helper"},
                {"id": "k5", "label": "Inventory Value at Risk", "agg": "total_value", "source": "val_at_risk_helper", "format": "currency"},
                {"id": "k6", "label": "Average Remaining Shelf Life Days", "agg": "avg", "source": "remaining_shelf_life_days"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Material Type", "source": "material_type", "all_label": "All Types"},
                {"id": "f4", "label": "Material Group", "source": "material_group", "all_label": "All Groups"},
                {"id": "f5", "label": "Storage Location", "source": "storage_location", "all_label": "All Locations"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "plant",
                    "agg": "count",
                    "title": "Plant-wise Shelf Life Exceptions"
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
                    "x": "remaining_shelf_life_days",
                    "agg": "count",
                    "title": "Remaining Shelf Life Distribution"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "date_of_expiry",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Expiry Trend Analysis"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "material_desc",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Inventory Value Exposure"
                }
            ]
        }],
    "columns": {
        "exception_type": ["Exception Type"],
        "company_code": ["Company Code"],
        "plant": ["Plant"],
        "material_type": ["Material Type"],
        "material_group": ["Material Group"],
        "storage_location": ["Storage Location"],
        "valuation_area": ["Valuation Area"],
        "material_number": ["Material Number"],
        "quantity": ["Quantity"],
        "amount": ["Amount in Local Currency"],
        "stock_value": ["STOCK_VALUE"],
        "total_val_stock": ["Total Valuated Stock"],
        "remaining_shelf_life_days": ["Remaining_Shelf_Life_Days"],
        "date_of_expiry": ["Date Of Expiry"],
        "material_desc": ["Material description"],
        "posting_date": ["Posting Date in the Document"],
        "date": ["Posting Date in the Document"],
        # Helpers
        "material_row_id": ["Material Row ID"],
        "expired_qty_helper": ["Expired Qty Helper"],
        "val_at_risk_helper": ["Val at Risk Helper"],
        "stock_value_per_unit": ["Stock Value per Unit"]
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