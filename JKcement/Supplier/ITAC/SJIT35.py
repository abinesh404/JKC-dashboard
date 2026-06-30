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
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("GR & IR Configurations over Item Category Type are Configured Inappropriately"),
            "cards": [
                {
                    "id": "k1",
                    "label": "Item Categories",
                    "agg": "unique",
                    "source": "item_category"
                },
                {
                    "id": "k2",
                    "label": "Materials",
                    "agg": "unique",
                    "source": "material"
                },
                {
                    "id": "k3",
                    "label": "Account Assignment Categories",
                    "agg": "unique",
                    "source": "account_assignment"
                },
                {
                    "id": "k4",
                    "label": "Business Item Types",
                    "agg": "unique",
                    "source": "business_item_type"
                },
                {
                    "id": "k5",
                    "label": "GR Configuration Exceptions",
                    "agg": "row_count"
                },
                {
                    "id": "k6",
                    "label": "IR Configuration Exceptions",
                    "agg": "row_count"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Item Category", "source": "item_category"},
                {"id": "f2", "label": "Account Assignment Category", "source": "account_assignment"},
                {"id": "f3", "label": "Business Item Type", "source": "business_item_type"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "pie",
                    "x": "item_category",
                    "agg": "count",
                    "legend": True,
                    "top_n": 5,
                    "title": "Top Item Categories with Configuration Exceptions"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "account_assignment",
                    "agg": "count",
                    "horizontal": True,
                    "top_n": 5,
                    "title": "Account Assignment Category Distribution"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "gr_indicator",
                    "agg": "count",
                    "title": "GR Indicator Distribution"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "business_item_type",
                    "agg": "count",
                    "legend": True,
                    "top_n": 5,
                    "title": "Business Item Type Distribution"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "ir_indicator",
                    "agg": "count",
                    "title": "Invoice Receipt Indicator Analysis"
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": get_exception_title("GR & IR Configurations over Account Assignment Categories are Configured Inappropriately"),
            "cards": [
                {
                    "id": "k1",
                    "label": "Account Assignment Categories",
                    "agg": "unique",
                    "source": "account_assignment"
                },
                {
                    "id": "k2",
                    "label": "Item Categories",
                    "agg": "unique",
                    "source": "item_category"
                },
                {
                    "id": "k3",
                    "label": "Materials",
                    "agg": "unique",
                    "source": "material"
                },
                {
                    "id": "k4",
                    "label": "Business Item Types",
                    "agg": "unique",
                    "source": "business_item_type"
                },
                {
                    "id": "k5",
                    "label": "GR Configuration Exceptions",
                    "agg": "row_count"
                },
                {
                    "id": "k6",
                    "label": "IR Configuration Exceptions",
                    "agg": "row_count"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Account Assignment Category", "source": "account_assignment"},
                {"id": "f2", "label": "Item Category", "source": "item_category"},
                {"id": "f3", "label": "Business Item Type", "source": "business_item_type"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "pie",
                    "x": "account_assignment",
                    "agg": "count",
                    "legend": True,
                    "top_n": 5,
                    "title": "Top Account Assignment Categories with Configuration Exceptions"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "item_category",
                    "agg": "count",
                    "horizontal": True,
                    "top_n": 5,
                    "title": "Item Category Distribution"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "ir_binding_indicator_aa",
                    "agg": "count",
                    "title": "IR Binding Indicator Analysis"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "business_item_type",
                    "agg": "count",
                    "legend": True,
                    "top_n": 5,
                    "title": "Business Item Type Distribution"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "gr_indicator",
                    "agg": "count",
                    "title": "GR Indicator Analysis"
                }
            ]
        }
    ],
    "columns": {
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
        f"data_files/SJIT35_Exception0{exc_id}.csv",
        f"data_files/SJIT35_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
