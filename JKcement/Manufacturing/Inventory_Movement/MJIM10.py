# Manufacturing/Inventory_Movement/MJIM10.py
import pandas as pd
import os

CONFIG = {
    "id": "MJIM10",
    "name": "QA Testing",
    "active_exceptions": [
        {
            "id": "1",
            "label": "All Exceptions",
            "title": "QA Testing was not done and subsequent movement types are Z01 or 309",
            "cards": [
                {"id": "k1", "label": "QA Bypass Transactions", "agg": "unique", "source": "accounting_document_number"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k4", "label": "Total Transfer Quantity", "agg": "total_value", "source": "quantity"},
                {"id": "k5", "label": "Materials Transferred Without QA", "agg": "unique", "source": "material_number"},
                {"id": "k6", "label": "Batches Without Inspection Lot", "agg": "unique", "source": "batch_row_id"}
            ],
            "filters": [
                {"id": "f_extype", "label": "Exception Type", "source": "exception_type"},
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Material Number", "source": "material_number", "all_label": "All Materials"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "company_name",
                    "y": "quantity",
                    "agg": "sum",
                    "title": "Company-wise QA Bypass Transfers"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "material_number",
                    "y": "quantity",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Top Materials Transferred Without QA"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "subsequent_transaction_type",
                    "agg": "count",
                    "title": "Movement Type Distribution"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "plant",
                    "y": "quantity",
                    "agg": "sum",
                    "title": "Plant-wise Transfer Quantity"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "user_name",
                    "agg": "count",
                    "top_n": 10,
                    "title": "User-wise Transactions"
                }
            ]
        }],
    "columns": {
        "exception_type": ["Exception Type"],
        "company_code": ["Company Code"],
        "company_name": ["Company Name"],
        "plant": ["Plant"],
        "material_number": ["Material Number"],
        "batch_number": ["Batch Number"],
        "quantity": ["Quantity"],
        "writeoff_qty": ["WriteOff_Qty"],
        "amount": ["Amount"],
        "user_name": ["User Name"],
        "movement_type": ["Movement Type"],
        "subsequent_transaction_type": ["Subsequent_Transaction_Type"],
        "accounting_document_number": ["Accounting Document Number"],
        "writeoff_type": ["Partial or Full Write-Off"],
        # Date fallback for layout initialization (manufacture date is available)
        "date": ["Manufacture Date"],
        # Helpers
        "batch_row_id": ["Batch Row ID"],
        "full_writeoff_id": ["Full Write-Off ID"],
        "partial_writeoff_id": ["Partial Write-Off ID"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Inventory_Movement"
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