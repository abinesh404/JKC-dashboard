# Finance/ITAC/FJIT15.py
import pandas as pd
import os

CONFIG = {
    "id": "FJIT15",
    "name": "PO Quantity Exceeds PR Quantity (Part II)",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "Cases Where the PR Number is Blank or Not Matching with PR Master Data",
            "cards": [
                {"id": "k1", "label": "Invalid/Missing PR Cases", "agg": "unique", "source": "purch_doc_num"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Vendors Impacted", "agg": "unique", "source": "vendor_code"},
                {"id": "k4", "label": "Materials Impacted", "agg": "unique", "source": "material_code"},
                {"id": "k5", "label": "Total PO Value", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k6", "label": "Total Quantity Without Valid PR", "agg": "total_value", "source": "po_qty"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Name of Company", "source": "company_name", "all_label": "All Companies Names"},
                {"id": "f3", "label": "City", "source": "city", "all_label": "All Cities"},
                {"id": "f4", "label": "Region", "source": "region", "all_label": "All Regions"},
                {"id": "f5", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f6", "label": "Purchasing Organization", "source": "purch_org", "all_label": "All Orgs"},
                {"id": "f7", "label": "Purchasing Group", "source": "purch_group", "all_label": "All Groups"},
                {"id": "f8", "label": "Purchasing Document Type", "source": "purch_doc_type", "all_label": "All Doc Types"},
                {"id": "f9", "label": "Purchasing Document Category", "source": "purch_doc_cat", "all_label": "All Categories"},
                {"id": "f10", "label": "Purchase Requisition Blocked", "source": "pr_blocked", "all_label": "All Block Statuses"},
                {"id": "f11", "label": "Requisition Processing State", "source": "pr_state", "all_label": "All States"},
                {"id": "f12", "label": "Qty Status", "source": "qty_status", "all_label": "All Qty Statuses"},
                {"id": "f13", "label": "Vendor Name", "source": "vendor_name", "all_label": "All Vendors"},
                {"id": "f14", "label": "Vendor Account Number", "source": "vendor_code", "all_label": "All Vendor Codes"},
                {"id": "f15", "label": "Material Number", "source": "material_code", "all_label": "All Materials"},
                {"id": "f16", "label": "Material Description", "source": "material_desc", "all_label": "All Descriptions"},
                {"id": "f17", "label": "Batch Number", "source": "batch_number", "all_label": "All Batches"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "company_name",
                    "y": "purch_doc_num",
                    "agg": "count",
                    "title": "Company-wise Invalid PR Cases"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "vendor_name",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Vendor-wise PO Value Without PR"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "material_desc",
                    "y": "po_qty",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Material-wise Quantity Without PR"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "purch_group",
                    "y": "purch_doc_num",
                    "agg": "count",
                    "title": "Purchasing Group-wise Exceptions"
                },
                {
                    "id": "c5",
                    "type": "line",
                    "x": "purch_doc_date",
                    "y": "purch_doc_num",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Trend of Invalid PR Transactions"
                }
            ]
        }
    ],
    "columns": {
        "exception_type": ["Exception Type"],
        "company_code": ["Company Code"],
        "company_name": ["Name of Company"],
        "city": ["City"],
        "region": ["Region"],
        "plant": ["Plant"],
        "purch_org": ["Purchasing Organization"],
        "purch_group": ["Purchasing Group"],
        "purch_doc_type": ["Purchasing Document Type"],
        "purch_doc_cat": ["Purchasing Document Category"],
        "pr_blocked": ["Purchase Requisition Blocked"],
        "pr_state": ["Requisition Processing State"],
        "qty_status": ["Qty_Status"],
        "vendor_name": ["Vendor Name"],
        "vendor_code": ["Vendor Account Number"],
        "material_code": ["Material Number"],
        "material_desc": ["Material Description"],
        "batch_number": ["Batch Number"],
        "purch_doc_num": ["Purchasing Document Number"],
        "purch_doc_date": ["Purchasing Document Date"],
        "amount": ["Net Order Value in PO Currency"],
        "po_qty": ["PO_Qty_Converted"],
        "date": ["Purchasing Document Date"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "ITAC"
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