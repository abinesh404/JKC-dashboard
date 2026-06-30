# Finance/ITAC/FJIT14.py
import pandas as pd
import os

CONFIG = {
    "id": "FJIT14",
    "name": "PO Quantity Exceeds PR Quantity",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Cases Where PO Quantity is Greater Than PR Quantity",
            "cards": [
                {"id": "k1", "label": "PO > PR Exceptions", "agg": "unique", "source": "purch_doc_num"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Vendors Impacted", "agg": "unique", "source": "vendor_code"},
                {"id": "k4", "label": "Materials Impacted", "agg": "unique", "source": "material_code"},
                {"id": "k5", "label": "Total Excess Quantity", "agg": "total_value", "source": "qty_diff"},
                {"id": "k6", "label": "Excess Procurement Value", "agg": "total_value", "source": "excess_value", "format": "currency"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Vendor Name", "source": "vendor_name", "all_label": "All Vendors"},
                {"id": "f4", "label": "Region", "source": "region", "all_label": "All Regions"},
                {"id": "f5", "label": "City", "source": "city", "all_label": "All Cities"},
                {"id": "f6", "label": "Purchasing Organization", "source": "purch_org", "all_label": "All Orgs"},
                {"id": "f7", "label": "Purchasing Group", "source": "purch_group", "all_label": "All Groups"},
                {"id": "f8", "label": "Purchasing Document Type", "source": "purch_doc_type", "all_label": "All Doc Types"},
                {"id": "f9", "label": "PR Blocked Status", "source": "pr_blocked", "all_label": "All Block Statuses"},
                {"id": "f10", "label": "Processing State", "source": "pr_state", "all_label": "All States"},
                {"id": "f11", "label": "Material Number", "source": "material_code", "all_label": "All Materials"},
                {"id": "f12", "label": "Material Description", "source": "material_desc", "all_label": "All Descriptions"},
                {"id": "f13", "label": "Batch Number", "source": "batch_number", "all_label": "All Batches"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "company_name",
                    "y": "qty_diff",
                    "agg": "sum",
                    "title": "Company-wise Excess Quantity"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "vendor_name",
                    "y": "qty_diff",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Vendor-wise Excess Procurement"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "material_desc",
                    "y": "qty_diff",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Material-wise Quantity Variance"
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
                    "y": "qty_diff",
                    "agg": "sum",
                    "time_group": "month",
                    "title": "Monthly Trend of PO Quantity Variance"
                }
            ]
        }
    ],
    "columns": {
        "company_code": ["Company Code"],
        "plant": ["Plant"],
        "vendor_name": ["Vendor Name"],
        "region": ["Region"],
        "city": ["City"],
        "purch_org": ["Purchasing Organization"],
        "purch_group": ["Purchasing Group"],
        "purch_doc_type": ["Purchasing Document Type"],
        "pr_blocked": ["Purchase Requisition Blocked"],
        "pr_state": ["Requisition Processing State"],
        "material_code": ["Material Number"],
        "material_desc": ["Material Description"],
        "batch_number": ["Batch Number"],
        "purch_doc_num": ["Purchasing Document Number"],
        "vendor_code": ["Vendor Account Number"],
        "company_name": ["Name of Company"],
        "purch_doc_date": ["Purchasing Document Date"],
        "qty_diff": ["Qty_Diff"],
        "excess_value": ["Excess Procurement Value"],
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
    paths = [
        rf"D:\off\JKC Dashboard\output\FJIT14_Exception{int(exc_id):02}.csv",
        rf"data_files/FJIT14_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to standard schema
    rename_map = {
        "Purchasing Document Number": "Purchasing Document Number",
        "Item Number of Purchasing Document": "Item Number of Purchasing Document",
        "Deletion Indicator in Purchasing Documen": "Deletion Indicator in Purchasing Documen",
        "Material Number": "Material Number",
        "Plant": "Plant",
        "Purchase Requisition Unit of Measure": "Purchase Requisition Unit of Measure",
        "Net Price in Purchasing Document": "Net Price in Purchasing Document",
        "Price Unit": "Price Unit",
        "Net Order Value in PO Currency": "Net Order Value in PO Currency",
        "Gross order value in PO currency": "Gross order value in PO currency",
        "Delivery Completed  Indicator": "Delivery Completed  Indicator",
        "Item blocked for SD delivery": "Item blocked for SD delivery",
        "Company Code": "Company Code",
        "Purchasing Document Category": "Purchasing Document Category",
        "Purchasing Document Type": "Purchasing Document Type",
        "Control indicator for purchasing document type": "Control indicator for purchasing document type",
        "Date on Which Record Was Created": "Date on Which Record Was Created",
        "Name of Person who Created the Object": "Name of Person who Created the Object",
        "Vendor Account Number": "Vendor Account Number",
        "Purchasing Organization": "Purchasing Organization",
        "Purchasing Group": "Purchasing Group",
        "Currency Key": "Currency Key",
        "Purchasing Document Date": "Purchasing Document Date",
        "Purchase Requisition Number": "Purchase Requisition Number",
        "Item Number of Purchase Requisition": "Item Number of Purchase Requisition",
        "Batch Number": "Batch Number",
        "Requisition Processing State": "Requisition Processing State",
        "Purchase Requisition Blocked": "Purchase Requisition Blocked",
        "Name of Company": "Name of Company",
        "City": "City",
        "Vendor Name": "Vendor Name",
        "Region": "Region",
        "Material Description": "Material Description",
        "Numerator for Conversion of Order Unit to Base Unit": "Numerator for Conversion of Order Unit to Base Unit",
        "Denominator for Conversion of Order Unit to Base Unit": "Denominator for Conversion of Order Unit to Base Unit",
        "PO_Qty": "PO_Qty",
        "PR_Qty": "PR_Qty",
        "PO_Qty_Converted": "PO_Qty_Converted",
        "Qty_Diff": "Qty_Diff",
        "Exception": "Exception"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = 0.0 if "Qty" in col or "Price" in col or "Value" in col or "value" in col or "Diff" in col else ""
            
    # Apply robust data cleaning
    for num_col in ["PO_Qty_Converted", "PR_Qty", "Qty_Diff", "Net Order Value in PO Currency"]:
        df[num_col] = pd.to_numeric(df[num_col], errors='coerce').fillna(0.0)
        
    # Apply business logic exclusions (if exists in columns)
    if 'Delivery Completed  Indicator' in df.columns:
        df = df[df['Delivery Completed  Indicator'] != 'X']
    if 'Purchase Requisition Blocked' in df.columns:
        df = df[df['Purchase Requisition Blocked'].isna() | (df['Purchase Requisition Blocked'] == '')]
    if 'Deletion Indicator in Purchasing Documen' in df.columns:
        df = df[df['Deletion Indicator in Purchasing Documen'].isna() | (df['Deletion Indicator in Purchasing Documen'] == '')]
        
    # Calculate Excess Procurement Value: (Qty_Diff / PO_Qty_Converted) * Net Order Value in PO Currency
    excess_vals = []
    for idx, row in df.iterrows():
        diff = float(row.get("Qty_Diff", 0.0))
        po_qty = float(row.get("PO_Qty_Converted", 0.0))
        net_val = float(row.get("Net Order Value in PO Currency", 0.0))
        
        if po_qty > 0:
            excess_vals.append((diff / po_qty) * net_val)
        else:
            excess_vals.append(0.0)
            
    df["Excess Procurement Value"] = excess_vals
    
    return df.fillna('')
