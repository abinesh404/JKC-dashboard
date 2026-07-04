# Customer/MasterData/CJMA15.py — Vendor To Customer setoff
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJMA15",

    "name": "Vendor To Customer setoff",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "vendor": ["Vendor Number"],

        "clearing_doc": ["Clearing Document Number"],

        "company": ["Company Code"],

        "customer": ["Customer Number"],

        "customer_amount": ["Customer Amount"],

        "vendor_amount": ["Vendor Amount"],

        "vendor_name": ["Vendor Name"],

        "clearing_key": ["CLEARING_KEY"],

        "customer_name": ["Customer Name"],

        "doc_type": ["Document Type_Vendor"],

        "city": ["City"],

        "date": ["Clearing Date_Vendor"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer Master Data"
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
