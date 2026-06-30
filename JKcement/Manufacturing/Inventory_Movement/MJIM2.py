# Manufacturing/Inventory_Movement/MJIM2.py
import pandas as pd
import os

CONFIG = {
    "id": "MJIM2",
    "name": "Idle Inventory Ageing at Source Batch Level",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Batches Idle More Than 90 Days (Idle Days > 90)",
            "cards": [
                {"id": "k1", "label": "Idle Batches (>90 Days)", "agg": "unique", "source": "batch_number"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k4", "label": "Total Inventory Value", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Total Idle Quantity", "agg": "total_value", "source": "quantity"},
                {"id": "k6", "label": "Average Idle Days", "agg": "avg", "source": "idle_days"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Material Group", "source": "material_group", "all_label": "All Groups"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "company_code",
                    "y": "amount",
                    "agg": "sum",
                    "title": "Company-wise Idle Inventory Value"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "material_number",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Top Materials by Idle Inventory Value"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "ageing_bucket",
                    "agg": "count",
                    "title": "Ageing Bucket Distribution"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "plant",
                    "y": "quantity",
                    "agg": "sum",
                    "title": "Plant-wise Idle Inventory"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "storage_location",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Storage Location Analysis"
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": "Batches Idle More Than 180 Days (Idle Days > 180)",
            "cards": [
                {"id": "k1", "label": "Idle Batches (>180 Days)", "agg": "unique", "source": "batch_number"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k4", "label": "Total Inventory Value", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Total Idle Quantity", "agg": "total_value", "source": "quantity"},
                {"id": "k6", "label": "Average Idle Days", "agg": "avg", "source": "idle_days"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Material Group", "source": "material_group", "all_label": "All Groups"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "company_code",
                    "y": "amount",
                    "agg": "sum",
                    "title": "Company-wise Idle Inventory Value"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "material_number",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Top Materials by Idle Inventory Value"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "ageing_bucket",
                    "agg": "count",
                    "title": "Ageing Bucket Distribution"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "plant",
                    "y": "quantity",
                    "agg": "sum",
                    "title": "Plant-wise Idle Inventory"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "warehouse_storage_condition",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Warehouse Storage Condition Analysis"
                }
            ]
        }
    ],
    "columns": {
        "company_code": ["Company Code"],
        "material_number": ["Material Number"],
        "material_group": ["Material Group"],
        "batch_number": ["Batch Number"],
        "quantity": ["Quantity"],
        "plant": ["Plant"],
        "storage_location": ["Storage Location"],
        "warehouse_storage_condition": ["Warehouse Storage Condition"],
        "amount": ["Amount in Local Currency"],
        "idle_days": ["Idle_Days"],
        "ageing_bucket": ["Ageing_Bucket"],
        "date": ["Posting Date in the Document"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Inventory_Movement"
    }

def get_data(exc_id):
    paths = [
        rf"D:\off\JKC Dashboard\output\MJIM2_Exception{int(exc_id):02}.csv",
        rf"data_files/MJIM2_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to match Suggested Column Mapping exactly
    rename_map = {
        "Posting Date in the Document": "Posting Date in the Document",
        "Document Date in Document": "Document Date in Document",
        "Warehouse Storage Condition": "Warehouse Storage Condition",
        "Amount in Local Currency": "Amount in Local Currency",
        "Batch Number": "Batch Number",
        "Material Number": "Material Number",
        "Material Group": "Material Group",
        "Company Code": "Company Code",
        "Plant": "Plant",
        "Quantity": "Quantity"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    required_cols = [
        "Company Code", "Material Number", "Material Group", "Material Type", "Batch Number",
        "Vendor Batch Number", "Quantity", "Base Unit of Measure", "Stock Type",
        "Plant", "Storage Location", "Warehouse Material Group", "Warehouse Storage Condition",
        "Amount in Local Currency", "Currency Key", "Posting Date in the Document",
        "Document Date in Document", "Last Movement Date", "Shelf Life Expiration or Best-Before Date",
        "Idle_Days", "Ageing_Bucket", "Exception", "Accounting Document Number",
        "Material Document Year", "Number of Material Document", "Fiscal Year", "Document Type",
        "User name", "Vendor Account Number", "Client", "Movement Type (Inventory Management)",
        "Debit/Credit Indicator", "Order Number"
    ]
    for col in required_cols:
        if col not in df.columns:
            df[col] = ""
            
    return df.fillna('')
