# Supplier/master_data/SJMA14.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJMA14",
    "name": "Vendor Details Matching with Employees",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")},
        {"id": "3", "label": "Exception 03", "title": get_exception_title("Exception 03")},
        {"id": "4", "label": "Exception 04", "title": get_exception_title("Exception 04")},
        {"id": "5", "label": "Exception 05", "title": get_exception_title("Exception 05")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "vendor": [
            "Vendor code",
            "Vendor_Name",
            "Vendor Name 1",
            "Vendor Name 2"
        ],
        "employee": [
            "Employee code",
            "Employee_Name",
            "Employee Name 1",
            "Employee Name 2"
        ],
        "vendor_country": [
            "Vendor Country"
        ],
        "employee_country": [
            "Employee Country"
        ],
        "vendor_city": [
            "Vendor City"
        ],
        "location": [
            "Vendor Country",
            "Vendor City",
            "Vendor District",
            "Employee Country",
            "Employee City",
            "Employee District"
        ],
        "address": [
            "Vendor_address",
            "Employee_address",
            "Vendor Street",
            "Employee Street"
        ],
        "pan": [
            "Vendor_PAN",
            "Employee_PAN"
        ],
        "bank": [
            "Vendor Bank Account",
            "Employee Bank Account"
        ],
        "vendor_bank_country": [
            "Vendor Bank Country"
        ],
        "employee_bank_country": [
            "Employee Bank Country"
        ],
        "vendor_bank_key": [
            "Vendor  Bank Key",
            "Vendor Bank Key"
        ],
        "gst": [
            "GST_Vendor",
            "GST_Employee"
        ],
        "vendor_created_by": [
            "Vendor Created by"
        ],
        "user": [
            "Vendor Created by",
            "Employee Created by"
        ],
        "vendor_acct_grp": [
            "Vendor Account group"
        ],
        "account_group": [
            "Vendor Account group",
            "Employee Account group"
        ],
        "vendor_created_on": [
            "Vendor Created on"
        ],
        "date": [
            "Vendor Created on",
            "Employee Created on"
        ],
        "remark": [
            "Remark"
        ]
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
        rf"data_files/SJMA14_Exception{int(exc_id):02}.csv",
        rf"data_files/SJMA14_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None
