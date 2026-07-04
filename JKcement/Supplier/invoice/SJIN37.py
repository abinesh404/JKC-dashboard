# Supplier/invoice/SJIN37.py
import pandas as pd
import os
from .template import get_exception_title

CONFIG = {
    "id": "SJIN37",
    "name": "Duplicate Vendor Invoices - I",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")},
        {"id": "3", "label": "Exception 03", "title": get_exception_title("Exception 03")},
        {"id": "4", "label": "Exception 04", "title": get_exception_title("Exception 04")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": ["Company Name", "Company Code"],
        "vendor": ["Vendor Name1", "Vendor"],
        "pan": ["Pan Number"],
        "amount": ["Amount"],
        "region": ["REGION"],
        "country": ["Country"],
        "payment_method": ["Payment method"],
        "user_name": ["User Name"],
        "doc_type": ["Document Type", "Document type"],
        "date": ["Posting Date"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Supplier Invoice"
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
