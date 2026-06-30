# Manufacturing/Others/MJOT06.py
import pandas as pd
import os

CONFIG = {
    "id": "MJOT06",
    "name": "Actual Yield Loss vis-a-vis Standard Yield Loss",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Actual Yield Loss Exceeds Standard Yield Loss Percentage",
            "cards": [
                {"id": "k1", "label": "Production Orders with Yield Loss", "agg": "unique", "source": "order_number"},
                {"id": "k2", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k3", "label": "Work Centers Impacted", "agg": "unique", "source": "work_center_id"},
                {"id": "k4", "label": "Total Planned Output Quantity", "agg": "total_value", "source": "planned_qty"},
                {"id": "k5", "label": "Total Actual Yield Quantity", "agg": "total_value", "source": "actual_yield"},
                {"id": "k6", "label": "Average Yield Loss %", "agg": "avg", "source": "actual_loss_percent"}
            ],
            "filters": [
                {"id": "f1", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f2", "label": "Work Center ID", "source": "work_center_id", "all_label": "All Work Centers"},
                {"id": "f3", "label": "MRP Controller", "source": "mrp_controller", "all_label": "All Controllers"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "plant",
                    "y": "actual_loss_percent",
                    "agg": "avg",
                    "title": "Plant-wise Yield Loss Analysis"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "work_center_id",
                    "y": "actual_loss_percent",
                    "agg": "avg",
                    "top_n": 10,
                    "title": "Work Center-wise Yield Loss"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "material_number",
                    "y": "actual_loss_percent",
                    "agg": "avg",
                    "top_n": 10,
                    "title": "Material-wise Yield Loss"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "posting_date",
                    "y": "actual_yield_percent",
                    "agg": "avg",
                    "time_group": "month",
                    "title": "Production Trend Analysis"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "mrp_controller",
                    "y": "yield_variance",
                    "agg": "avg",
                    "title": "MRP Controller-wise Yield Variance"
                }
            ]
        }
    ],
    "columns": {
        "plant": ["Plant"],
        "work_center_id": ["Work Center ID"],
        "mrp_controller": ["MRP Controller"],
        "order_number": ["Order Number"],
        "planned_qty": ["Planned output quantity"],
        "actual_yield": ["Actual yield (confirmed)"],
        "actual_loss_percent": ["Actual_Loss_Percent"],
        "actual_yield_percent": ["Actual_Yield_Percent"],
        "yield_variance": ["Yield Variance"],
        "material_number": ["Material Number"],
        "posting_date": ["Posting Date"],
        "date": ["Posting Date"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Others"
    }

def get_data(exc_id):
    paths = [
        rf"D:\off\JKC Dashboard\output\MJOT06_Exception{int(exc_id):02}.csv",
        rf"data_files/MJOT06_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to standard schema
    rename_map = {
        "Order Number": "Order Number",
        "Material Number": "Material Number",
        "Plant": "Plant",
        "Work Center ID": "Work Center ID",
        "Operation Short Text": "Operation Short Text",
        "Operation/Activity Number": "Operation/Activity Number",
        "Created By": "Created By",
        "Created Date": "Created Date",
        "Posting Date": "Posting Date",
        "Basic Finish Date": "Basic Finish Date",
        "Basic Start Date": "Basic Start Date",
        "Reservation Number": "Reservation Number",
        "Reservation Item": "Reservation Item",
        "Storage Location": "Storage Location",
        "Purchase Document Item Number": "Purchase Document Item Number",
        "Purchase Document Number": "Purchase Document Number",
        "Vendor Code": "Vendor Code",
        "Movement Type": "Movement Type",
        "MRP Controller": "MRP Controller",
        "Planned output quantity": "Planned output quantity",
        "Requirement Quantity": "Requirement Quantity",
        "Unit Measure": "Unit Measure",
        "Withdrawn Quantity": "Withdrawn Quantity",
        "Actual yield (confirmed)": "Actual yield (confirmed)",
        "Actual_Yield_Percent": "Actual_Yield_Percent",
        "Actual_Loss_Percent": "Actual_Loss_Percent",
        "Standard_Yield_Loss": "Standard_Yield_Loss"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = 0.0 if "Qty" in col or "quantity" in col or "Percent" in col or "Loss" in col else ""
            
    # Calculate Yield Variance (Actual_Loss_Percent - Standard_Yield_Loss)
    act_loss = pd.to_numeric(df["Actual_Loss_Percent"], errors='coerce').fillna(0)
    std_loss = pd.to_numeric(df["Standard_Yield_Loss"], errors='coerce').fillna(0)
    df["Yield Variance"] = act_loss - std_loss
    
    return df.fillna('')
