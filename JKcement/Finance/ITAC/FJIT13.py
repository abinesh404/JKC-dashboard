# Finance/ITAC/FJIT13.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "FJIT13",
    "name": "Payment Has Been Made Against PO Without Adjusting Advance",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company_code": ["Company Code"],
        "vendor_code": ["Vendor Code"],
        "vendor_country": ["Vendor Country"],
        "currency": ["Currency"],
        "special_gl": ["Special_GL_Ind"],
        "fiscal_year": ["Fiscal Year"],
        "vendor_name": ["Vendor Name"],
        "company_name": ["Company"],
        "po_creator": ["PO Creator ID"],
        "po_number": ["PO_Number"],
        "mm_invoice": ["MM Invoice"],
        "fi_invoice": ["FI Invoice"],
        "advance_clearing_doc": ["Advance_Clearing_Doc"],
        "advance_amount": ["Advance_Amount_LC"],
        "gross_amount": ["MM_Gross_Amount"],
        "fi_amount": ["FI_Amount_LC"],
        "advance_date": ["Advance_Posting_Date"],
        "po_creation_date": ["PO Creation Date"],
        "date": ["Advance_Posting_Date"],
        # Helpers
        "advance_age_days": ["Advance Age Days"],
        "missing_clearing_doc_id": ["Missing Clearing Doc ID"],
        "open_advance_age": ["Open Advance Age"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "ITAC"
    }

def get_data(exc_id):
    paths = [
        rf"data_files/FJIT13_Exception{int(exc_id):02}.csv",
        rf"data_files/FJIT13_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None