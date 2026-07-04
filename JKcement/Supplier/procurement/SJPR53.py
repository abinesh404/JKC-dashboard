# Supplier/procurement/SJPR53.py — Same Transaction & Group PO and Non-PO Invoices Raised
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR53",
    "name": "Same Transaction & Group PO and Non-PO Invoices Raised",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": [
            "Company Code",
            "Company Description",
            "Company City"
        ],
        "company_desc": [
            "Company Description"
        ],
        "plant": [
            "Plant Code",
            "Plant Name"
        ],
        "vendor": [
            "Vendor Code"
        ],
        "invoice": [
            "Accounting document Number",
            "Fiscal Year",
            "Document Type"
        ],
        "po": [
            "Purchasing Organization",
            "Purchasing Document Number",
            "Item Number of Purchasing Document"
        ],
        "purch_org": [
            "Purchasing Organization"
        ],
        "gl": [
            "General Ledger Account",
            "G/L Account Number",
            "G/L Account Group",
            "G/L Account Long Text",
            "G/L Acct Long Text",
            "G/L Long Text",
            "GLACCOUNT_TYPE",
            "GLACCOUNT_SUBTYPE",
            "Derived_GL",
            "Cost Element"
        ],
        "gl_group": [
            "G/L Account Group"
        ],
        "gl_desc": [
            "G/L Account Long Text",
            "G/L Acct Long Text",
            "G/L Long Text"
        ],
        "amount": [
            "Amount in Local Currency"
        ],
        "date": [
            "Document Date in Document",
            "Posting Date in the Document",
            "Clearing Date"
        ],
        "posting_date": [
            "Posting Date in the Document"
        ],
        "user": [
            "User Name",
            "Name of Person who Created the Object"
        ],
        "item_details": [
            "Item Text",
            "Posting Key",
            "Number of Line Item Within Accounting Document",
            "Account Type",
            "DR/CR Indicator"
        ],
        "search_key": [
            "Search Term for Using Matchcode"
        ]
    }
}


def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Supplier Procurement"
    }


def get_data(exc_id):
    insight_id = CONFIG["id"]
    import re
    import pandas as pd
    m = re.search(r'([A-Za-z]+)(\d+)', insight_id)
    padded_id = f"{m.group(1)}0{m.group(2)}" if m and len(m.group(2)) == 1 else insight_id
    merged_df = pd.DataFrame()
    file_found = False
    for i in range(1, 10):
        paths = [
            f"data_files/{insight_id}_Exception0{i}.csv",
            f"data_files/{insight_id}_Exception{i}.csv",
            f"data_files/{padded_id}_Exception0{i}.csv",
            f"data_files/{padded_id}_Exception{i}.csv"
        ]
        path = next((p for p in paths if os.path.exists(p)), None)
        if path:
            file_found = True
            df = pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
            df['Exception Type'] = f"Exception {i:02}"
            merged_df = pd.concat([merged_df, df], ignore_index=True)
    if not file_found:
        return None
    return merged_df
