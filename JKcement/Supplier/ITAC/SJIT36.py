# Supplier/ITAC/SJIT36.py — Incorrect Message Type Configuration
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from ..procurement.template import get_chart_title, get_exception_title
from .template import get_exception_title


CONFIG = {
    "id": "SJIT36",
    "name": "Incorrect Message Type Configuration",
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
        "user": [
            "User Name"
        ],
        "active_message_type": [
            "Active message type"
        ],
        "batch_input_message_type": [
            "Message Type (Batch Input Handling)"
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
        rf"data_files/SJIT36_Exception{int(exc_id):02}.csv",
        rf"data_files/SJIT36_Exception{int(exc_id)}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if path:
        return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
    return None