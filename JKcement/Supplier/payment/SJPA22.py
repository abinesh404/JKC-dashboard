# Supplier/payment/SJPA22.py
import pandas as pd
import os
from .template import get_exception_title, get_chart_title

CONFIG = {
    "id": "SJPA22",
    "name": "Payment Released without Quality Clearance",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": [
            "Company Code",
            "Name of Company",
            "City",
            "Country Key"
        ],
        "company_name": [
            "Name of Company"
        ],
        "vendor": [
            "Vendor Account Number",
            "VAT Registration Number"
        ],
        "purchase_order": [
            "Purchasing Document Number",
            "Purchasing Document Type",
            "Purchasing Organization",
            "Purchasing Group",
            "Item Number of Purchasing Document"
        ],
        "purchasing_org": [
            "Purchasing Organization"
        ],
        "material": [
            "Material Number",
            "Short Text Material Description",
            "Plant"
        ],
        "plant": [
            "Plant"
        ],
        "quantity": [
            "Purchase Order Quantity",
            "Purchase Order Unit of Measure"
        ],
        "amount": [
            "Amount in Local Currency",
            "Net Value",
            "Net Price",
            "Amount in Document Currency",
            "Currency Key"
        ],
        "quality_inspection": [
            "Inspection Lot Number",
            "Catalog",
            "Usage Decision Code",
            "Usage Decision Has Been Made",
            "Date of Code Used for Usage Decision"
        ],
        "inspection_lot": [
            "Inspection Lot Number"
        ],
        "accounting": [
            "Accounting Document Number",
            "Document Number of the Clearing Document",
            "Document Type",
            "Fiscal Year",
            "Number of Line Item Within Accounting Document",
            "Terms of Payment Key",
            "Reversal Doc"
        ],
        "date": [
            "Clearing Date",
            "Purchasing Document Date",
            "Posting Date in the Document",
            "Day On Which Accounting Document Was Entered",
            "Date on Which the Data Record Was Created"
        ],
        "clearing_date": [
            "Clearing Date"
        ],
        "delay": [
            "Days_Difference (AUGDT – VDATUM)",
            "Days_Difference"
        ],
        "user": [
            "User Name"
        ],
        "exception": [
            "Exception"
        ]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Supplier Payment"
    }

def get_data(exc_id):
    paths = [
        rf"data_files/SJPA22_Exception{int(exc_id):02}.csv",
        rf"data_files/SJPA22_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None