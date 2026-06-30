# Manufacturing/Production/MJPR7.py
import pandas as pd
import os

CONFIG = {
    "id": "MJPR7",
    "name": "Difference in Shelf Life",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Shelf Life Inconsistency (Expiry or Shelf Life Mismatch)",
            "cards": [
                {"id": "k1", "label": "Shelf Life Exceptions", "agg": "unique", "source": "material_row_id"},
                {"id": "k2", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k3", "label": "Materials Impacted", "agg": "unique", "source": "material_number"},
                {"id": "k4", "label": "Expired Inventory Quantity", "agg": "total_value", "source": "expired_qty_helper"},
                {"id": "k5", "label": "Inventory Value at Risk", "agg": "total_value", "source": "val_at_risk_helper", "format": "currency"},
                {"id": "k6", "label": "Average Remaining Shelf Life Days", "agg": "avg", "source": "remaining_shelf_life_days"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Material Type", "source": "material_type", "all_label": "All Types"},
                {"id": "f4", "label": "Material Group", "source": "material_group", "all_label": "All Groups"},
                {"id": "f5", "label": "Storage Location", "source": "storage_location", "all_label": "All Locations"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "plant",
                    "agg": "count",
                    "title": "Plant-wise Shelf Life Exceptions"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "material_group",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Material Group-wise Exception Analysis"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "remaining_shelf_life_days",
                    "agg": "count",
                    "title": "Remaining Shelf Life Distribution"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "date_of_expiry",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Expiry Trend Analysis"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "material_desc",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Inventory Value Exposure"
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": "Inventory Valuation Error (Stock Quantity and Value Mismatch)",
            "cards": [
                {"id": "k1", "label": "Valuation Exceptions", "agg": "unique", "source": "material_row_id"},
                {"id": "k2", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k3", "label": "Materials Impacted", "agg": "unique", "source": "material_number"},
                {"id": "k4", "label": "Total Inventory Value", "agg": "total_value", "source": "stock_value", "format": "currency"},
                {"id": "k5", "label": "Total Stock Quantity", "agg": "total_value", "source": "quantity"},
                {"id": "k6", "label": "Average Stock Value per Unit", "agg": "avg", "source": "stock_value_per_unit", "format": "currency"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Valuation Area", "source": "valuation_area", "all_label": "All Areas"},
                {"id": "f4", "label": "Material Type", "source": "material_type", "all_label": "All Types"},
                {"id": "f5", "label": "Storage Location", "source": "storage_location", "all_label": "All Locations"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "plant",
                    "y": "stock_value",
                    "agg": "sum",
                    "title": "Plant-wise Valuation Errors"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "material_group",
                    "y": "total_val_stock",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Material Group-wise Valuation Exposure"
                },
                {
                    "id": "c3",
                    "type": "doughnut",
                    "x": "material_type",
                    "agg": "count",
                    "legend": True,
                    "title": "Material Type Distribution"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "posting_date",
                    "y": "stock_value",
                    "agg": "sum",
                    "time_group": "month",
                    "title": "Inventory Valuation Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "storage_location",
                    "y": "quantity",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Storage Location Analysis"
                }
            ]
        }
    ],
    "columns": {
        "company_code": ["Company Code"],
        "plant": ["Plant"],
        "material_type": ["Material Type"],
        "material_group": ["Material Group"],
        "storage_location": ["Storage Location"],
        "valuation_area": ["Valuation Area"],
        "material_number": ["Material Number"],
        "quantity": ["Quantity"],
        "amount": ["Amount in Local Currency"],
        "stock_value": ["STOCK_VALUE"],
        "total_val_stock": ["Total Valuated Stock"],
        "remaining_shelf_life_days": ["Remaining_Shelf_Life_Days"],
        "date_of_expiry": ["Date Of Expiry"],
        "material_desc": ["Material description"],
        "posting_date": ["Posting Date in the Document"],
        "date": ["Posting Date in the Document"],
        # Helpers
        "material_row_id": ["Material Row ID"],
        "expired_qty_helper": ["Expired Qty Helper"],
        "val_at_risk_helper": ["Val at Risk Helper"],
        "stock_value_per_unit": ["Stock Value per Unit"]
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
        rf"D:\off\JKC Dashboard\output\MJPR7_Exception{int(exc_id):02}.csv",
        rf"data_files/MJPR7_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to match standard schema
    rename_map = {
        "Material Number": "Material Number",
        "Number of Material Document": "Number of Material Document",
        "Quantity": "Quantity",
        "Valuation Type": "Valuation Type",
        "Customer number of plant": "Customer number of plant",
        "Vendor number of plant": "Vendor number of plant",
        "City": "City",
        "Region": "Region",
        "Accounting Document Number": "Accounting Document Number",
        "Posting Date in the Document": "Posting Date in the Document",
        "Company Code": "Company Code",
        "Movement Type": "Movement Type",
        "Batch Number": "Batch Number",
        "Amount in Local Currency": "Amount in Local Currency",
        "Fiscal Year": "Fiscal Year",
        "Debit/Credit Indicator": "Debit/Credit Indicator",
        "Plant": "Plant",
        "Material Document Year": "Material Document Year",
        "Document Type": "Document Type",
        "Document Date in Document": "Document Date in Document",
        "User name": "User name",
        "Transaction Code": "Transaction Code",
        "Document Header Text": "Document Header Text",
        "Date Of Expiry": "Date Of Expiry",
        "BATCH_ID": "BATCH_ID",
        "Date of Manufacture": "Date of Manufacture",
        "BATCH_TYPE": "BATCH_TYPE",
        "Material Type": "Material Type",
        "Material Group": "Material Group",
        "Valuation Area": "Valuation Area",
        "Base Unit of Measure": "Base Unit of Measure",
        "Storage percentage": "Storage percentage",
        "General item category group": "General item category group",
        "Stock Type": "Stock Type",
        "Storage Location": "Storage Location",
        "Minimum Remaining Shelf Life": "Minimum Remaining Shelf Life",
        "Last_Movement_Date": "Last_Movement_Date",
        "Total Shelf Life": "Total Shelf Life",
        "Remaining_Shelf_Life_Days": "Remaining_Shelf_Life_Days",
        "Standard price": "Standard price",
        "Total Valuated Stock": "Total Valuated Stock",
        "Material description": "Material description"
    }
    
    if int(exc_id) == 2:
        rename_map.update({
            "STOCK_VALUE": "STOCK_VALUE",
            "Exception2": "Exception2"
        })
    else:
        rename_map.update({
            "Exception1": "Exception1",
            "Days_Since_Last_Movement": "Days_Since_Last_Movement"
        })
        
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = 0.0 if "Qty" in col or "Quantity" in col or "price" in col or "Stock" in col or "VALUE" in col or "Days" in col or "Amount" in col else ""
            
    # Unique ID helper for exceptions
    row_ids = []
    for idx, _ in df.iterrows():
        row_ids.append(f"Exc{exc_id}_{idx}")
    df["Material Row ID"] = row_ids
    
    # Calculate helpers for Exception 01
    if int(exc_id) == 1:
        expired_qtys = []
        val_at_risks = []
        
        for idx, row in df.iterrows():
            rsl_days = pd.to_numeric(row.get("Remaining_Shelf_Life_Days", 0), errors='coerce')
            qty = pd.to_numeric(row.get("Quantity", 0), errors='coerce')
            amt = pd.to_numeric(row.get("Amount in Local Currency", 0), errors='coerce')
            
            if pd.notna(rsl_days) and rsl_days < 0:
                expired_qtys.append(qty)
            else:
                expired_qtys.append(0.0)
                
            if pd.notna(rsl_days) and rsl_days < 10:
                val_at_risks.append(amt)
            else:
                val_at_risks.append(0.0)
                
        df["Expired Qty Helper"] = expired_qtys
        df["Val at Risk Helper"] = val_at_risks
        
    # Calculate helpers for Exception 02
    elif int(exc_id) == 2:
        val_per_units = []
        for idx, row in df.iterrows():
            qty = pd.to_numeric(row.get("Quantity", 0), errors='coerce')
            stock_val = pd.to_numeric(row.get("STOCK_VALUE", 0), errors='coerce')
            
            if pd.notna(qty) and qty > 0:
                val_per_units.append(stock_val / qty)
            else:
                val_per_units.append(0.0)
                
        df["Stock Value per Unit"] = val_per_units
        
    return df.fillna('')
