# Manufacturing/Production/MJPR9.py
import pandas as pd
import os

CONFIG = {
    "id": "MJPR9",
    "name": "Receipt of Low Shelf Life Material",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Remaining Shelf Life Less Than 50% at the Time of GRN",
            "cards": [
                {"id": "k1", "label": "Low Shelf Life GRNs", "agg": "unique", "source": "material_doc_id"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Vendors Impacted", "agg": "unique", "source": "vendor_account_number"},
                {"id": "k4", "label": "Total Quantity Received", "agg": "total_value", "source": "quantity"},
                {"id": "k5", "label": "Inventory Value at Risk", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k6", "label": "Average Remaining Shelf Life %", "agg": "avg", "source": "remaining_percent", "format": "percentage"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Vendor Account Number", "source": "vendor_account_number", "all_label": "All Vendors"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "name1",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Vendor-wise Low Shelf Life Receipts"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "plant",
                    "y": "amount",
                    "agg": "sum",
                    "title": "Plant-wise Inventory Value at Risk"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "material_number",
                    "y": "quantity",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Material-wise Quantity Received"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "posting_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Low Shelf Life Receipt Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "purchasing_group",
                    "agg": "count",
                    "title": "Purchasing Group Analysis"
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": "Shelf Life Less Than 365 Days at the Time of GRN",
            "cards": [
                {"id": "k1", "label": "Short Shelf Life GRNs", "agg": "unique", "source": "material_doc_id"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Vendors Impacted", "agg": "unique", "source": "vendor_account_number"},
                {"id": "k4", "label": "Total Quantity Received", "agg": "total_value", "source": "quantity"},
                {"id": "k5", "label": "Inventory Value at Risk", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k6", "label": "Average Remaining Shelf Life Days", "agg": "avg", "source": "remaining_shelf_life_days"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Purchasing Group", "source": "purchasing_group", "all_label": "All Groups"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "name1",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Vendor-wise Short Shelf Life Receipts"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "plant",
                    "y": "amount",
                    "agg": "sum",
                    "title": "Plant-wise Inventory Exposure"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "material_number",
                    "y": "remaining_shelf_life_days",
                    "agg": "avg",
                    "top_n": 10,
                    "title": "Material-wise Remaining Shelf Life"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "posting_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Receipt Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "purchasing_group",
                    "agg": "count",
                    "title": "Purchasing Group Analysis"
                }
            ]
        }
    ],
    "columns": {
        "company_code": ["Company Code"],
        "plant": ["Plant"],
        "vendor_account_number": ["Vendor Account Number"],
        "purchasing_group": ["Purchasing Group"],
        "material_number": ["Material Number"],
        "name1": ["NAME1"],
        "quantity": ["Quantity"],
        "amount": ["Amount in Local Currency"],
        "remaining_percent": ["Remaining_Percent"],
        "remaining_shelf_life_days": ["Remaining Shelf Life Days"],
        "posting_date": ["Posting Date in the Document"],
        "date": ["Posting Date in the Document"],
        # Helpers
        "material_doc_id": ["Material Doc ID"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Production"
    }

def get_data(exc_id):
    paths = [
        rf"D:\off\JKC Dashboard\output\MJPR9_Exception{int(exc_id):02}.csv",
        rf"data_files/MJPR9_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to standard schema
    rename_map = {
        "Order Number": "Order Number",
        "Order Item Number": "Order Item Number",
        "Accounting Document Number": "Accounting Document Number",
        "Posting Date in the Document": "Posting Date in the Document",
        "Company Code": "Company Code",
        "Number of Line Item Within Accounting Document": "Number of Line Item Within Accounting Document",
        "Movement Type": "Movement Type",
        "Batch Number": "Batch Number",
        "Day On Which Accounting Document Was Entered": "Day On Which Accounting Document Was Entered",
        "Time of Entry": "Time of Entry",
        "Amount in Local Currency": "Amount in Local Currency",
        "Purchase Order Number": "Purchase Order Number",
        "Item Number of Purchasing Document": "Item Number of Purchasing Document",
        "Fiscal Year": "Fiscal Year",
        "Date of Manufacture": "Date of Manufacture",
        "Vendor Account Number": "Vendor Account Number",
        "Client": "Client",
        "Material Number": "Material Number",
        "Number of Material Document": "Number of Material Document",
        "Base Unit of Measure": "Base Unit of Measure",
        "Quantity": "Quantity",
        "Material Document Year": "Material Document Year",
        "Item Text": "Item Text",
        "Debit/Credit Indicator": "Debit/Credit Indicator",
        "Shelf Life Expiration or Best-Before Date": "Shelf Life Expiration or Best-Before Date",
        "Currency Key": "Currency Key",
        "Plant": "Plant",
        "Reference Document Number": "Reference Document Number",
        "Document Type": "Document Type",
        "Document Date in Document": "Document Date in Document",
        "User name": "User name",
        "Deletion Indicator in Purchasing Document": "Deletion Indicator in Purchasing Document",
        "Changed On": "Changed On",
        "Name of Person who Created the Object": "Name of Person who Created the Object",
        "NAME1": "NAME1",
        "Terms of Payment Key": "Terms of Payment Key",
        "Purchasing Group": "Purchasing Group",
        "Purchasing Document Date": "Purchasing Document Date",
        "Account Number of Customer": "Account Number of Customer",
        "VAT Registration Number": "VAT Registration Number",
        "Name of Person Who Changed Object": "Name of Person Who Changed Object",
        "Purchasing Document Type": "Purchasing Document Type",
        "Purchasing Document Category": "Purchasing Document Category",
        "Short Description of Purchasing Document Type": "Short Description of Purchasing Document Type",
        "Name 1": "Name 1",
        "Region": "Region",
        "Total_Shelf_Life": "Total_Shelf_Life"
    }
    
    if int(exc_id) == 1:
        rename_map.update({
            "Remaining_Shelf_Days": "Remaining_Shelf_Days",
            "Remaining_Percent < 50": "Remaining_Percent < 50"
        })
    elif int(exc_id) == 2:
        rename_map.update({
            "Reamining shelf life_days<365": "Reamining shelf life_days<365"
        })
        
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = 0.0 if "Qty" in col or "Quantity" in col or "Percent" in col or "Life" in col or "Days" in col or "Amount" in col else ""
            
    # Calculate helpers for Exception 01
    if int(exc_id) == 1:
        tot_shelf = pd.to_numeric(df["Total_Shelf_Life"], errors='coerce').fillna(0)
        rem_shelf = pd.to_numeric(df["Remaining_Shelf_Days"], errors='coerce').fillna(0)
        df["Remaining_Percent"] = (rem_shelf / tot_shelf * 100).fillna(0)
        
    # Calculate helpers for Exception 02
    elif int(exc_id) == 2:
        df["Remaining Shelf Life Days"] = pd.to_numeric(df["Reamining shelf life_days<365"], errors='coerce').fillna(0)
        
    # Unique ID helper for GRN Document
    grn_ids = []
    for idx, row in df.iterrows():
        grn_num = str(row.get("Number of Material Document", "")).strip()
        grn_ids.append(f"GRN_{idx}" if grn_num else "")
    df["Material Doc ID"] = grn_ids
    
    return df.fillna('')
