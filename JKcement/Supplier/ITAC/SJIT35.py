# Supplier/ITAC/SJIT35.py — GR & IR Configurations over Item and Account Assignment Categories are Configured Inappropriately
# ---------------------------------------------------------------------------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# ---------------------------------------------------------------------------------------------------------------------

import pandas as pd
import os

from ..procurement.template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJIT35",
    "name": "GR & IR Configurations over Item and Account Assignment Categories are Configured Inappropriately",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")},
        {"id": "2", "label": "Exception 02", "title": get_exception_title("Exception 02")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "item_category": [
            "Item Category",
            "Text for Item Cat.",
            "Status field for item category"
        ],
        "material": [
            "Material Number"
        ],
        "account_assignment": [
            "Account Assignment Category",
            "AcctAssgntCateg Desc",
            "Account assignment category usage",
            "Account assignment mandatory indicator",
            "Account assignment type allowed"
        ],
        "gr_indicator": [
            "Goods Receipt indicator"
        ],
        "gr_binding_indicator_item_cat": [
            "GR binding indicator_Item Category"
        ],
        "gr_binding_indicator_aa": [
            "GR binding indicator_Account Assignment Categories"
        ],
        "gr_non_val_indicator": [
            "GR non-valuated indicator"
        ],
        "gr_non_val_indicator_consignment": [
            "GR non-valuated indicator for consignment"
        ],
        "non_val_gr_indicator": [
            "Non-valuated GR indicator"
        ],
        "ir_indicator": [
            "Invoice Receipt indicator"
        ],
        "invoice_update_indicator": [
            "Invoice update indicator"
        ],
        "ir_binding_indicator": [
            "IR binding indicator"
        ],
        "ir_binding_indicator_item_cat": [
            "IR binding indicator_Item Category"
        ],
        "ir_binding_indicator_aa": [
            "IR binding indicator_Account Assignment Categories"
        ],
        "business_item_type": [
            "Business Item Type"
        ],
        "consumption_posting_indicator": [
            "Consumption posting indicator"
        ],
        "commitment_relevance_indicator": [
            "Commitment relevance indicator"
        ],
        "special_stock_indicator": [
            "Special stock indicator"
        ],
        "collective_number_indicator": [
            "Collective number indicator"
        ],
        "tax_code_indicator": [
            "Tax code indicator"
        ],
        "delivery_costs_indicator": [
            "Delivery costs indicator"
        ],
        "valuation_relevant_indicator": [
            "Valuation relevant indicator"
        ],
        "order_acknowledgment_requirement_indicator": [
            "Order acknowledgment requirement indicator"
        ],
        "diff_invoice": [
            "DIFF_INVOICE"
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
        rf"data_files/SJIT35_Exception{int(exc_id):02}.csv",
        rf"data_files/SJIT35_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None