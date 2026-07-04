# Supplier/ITAC/SJIT34.py — Automatic System Not Set Properly
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from ..procurement.template import get_chart_title, get_exception_title
from .template import get_exception_title


CONFIG = {
    "id": "SJIT34",
    "name": "Automatic System Not Set Properly",
    "active_exceptions": [
        {"id": "1", "label": "Exception 01", "title": get_exception_title("Exception 01")}
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "application_area": [
            "Application Area"
        ],
        "message_number": [
            "Message number"
        ],
        "allowed_message_type": [
            "Allowed message types"
        ],
        "standard_message_type": [
            "Standard message type"
        ],
        "switch_off_message": [
            "Switch off message"
        ],
        "status": [
            "STATUS"
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
        rf"data_files/SJIT34_Exception{int(exc_id):02}.csv",
        rf"data_files/SJIT34_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None