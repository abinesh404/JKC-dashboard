# Supplier/invoice/SJIN29.py
import pandas as pd
import os

CONFIG = {
    "id": "SJIN29",
    "name": "Consumption Booked in Process Order After the GRN Date",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
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
        rf"data_files/SJIN29_Exception{int(exc_id):02}.csv",
        rf"data_files/SJIN29_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None