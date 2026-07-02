# Supplier/ITAC/SJIT31.py — Purchase Documents Pertaining to Exception Item Categories with GR Check Not Defined in PO
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

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
    paths = [
        rf"data_files/SJIT31_Exception{int(exc_id):02}.csv",
        rf"data_files/SJIT31_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None