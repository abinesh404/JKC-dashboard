# Customer/ITAC/CJIT3.py — Credit sales exceeding limit
# -----------------------------------------------------

import pandas as pd
import os

from .template import get_chart_title, get_exception_title


CONFIG = {

    "id": "CJIT3",

    "name": "Credit sales exceeding limit",

    "active_exceptions": [

        {
            "id": "1",

            "label": "All Exceptions",

            "title": get_exception_title("Credit sales exceeding limit"),

            "cards": [

                {"id": "k1", "label": "Total Value", "agg": "total_value", "source": "amount", "format": "currency"},

                {"id": "k2", "label": "Exceptions", "agg": "row_count"},

                {"id": "k3", "label": "Unique Customers", "agg": "unique", "source": "customer"},

                {"id": "k4", "label": "Avg Impact", "agg": "avg", "source": "amount"},

                {"id": "k5", "label": "Max Deviation", "agg": "max", "source": "amount"},

                {"id": "k6", "label": "Total Base Records", "agg": "row_count"}
            ],

            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},

                {"id": "f1", "label": "Country", "source": "country"},

                {"id": "f2", "label": "Region", "source": "region"},

                {"id": "f3", "label": "CCA Description", "source": "cca"}
            ],

            "charts": [

                {"id": "c1", "type": "doughnut", "x": "country", "agg": "count", "title": get_chart_title("Split by Country")},

                {"id": "c2", "type": "bar", "x": "customer", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": get_chart_title("Top Violators", "Customer")},

                {"id": "c3", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": get_chart_title("Timeline Trend")},

                {"id": "c4", "type": "bar", "x": "region", "agg": "count", "top_n": 10, "title": get_chart_title("Distribution", "Region")}
            ]
        }
    ],

    "columns": {
        "exception_type": ["Exception Type"],

        "country": ["country_key"],

        "region": ["region"],

        "cca": ["cca_description"],

        "customer": ["name1"],

        "amount": ["tot_receivables"],

        "date": ["Posting Date"]
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