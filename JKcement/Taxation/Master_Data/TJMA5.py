# Taxation/Master_Data/TJMA5.py
import pandas as pd
import os

CONFIG = {
    "id": "TJMA5",
    "name": "Customer Reconciliation Account Not Defined",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "Cases Where the Customer is Active but Has No Reconciliation Account Defined",
            "cards": [
                {"id": "k1", "label": "Customers Without Recon Account", "agg": "unique", "source": "customer_number"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Active Customers", "agg": "unique", "source": "active_customer_id"},
                {"id": "k4", "label": "Outstanding Balance", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Customers with Transactions", "agg": "unique", "source": "accounting_doc_num"},
                {"id": "k6", "label": "High Risk Customers", "agg": "unique", "source": "high_risk_customer_id"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Customer Number", "source": "customer_number", "all_label": "All Customers"},
                {"id": "f3", "label": "Region", "source": "region", "all_label": "All Regions"},
                {"id": "f4", "label": "Terms of Payment Key", "source": "payment_terms", "all_label": "All Payment Terms"},
                {"id": "f5", "label": "Document Status", "source": "doc_status", "all_label": "All Statuses"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "company_code",
                    "agg": "count",
                    "title": "Company-wise Missing Reconciliation Accounts"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "region",
                    "agg": "count",
                    "title": "Region-wise Customer Distribution"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "name1",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Customer Outstanding Exposure"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "posting_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Transaction Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "payment_terms",
                    "agg": "count",
                    "title": "Payment Terms Analysis"
                }
            ]
        }
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company_code": ["Company Code"],
        "customer_number": ["Customer Number"],
        "region": ["Region"],
        "payment_terms": ["Terms of Payment Key"],
        "doc_status": ["Document Status"],
        "name1": ["Name1"],
        "amount": ["Amount in Local Currency"],
        "accounting_doc_num": ["Accounting Document Number"],
        "posting_date": ["Posting Date in the Document"],
        "date": ["Posting Date in the Document"],
        # Helpers
        "active_customer_id": ["Active Customer ID"],
        "high_risk_customer_id": ["High Risk Customer ID"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Master_Data"
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