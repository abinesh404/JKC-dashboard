# Supplier/ITAC/SJIT34.py — Automatic System Not Set Properly
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from ..procurement.template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJIT34",
    "name": "Automatic System Not Set Properly",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Automatic System Not Set Properly"),
            "cards": [
                {
                    "id": "k1",
                    "label": "Application Areas",
                    "agg": "unique",
                    "source": "application_area"
                },
                {
                    "id": "k2",
                    "label": "Message Numbers",
                    "agg": "unique",
                    "source": "message_number"
                },
                {
                    "id": "k3",
                    "label": "Allowed Message Types",
                    "agg": "unique",
                    "source": "allowed_message_type"
                },
                {
                    "id": "k4",
                    "label": "Standard Message Types",
                    "agg": "unique",
                    "source": "standard_message_type"
                },
                {
                    "id": "k5",
                    "label": "Switched-Off Messages",
                    "agg": "unique",
                    "source": "switch_off_message"
                },
                {
                    "id": "k6",
                    "label": "Total Exceptions",
                    "agg": "row_count"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Application Area", "source": "application_area"},
                {"id": "f2", "label": "Allowed Message Type", "source": "allowed_message_type"},
                {"id": "f3", "label": "Standard Message Type", "source": "standard_message_type"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "pie",
                    "x": "application_area",
                    "agg": "count",
                    "legend": True,
                    "top_n": 5,
                    "title": "Top Application Areas with Configuration Exceptions"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "message_number",
                    "agg": "count",
                    "horizontal": True,
                    "top_n": 5,
                    "title": "Message Number Distribution"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "allowed_message_type",
                    "agg": "count",
                    "title": "Allowed Message Type Distribution"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "standard_message_type",
                    "agg": "count",
                    "legend": True,
                    "top_n": 5,
                    "title": "Standard Message Type Distribution"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "switch_off_message",
                    "agg": "count",
                    "title": "Switched-Off Messages Analysis"
                }
            ]
        }
    ],
    "columns": {
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
        f"data_files/SJIT34_Exception0{exc_id}.csv",
        f"data_files/SJIT34_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
