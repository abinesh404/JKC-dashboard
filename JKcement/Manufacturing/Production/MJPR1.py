# Manufacturing/Production/MJPR1.py
import pandas as pd
import os

CONFIG = {
    "id": "MJPR1",
    "name": "Inventory Valuation - Zero/Negative Stock Value",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Materials with Stock Quantity > 0 but Stock Value <= 0",
            "cards": [
                {"id": "k1", "label": "Exception Materials", "agg": "unique", "source": "material_number"},
                {"id": "k2", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k3", "label": "Material Groups Impacted", "agg": "unique", "source": "material_group"},
                {"id": "k4", "label": "Total Stock Quantity", "agg": "total_value", "source": "quantity"},
                {"id": "k5", "label": "Total Negative/Zero Stock Value", "agg": "total_value", "source": "stock_value", "format": "currency"},
                {"id": "k6", "label": "Average Stock Value per Material", "agg": "avg", "source": "stock_value", "format": "currency"}
            ],
            "filters": [
                {"id": "f1", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f2", "label": "Material Type", "source": "material_type", "all_label": "All Types"},
                {"id": "f3", "label": "Material Group", "source": "material_group", "all_label": "All Groups"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "plant",
                    "y": "stock_value",
                    "agg": "sum",
                    "title": "Plant-wise Negative Inventory Value"
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
                    "x": "material_type",
                    "agg": "count",
                    "title": "Material Type Distribution"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "posting_date",
                    "y": "stock_value",
                    "agg": "sum",
                    "time_group": "month",
                    "title": "Inventory Value Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "storage_location",
                    "y": "quantity",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Storage Location Exposure"
                }
            ]
        }
    ],
    "columns": {
        "plant": ["Plant"],
        "material_type": ["Material Type"],
        "material_group": ["Material Group"],
        "material_number": ["Material Number"],
        "quantity": ["Quantity"],
        "stock_value": ["Stock_Value"],
        "posting_date": ["Posting Date in the Document"],
        "storage_location": ["Storage Location"],
        "date": ["Posting Date in the Document"]
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
        rf"D:\off\JKC Dashboard\output\MJPR1_Exception{int(exc_id):02}.csv",
        rf"data_files/MJPR1_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to standard schema
    rename_map = {
        "Material Number": "Material Number",
        "Valuation Area": "Valuation Area",
        "Valuation Type": "Valuation Type",
        "Deletion flag material valuation type": "Deletion flag material valuation type",
        "Value of Total Valuated Stock": "Value of Total Valuated Stock",
        "Name _Created the Object": "Name _Created the Object",
        "Material Type": "Material Type",
        "Material Group": "Material Group",
        "Base Unit of Measure": "Base Unit of Measure",
        "Gross Weight": "Gross Weight",
        "Net Weight": "Net Weight",
        "Weight Unit": "Weight Unit",
        "Division": "Division",
        "Material Category": "Material Category",
        "Minimum Remaining Shelf Life": "Minimum Remaining Shelf Life",
        "Total shelf life": "Total shelf life",
        "Storage percentage": "Storage percentage",
        "Plant": "Plant",
        "Name": "Name",
        "City": "City",
        "Region": "Region",
        "Accounting Document Number": "Accounting Document Number",
        "Posting Date in the Document": "Posting Date in the Document",
        "Num_of Line Item Within Acc_ Doc": "Num_of Line Item Within Acc_ Doc",
        "Movement Type (Inventory Management)": "Movement Type (Inventory Management)",
        "Batch Number": "Batch Number",
        "Day Accounting Doc_Entered": "Day Accounting Doc_Entered",
        "Time of Entry": "Time of Entry",
        "Amount": "Amount",
        "Fiscal Year": "Fiscal Year",
        "Date of Manufacture": "Date of Manufacture",
        "Stock Type": "Stock Type",
        "Storage Location": "Storage Location",
        "Num_of Material Document": "Num_of Material Document",
        "Quantity": "Quantity",
        "Material Document Year": "Material Document Year",
        "Currency Key": "Currency Key",
        "Document Type": "Document Type",
        "Document Date in Document": "Document Date in Document",
        "Last_Movement_Date": "Last_Movement_Date",
        "Standard price": "Standard price",
        "Total Valuated Stock": "Total Valuated Stock",
        "Stock_Value": "Stock_Value",
        "Stock_Status": "Stock_Status"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = 0.0 if "Value" in col or "price" in col or "Stock" in col or "Quantity" in col or "Amount" in col else ""
            
    return df.fillna('')
