# Supplier/procurement/SJPR5.py — Single Source Vendors
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJPR5",
    "name": "Single Source Vendors",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": [
            "Company Code",
            "Company Name",
            "Company City"
        ],
        "company_name": [
            "Company Name"
        ],
        "plant": [
            "Plant Code",
            "Plant Name",
            "Plant City"
        ],
        "plant_name": [
            "Plant Name"
        ],
        "vendor": [
            "Vendor Code",
            "Vendor Name",
            "Vendor City"
        ],
        "material": [
            "Material Number",
            "Material Type",
            "Material Group",
            "Material Description"
        ],
        "material_group": [
            "Material Group"
        ],
        "qty": [
            "Purchase Order Quantity"
        ],
        "amount": [
            "Net Price in Purchasing Document (in Document Currency)"
        ],
        "po": [
            "Purchasing Document Number",
            "Item Number of Purchasing Document",
            "Purchasing Document Type",
            "Purchasing Document Category"
        ],
        "date": [
            "Purchasing Document Date"
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
