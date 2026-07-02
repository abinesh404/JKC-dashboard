# Taxation/GST/TJGS4.py
import pandas as pd
import os

CONFIG = {
    "id": "TJGS4",
    "name": "GST Duplicate Invoices",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "GST Duplicate Invoices",
            "cards": [
                {"id": "k1", "label": "Duplicate GST Invoices", "agg": "unique", "source": "doc_no"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "rec_co_code"},
                {"id": "k3", "label": "Users Involved", "agg": "unique", "source": "user_name"},
                {"id": "k4", "label": "Duplicate Invoice Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Reversed Duplicate Invoices", "agg": "unique", "source": "reversed_dup_invoices"},
                {"id": "k6", "label": "Open Duplicate Invoices", "agg": "unique", "source": "open_dup_invoices"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "Fiscal Year", "source": "fiscal_year", "all_label": "All Years"},
                {"id": "f2", "label": "User Name", "source": "user_name", "all_label": "All Users"},
                {"id": "f3", "label": "Currency", "source": "currency", "all_label": "All Currencies"},
                {"id": "f4", "label": "Document Type", "source": "type", "all_label": "All Types"},
                {"id": "f5", "label": "Reversal Flag", "source": "reversal_flag", "all_label": "All Statuses"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "fiscal_year",
                    "agg": "count",
                    "title": "Fiscal Year-wise Duplicate Invoices"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "user_name",
                    "agg": "count",
                    "top_n": 10,
                    "title": "User-wise Duplicate Invoice Posting"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "days_difference",
                    "agg": "count",
                    "title": "Duplicate Invoice Age Analysis"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "pstng_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Duplicate Invoice Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "reversal_flag",
                    "agg": "count",
                    "title": "Reversal Status Analysis"
                }
            ]
        }
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "fiscal_year": ["Fiscal Year"],
        "user_name": ["User Name"],
        "currency": ["currency"],
        "type": ["Type"],
        "reversal_flag": ["Reversal Flag"],
        "doc_no": ["Doc No"],
        "rec_co_code": ["Rec Co Code"],
        "days_difference": ["Days_Difference"],
        "pstng_date": ["Pstng Date"],
        "date": ["Pstng Date"],
        "amount": ["Amount"],
        # Helpers
        "reversed_dup_invoices": ["Reversed Dup Invoices"],
        "open_dup_invoices": ["Open Dup Invoices"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "GST"
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