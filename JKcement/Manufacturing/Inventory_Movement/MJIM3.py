# Manufacturing/Inventory_Movement/MJIM3.py
import pandas as pd
import os

CONFIG = {
    "id": "MJIM3",
    "name": "Lack of QA Testing",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "No Inspection Lot Was Created for the Original Document",
            "cards": [
                {"id": "k1", "label": "Materials Without QA Inspection", "agg": "unique", "source": "material_number"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k4", "label": "Total Inventory Value", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Total Quantity Without QA", "agg": "total_value", "source": "quantity"},
                {"id": "k6", "label": "Batches Without Inspection Lot", "agg": "unique", "source": "batch_number"}
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
                    "agg": "count",
                    "title": "Company-wise QA Exceptions"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "material_number",
                    "y": "amount",
                    "agg": "sum",
                    "horizontal": True,
                    "top_n": 10,
                    "title": "Top Materials Without QA Testing"
                },
                {
                    "id": "c3",
                    "type": "doughnut",
                    "x": "plant",
                    "agg": "count",
                    "legend": True,
                    "title": "Plant-wise QA Exception Distribution"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "manufacture_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly QA Exception Trend"
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
        "amount": ["Amount"],
        "quantity": ["Quantity"],
        "manufacture_date": ["Manufacture Date"],
        "movement_type": ["Movement Type"],
        "date": ["Manufacture Date"]
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
        rf"D:\off\JKC Dashboard\output\MJIM3_Exception{int(exc_id):02}.csv",
        rf"data_files/MJIM3_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to match Suggested Column Mapping exactly
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
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    required_cols = list(rename_map.values())
    for col in required_cols:
        if col not in df.columns:
            df[col] = ""
            
    return df.fillna('')
