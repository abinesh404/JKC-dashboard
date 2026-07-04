# Customer/Sales/CJSA24.py — Timely manner of LR date and Invoice date
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJSA24",

    "name": "Timely manner of LR date and Invoice date",

    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")}
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "vendor": ["Vendor Code"],

        "invoice_doc": ["Invoice Document Number"],

        "po_number": ["Purchase Order Number"],

        "delivery": ["Delivery Number"],

        "delivery_item": ["Delivery Item"],

        "gross_amount": ["Gross Invoice Amount"],

        "vendor_name": ["Vendor Name"],

        "delivery_type": ["Delivery Type"],

        "days_diff": ["Days_Difference"],

        "material": ["Material"],

        "date": ["Invoice Date"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer Sales"
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
