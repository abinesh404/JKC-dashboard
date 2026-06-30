# Manufacturing/Inventory_Movement/MJIM10.py
import pandas as pd
import os

CONFIG = {
    "id": "MJIM10",
    "name": "QA Testing",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
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
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": "QA Testing was not done and subsequent movement types are 701–718 (Write-Off or Adjustment)",
            "cards": [
                {"id": "k1", "label": "Write-Off Transactions", "agg": "unique", "source": "accounting_document_number"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k4", "label": "Total Write-Off Quantity", "agg": "total_value", "source": "writeoff_qty"},
                {"id": "k5", "label": "Full Write-Off Cases", "agg": "unique", "source": "full_writeoff_id"},
                {"id": "k6", "label": "Partial Write-Off Cases", "agg": "unique", "source": "partial_writeoff_id"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Partial or Full Write-Off", "source": "writeoff_type", "all_label": "All Classifications"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "company_name",
                    "y": "writeoff_qty",
                    "agg": "sum",
                    "title": "Company-wise Write-Off Quantity"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "material_number",
                    "y": "writeoff_qty",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Material-wise Write-Off Analysis"
                },
                {
                    "id": "c3",
                    "type": "doughnut",
                    "x": "writeoff_type",
                    "agg": "count",
                    "legend": True,
                    "title": "Write-Off Classification Distribution"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "plant",
                    "y": "amount",
                    "agg": "sum",
                    "title": "Plant-wise Write-Off Exposure"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "movement_type",
                    "agg": "count",
                    "title": "Movement Type Analysis"
                }
            ]
        }
    ],
    "columns": {
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
    paths = [
        rf"D:\off\JKC Dashboard\output\MJIM10_Exception{int(exc_id):02}.csv",
        rf"data_files/MJIM10_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to standard schema
    rename_map = {
        "Company Code": "Company Code",
        "Company Name": "Company Name",
        "City": "City",
        "Country": "Country",
        "Currency": "Currency",
        "Language": "Language",
        "Plant": "Plant",
        "Batch Number": "Batch Number",
        "Material Number": "Material Number",
        "Customer": "Customer",
        "Vendor Code": "Vendor Code",
        "Accounting Document Number": "Accounting Document Number",
        "Storage Location": "Storage Location",
        "Material Document Number": "Material Document Number",
        "Decision code": "Decision Code",
        "UD_Result": "UD_Result",
        "Order Number": "Order Number",
        "Amount": "Amount",
        "Manufacture Date": "Manufacture Date",
        "Unit Measure": "Unit Measure",
        "Fiscal Year": "Fiscal Year",
        "Item Text_full MSEG": "Item Text_full MSEG",
        "Credit/Debit Indicator": "Credit/Debit Indicator",
        "User Name": "User Name",
        "Usage Decision Date": "Usage Decision Date",
        "Inspection_Setup_Required": "Inspection_Setup_Required",
        "Inspection Lot Number": "Inspection Lot Number",
        "Inspection_Lot_Available": "Inspection_Lot_Available",
        "Subsequently_QA_Testing_Done": "Subsequently_QA_Testing_Done",
        "Subsequent_Transaction_Type": "Subsequent_Transaction_Type",
        "Movement Type": "Movement Type",
        "Quantity": "Quantity"
    }
    
    if int(exc_id) == 2:
        rename_map.update({
            "WriteOff_Qty": "WriteOff_Qty",
            "GRN_Qty": "GRN_Qty",
            "Pct": "Pct",
            "Partial or Full write-off": "Partial or Full Write-Off"
        })
        
    df = df.rename(columns=rename_map)
    
    # Ensure all renamed columns are present
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = ""
            
    # Calculate helpers for Exception 01
    if int(exc_id) == 1:
        batch_ids = []
        for idx, row in df.iterrows():
            batch_num = str(row.get("Batch Number", "")).strip()
            if batch_num != "" and batch_num.lower() != "nan":
                batch_ids.append(f"Batch_{idx}")
            else:
                batch_ids.append("")
        df["Batch Row ID"] = batch_ids
        
    # Calculate helpers for Exception 02
    elif int(exc_id) == 2:
        full_wo_ids = []
        part_wo_ids = []
        for idx, row in df.iterrows():
            wo_type = str(row.get("Partial or Full Write-Off", "")).strip()
            if wo_type.lower() == "full write-off":
                full_wo_ids.append(f"Full_{idx}")
                part_wo_ids.append("")
            elif wo_type.lower() == "partial write-off":
                full_wo_ids.append("")
                part_wo_ids.append(f"Part_{idx}")
            else:
                full_wo_ids.append("")
                part_wo_ids.append("")
        df["Full Write-Off ID"] = full_wo_ids
        df["Partial Write-Off ID"] = part_wo_ids
        
    return df.fillna('')
