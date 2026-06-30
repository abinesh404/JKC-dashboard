# Supplier/invoice/SJIN29.py
import pandas as pd
import os

CONFIG = {
    "id": "SJIN29",
    "name": "Consumption Booked in Process Order After the GRN Date",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Cases Where Consumption Was Booked After GRN Date",
            "cards": [
                {"id": "k1", "label": "Exception Transactions", "agg": "total_rows"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k4", "label": "Total GRN Amount", "agg": "sum", "source": "grn_amount", "format": "currency"},
                {"id": "k5", "label": "Total Consumption Amount", "agg": "sum", "source": "consumption_amount", "format": "currency"},
                {"id": "k6", "label": "Average Delay Days (Consumption Date - GRN Date)", "agg": "avg", "source": "delay_days"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Material Number", "source": "material", "all_label": "All Materials"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise Delayed Consumption"},
                {"id": "c2", "type": "bar", "x": "material", "y": "consumption_amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Materials by Consumption Amount"},
                {"id": "c3", "type": "doughnut", "x": "plant", "agg": "count", "title": "Plant-wise Exception Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "posting_date_consumption", "agg": "count", "time_group": "month", "title": "Monthly Consumption Delay Trend"},
                {"id": "c5", "type": "bar", "x": "cost_center", "y": "consumption_amount", "agg": "sum", "title": "Cost Center-wise Consumption Amount"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Name", "Company Code"],
        "plant": ["Plant"],
        "material": ["Material Number"],
        "grn_amount": ["GRN Amount"],
        "consumption_amount": ["Consumption_Amount"],
        "delay_days": ["delay_days"],
        "cost_center": ["Cost Center"],
        "date": ["Posting Date_Consumption"],
        "posting_date_consumption": ["Posting Date_Consumption"],
        "amount": ["Consumption_Amount"]
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
        f"data_files/SJIN29_Exception0{exc_id}.csv",
        f"data_files/SJIN29_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    
    # Calculate Delay Days
    if 'Posting Date_Consumption' in df.columns and 'Posting Date_GRN' in df.columns:
        p_cons = pd.to_datetime(df['Posting Date_Consumption'], errors='coerce')
        p_grn = pd.to_datetime(df['Posting Date_GRN'], errors='coerce')
        df['delay_days'] = (p_cons - p_grn).dt.days.fillna(0).astype(int)
    else:
        df['delay_days'] = 0
        
    return df.fillna('')
