# Supplier/ITAC/SJIT31.py — Purchase Documents Pertaining to Exception Item Categories with GR Check Not Defined in PO
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os
from .template import get_exception_title

from ..procurement.template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJIT31",
    "name": "Purchase Documents Pertaining to Exception Item Categories with GR Check Not Defined in PO",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company": [
            "Company code"
        ],
        "plant": [
            "Plant"
        ],
        "vendor": [
            "Vendor"
        ],
        "po": [
            "Purchasing Document Number",
            "EBELP",
            "Document category",
            "PO Type"
        ],
        "material": [
            "Material Number"
        ],
        "item_category": [
            "Item Category",
            "Text for Item Cat.",
            "PSTYP",
            "Business Item Type",
            "Status field for item category"
        ],
        "account_assignment": [
            "Account Assignment Category",
            "AcctAssgntCateg Desc",
            "Account assignment category usage",
            "Account assignment mandatory indicator",
            "Account assignment type allowed"
        ],
        "gr_ir_indicators": [
            "Goods Receipt indicator",
            "GR binding indicator",
            "GR non-valuated indicator",
            "GR non-valuated indicator for consignment",
            "Invoice Receipt indicator",
            "IR binding indicator",
            "Invoice update indicator",
            "Non-valuated GR indicator",
            "Delivery costs indicator",
            "Valuation relevant indicator",
            "Commitment relevance indicator"
        ],
        "control_indicators": [
            "Consumption posting indicator",
            "Special stock indicator",
            "Collective number indicator",
            "Tax code indicator",
            "Order acknowledgment requirement indicator",
            "DIFF_INVOICE"
        ],
        "status": [
            "Deletion Indicator",
            "Item Status"
        ],
        "date": [
            "change date"
        ]
    }
}


def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Supplier ITAC"
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
