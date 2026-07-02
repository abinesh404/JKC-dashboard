# Supplier/master_data/SJMA45.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJMA45",
    "name": "Variation in Payment terms in Invoice vs Masters",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Name", "Company Code"],
        "company_name": ["Company Name"],
        "customer": ["Customer Name", "Customer Number"],
        "customer_name": ["Customer Name"],
        "billing_doc": ["Billing Document"],
        "amount": ["Amount in Local Currency"],
        "overdue_days": ["Overdue_Days"],
        "pay_terms_inv": ["Terms of Payment Key (Invoice)"],
        "ageing_bracket": ["Ageing Bracket"],
        "payment_date": ["Payment Date"],
        "date": ["Payment Date", "Clearing Date", "Baseline Date for Due Date Calculation", "Net Due Date", "Net Due Date as per Customer Master"],
        "user": ["Name of Person who Created the Object"],
        "document": ["Accounting Document Number", "Billing Document"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Supplier Master Data"
    }

def get_data(exc_id):
    paths = [
        rf"data_files/SJMA45_Exception{int(exc_id):02}.csv",
        rf"data_files/SJMA45_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
