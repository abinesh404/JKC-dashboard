# Taxation/GST/TJGS1.py
import pandas as pd
import os

CONFIG = {
    "id": "TJGS1",
    "name": "GST - Identify Instances Where Payment Made Beyond 180 Days from Invoice Date",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "Instances Where Payment Has Been Made After 180 Days from the Invoice Date and Resultant Interest Loss on GST",
            "cards": [
                {"id": "k1", "label": "Delayed GST Payments", "agg": "unique", "source": "accounting_document_number"},
                {"id": "k2", "label": "Vendors Impacted", "agg": "unique", "source": "vendor"},
                {"id": "k3", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k4", "label": "Total GST Amount", "agg": "total_value", "source": "gst_amount", "format": "currency"},
                {"id": "k5", "label": "Total Interest Loss", "agg": "total_value", "source": "interest_loss", "format": "currency"},
                {"id": "k6", "label": "Average Delay Days", "agg": "avg", "source": "days_delay"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Vendor", "source": "vendor", "all_label": "All Vendors"},
                {"id": "f3", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f4", "label": "GST Status", "source": "gst_status", "all_label": "All Statuses"},
                {"id": "f5", "label": "User Name", "source": "user_name", "all_label": "All Users"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "vendor",
                    "y": "interest_loss",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Vendor-wise Interest Loss"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "name_of_company",
                    "y": "gst_amount",
                    "agg": "sum",
                    "title": "Company-wise GST Exposure"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "days_delay",
                    "agg": "count",
                    "title": "Delay Bucket Analysis"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "posting_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Delayed Payment Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "plant",
                    "y": "interest_loss",
                    "agg": "sum",
                    "title": "Plant-wise GST Interest Exposure"
                }
            ]
        }
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company_code": ["Company Code"],
        "vendor": ["Vendor"],
        "plant": ["Plant"],
        "gst_status": ["GST_STATUS"],
        "user_name": ["User name"],
        "accounting_document_number": ["Accounting Document Number"],
        "gst_amount": ["GST_Amount"],
        "interest_loss": ["Interest_Loss"],
        "days_delay": ["Days_Delay"],
        "name_of_company": ["Name of Company"],
        "posting_date": ["Posting Date in the Document"],
        "date": ["Posting Date in the Document"]
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