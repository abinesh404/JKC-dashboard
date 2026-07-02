# Customer/Sales/CJSA28.py — Manual Intervention
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJSA28",

    "name": "Manual Intervention",

    "active_exceptions": [

        {
            "id": "1",

            "label": "All Exceptions",

            "title": get_exception_title("Manual Intervention"),

            "cards": [

                {"id": "k1", "label": "Company Code", "agg": "unique", "source": "company"},

                {"id": "k2", "label": "Billing Document", "agg": "unique", "source": "billing_doc"},

                {"id": "k3", "label": "Material", "agg": "unique", "source": "material"},

                {"id": "k4", "label": "Plant", "agg": "unique", "source": "plant"},

                {"id": "k5", "label": "User Count", "agg": "unique", "source": "user"},

                {"id": "k6", "label": "Impact", "agg": "sum", "source": "impact", "format": "currency"}
            ],

            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},

                {"id": "f1", "label": "User Name", "source": "user"},

                {"id": "f2", "label": "Billing Type", "source": "billing_type"},

                {"id": "f3", "label": "Material Description", "source": "material_desc"},

                {"id": "f4", "label": "Created On", "source": "date"}
            ],

            "charts": [

                {"id": "c1", "type": "bar", "x": "user", "y": "impact", "agg": "sum", "top_n": 10, "title": get_chart_title("User", "Impact")},

                {"id": "c2", "type": "pie", "x": "billing_type", "y": "billing_doc", "agg": "count", "title": get_chart_title("Billing Type", "Billing Docs")},

                {"id": "c3", "type": "line", "x": "date", "y": "impact", "agg": "sum", "time_group": "month", "title": get_chart_title("Created On", "Impact Trend")},

                {"id": "c4", "type": "doughnut", "x": "plant", "y": "impact", "agg": "sum", "title": get_chart_title("Plant", "Impact")},

                {"id": "c5", "type": "bar", "x": "material_desc", "y": "impact", "agg": "sum", "horizontal": True, "top_n": 10, "title": get_chart_title("Material", "Impact")}
            ]
        }
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "company": ["Company Code"],

        "billing_doc": ["Billing Document"],

        "material": ["Material"],

        "plant": ["Plant"],

        "user": ["User Name"],

        "impact": ["Impact"],

        "billing_type": ["Billing Type"],

        "material_desc": ["Material Description"],

        "date": ["Created On"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer Sales"
    }


def get_data(exc_id):
    insight_id = CONFIG["id"]
    merged_df = pd.DataFrame()
    for i in range(1, 10):
        path1 = f"data_files/{insight_id}_Exception0{i}.csv"
        path2 = f"data_files/{insight_id}_Exception{i}.csv"
        path = next((p for p in [path1, path2] if os.path.exists(p)), None)
        if path:
            df = pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
            df['Exception Type'] = f"Exception {i}"
            merged_df = pd.concat([merged_df, df], ignore_index=True)
    if merged_df.empty:
        return None
    return merged_df