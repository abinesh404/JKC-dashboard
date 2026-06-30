# Supplier/ITAC/SJIT36.py — Incorrect Message Type Configuration
# -----------------------------------------------------
# INSIGHT CONFIG — Pure "WHAT to show" (no logic)
# -----------------------------------------------------

import pandas as pd
import os

from ..procurement.template import get_chart_title, get_exception_title


CONFIG = {
    "id": "SJIT36",
    "name": "Incorrect Message Type Configuration",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": get_exception_title("Message Control Set to Warnings"),
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
                    "label": "Users",
                    "agg": "unique",
                    "source": "user"
                },
                {
                    "id": "k4",
                    "label": "Active Message Types",
                    "agg": "unique",
                    "source": "active_message_type"
                },
                {
                    "id": "k5",
                    "label": "Batch Input Message Types",
                    "agg": "unique",
                    "source": "batch_input_message_type"
                },
                {
                    "id": "k6",
                    "label": "Total Configuration Exceptions",
                    "agg": "row_count"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Application Area", "source": "application_area"},
                {"id": "f2", "label": "User Name", "source": "user"},
                {"id": "f3", "label": "Active Message Type", "source": "active_message_type"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "pie",
                    "x": "application_area",
                    "agg": "count",
                    "legend": True,
                    "top_n": 5,
                    "title": "Top Application Areas with Warning Messages"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "user",
                    "agg": "count",
                    "horizontal": True,
                    "top_n": 5,
                    "title": "Top Users with Warning Message Configuration"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "message_number",
                    "agg": "count",
                    "title": "Message Number Distribution"
                },
                {
                    "id": "c4",
                    "type": "doughnut",
                    "x": "active_message_type",
                    "agg": "count",
                    "legend": True,
                    "top_n": 5,
                    "title": "Active Message Type Distribution"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "batch_input_message_type",
                    "agg": "count",
                    "title": "Batch Input Handling Message Type Distribution"
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
        f"data_files/SJIT36_Exception0{exc_id}.csv",
        f"data_files/SJIT36_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
