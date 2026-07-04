# Customer/ITAC/CJIT7.py — Manual price entry
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJIT7",

    "name": "Manual price entry",

    "active_exceptions": [

        {
            "id": "1",

            "label": "All Exceptions",

            "title": get_exception_title("Manual price entry"),

            "cards": [

                {"id": "k1", "label": "Total Value", "agg": "total_value", "source": "amount", "format": "currency"},

                {"id": "k2", "label": "Exceptions", "agg": "row_count"},

                {"id": "k3", "label": "Unique Condition Types", "agg": "unique", "source": "condition"},

                {"id": "k4", "label": "Avg Impact", "agg": "avg", "source": "amount"},

                {"id": "k5", "label": "Max Deviation", "agg": "max", "source": "amount"},

                {"id": "k6", "label": "Total Base Records", "agg": "row_count"}
            ],

            "filters": [
                {"id": "f1", "label": "Sales Organisation", "source": "sales_org"},

                {"id": "f2", "label": "Pricing Procedure", "source": "pricing"},

                {"id": "f3", "label": "Usage", "source": "usage"}
            ],

            "charts": [

                {"id": "c1", "type": "doughnut", "x": "sales_org", "agg": "count", "title": get_chart_title("Split by Sales Organisation")},

                {"id": "c2", "type": "bar", "x": "condition", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": get_chart_title("Top Condition Types", "Amount")},

                {"id": "c3", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": get_chart_title("Timeline Trend")},

                {"id": "c4", "type": "bar", "x": "pricing", "agg": "count", "top_n": 10, "title": get_chart_title("Distribution", "Pricing Procedure")}
            ]
        }
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "sales_org": ["Sales Organisation"],

        "pricing": ["Pricing Procedure"],

        "usage": ["Usage"],

        "condition": ["Condition Type Description"],

        "amount": ["Step Number"],

        "date": ["Date"]
    }
}


def meta():

    return {

        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Customer ITAC"
    }


def get_data(exc_id):
    insight_id = CONFIG["id"]
    import re
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
            df['Exception Type'] = f"Exception {i}"
            merged_df = pd.concat([merged_df, df], ignore_index=True)
    if not file_found:
        return None
    return merged_df