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
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Purchase Documents Pertaining to Exception Item Categories for which GR Check is Not Defined in PO"),
            "cards": [
                {
                    "id": "k1",
                    "label": "Companies",
                    "agg": "unique",
                    "source": "company"
                },
                {
                    "id": "k2",
                    "label": "Plants",
                    "agg": "unique",
                    "source": "plant"
                },
                {
                    "id": "k3",
                    "label": "Vendors",
                    "agg": "unique",
                    "source": "vendor"
                },
                {
                    "id": "k4",
                    "label": "Purchase Documents",
                    "agg": "unique",
                    "source": "po"
                },
                {
                    "id": "k5",
                    "label": "Item Categories",
                    "agg": "unique",
                    "source": "item_category"
                },
                {
                    "id": "k6",
                    "label": "Materials",
                    "agg": "unique",
                    "source": "material"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Plant", "source": "plant"},
                {"id": "f3", "label": "Vendor", "source": "vendor"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "pie",
                    "x": "item_category",
                    "agg": "count",
                    "top_n": 5,
                    "title": "Top 5 Item Categories by Exception Count"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "vendor",
                    "agg": "count",
                    "top_n": 10,
                    "horizontal": True,
                    "title": "Top 10 Vendors by Exception Count"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Exception Trend"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "company",
                    "agg": "count",
                    "title": "Company-wise Exception Share"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "plant",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Top Plants by Exception Count"
                }
            ]
        }
    ],
    "columns": {
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
        f"data_files/SJIT31_Exception0{exc_id}.csv",
        f"data_files/SJIT31_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
