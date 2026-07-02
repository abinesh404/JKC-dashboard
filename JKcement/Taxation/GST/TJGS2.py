# Taxation/GST/TJGS2.py
import pandas as pd
import os

CONFIG = {
    "id": "TJGS2",
    "name": "GST Query",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "Cases Where GST Invoices Have the Same Vendor Invoice Number (Reference Number) in the Same Fiscal Year",
            "cards": [
                {"id": "k1", "label": "Duplicate GST Invoices", "agg": "unique", "source": "accounting_doc_num"},
                {"id": "k2", "label": "Vendors Impacted", "agg": "unique", "source": "vendor_code"},
                {"id": "k3", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k4", "label": "Total GST Amount", "agg": "total_value", "source": "total_gst", "format": "currency"},
                {"id": "k5", "label": "Duplicate Invoice Amount", "agg": "total_value", "source": "dup_inv_amt", "format": "currency"},
                {"id": "k6", "label": "Fiscal Years Impacted", "agg": "unique", "source": "fiscal_year"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Vendor Code", "source": "vendor_code", "all_label": "All Vendors"},
                {"id": "f3", "label": "Fiscal Year", "source": "fiscal_year", "all_label": "All Years"},
                {"id": "f4", "label": "User Name", "source": "user_name", "all_label": "All Users"},
                {"id": "f5", "label": "Account Group", "source": "account_group", "all_label": "All Groups"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "vendor_name",
                    "y": "reference",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Vendor Duplicate Analysis"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "company_desc",
                    "y": "total_gst",
                    "agg": "sum",
                    "title": "Company Exposure"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "fiscal_year",
                    "agg": "count",
                    "title": "Fiscal Year Trend"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "user_name",
                    "agg": "count",
                    "top_n": 10,
                    "title": "User Analysis"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "gl_long_text",
                    "y": "total_gst",
                    "agg": "sum",
                    "title": "GST Component Analysis"
                }
            ]
        }
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company_code": ["Company Code"],
        "company_desc": ["Company Description"],
        "vendor_code": ["Vendor Code"],
        "vendor_name": ["Vendor Name"],
        "fiscal_year": ["Fiscal Year"],
        "user_name": ["User Name"],
        "account_group": ["Account group"],
        "accounting_doc_num": ["Accounting Document Number"],
        "total_gst": ["Total GST"],
        "dup_inv_amt": ["Duplicate Invoice Amount"],
        "reference": ["Reference"],
        "gl_long_text": ["G/L Account Long Text"],
        "date": ["Posting Date"]
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