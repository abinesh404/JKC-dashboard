# Manufacturing/Others/MJOT11.py
import pandas as pd
import os

CONFIG = {
    "id": "MJOT11",
    "name": "Scrap Sales Procedure Audit",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "Same Plant Scrap Sales Pricing Deviation",
            "cards": [
                {"id": "k1", "label": "Scrap Sale Transactions", "agg": "unique", "source": "billing_doc_num"},
                {"id": "k2", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k3", "label": "Materials Impacted", "agg": "unique", "source": "material_number"},
                {"id": "k4", "label": "Total Scrap Sales Value", "agg": "total_value", "source": "net_lc", "format": "currency"},
                {"id": "k5", "label": "Total Price Impact", "agg": "total_value", "source": "impact", "format": "currency"},
                {"id": "k6", "label": "Average Variation %", "agg": "avg", "source": "variation_pct", "format": "percentage"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Material Number", "source": "material_number", "all_label": "All Materials"},
                {"id": "f4", "label": "Billing Month", "source": "billing_month", "all_label": "All Months"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "plant",
                    "y": "net_lc",
                    "agg": "sum",
                    "title": "Plant-wise Scrap Sales Value"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "material_number",
                    "y": "variation_pct",
                    "agg": "avg",
                    "top_n": 10,
                    "title": "Material-wise Price Variation"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "material_number",
                    "y": "net_value",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Top Scrap Materials by Revenue"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "billing_month",
                    "y": "net_lc",
                    "agg": "sum",
                    "title": "Monthly Scrap Sales Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "sold_to_party",
                    "y": "net_lc",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Customer-wise Scrap Sales Analysis"
                }
            ]
        }],
    "columns": {
        "exception_type": ["Exception Type"],
        "company_code": ["Company Code"],
        "plant": ["Plant"],
        "material_number": ["Material Number"],
        "sales_org": ["Sales Organization"],
        "billing_month": ["Billing Month"],
        "billing_doc_num": ["Billing Document Number"],
        "net_lc": ["Net_LC"],
        "net_value": ["Net Value"],
        "net_price_unit": ["Net_Price_Unit"],
        "price_diff": ["Price_Diff"],
        "impact": ["Impact"],
        "variation_pct": ["Variation_%"],
        "sold_to_party": ["Sold-to Party"],
        "date": ["Billing Date"]
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