# Supplier/master_data/SJMA16.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJMA16",
    "name": "Vendor Name and Customer Name is Same",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")},
        {"id": "3", "label": "Exception 03", "title": get_exception_title("Exception 03")},
        {"id": "4", "label": "Exception 04", "title": get_exception_title("Exception 04")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Code_Cus", "Company Code_ven", "Company Code_Ven", "Customer code_ven"],
        "company_cus": ["Company Code_Cus"],
        "company_ven": ["Company Code_ven", "Company Code_Ven", "Customer code_ven"],
        "region": ["Region"],
        "currency": ["Currency Key"],
        "amount": ["Amount in Local Currency"],
        "amount_doc": ["Amount in document currency"],
        "vendor": ["Account Number of Vendor or Creditor"],
        "vendor_name": ["NAME1_Vendor"],
        "customer": ["Customer Number"],
        "customer_name": ["NAME1_Customer"],
        "date": ["Posting Date in the Document"],
        "doc_num": ["Accounting Document Number"],
        "payment_terms": ["Terms of Payment Key"],
        "posting_block_ven": ["Posting block for company code_Ven", "Posting Block for Company Code"],
        "cust_company_count": ["Cust_Company_Count"],
        "vend_company_count": ["Vend_Company_Count"]
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
        rf"data_files/SJMA16_Exception{int(exc_id):02}.csv",
        rf"data_files/SJMA16_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
