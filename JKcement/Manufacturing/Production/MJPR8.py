# Manufacturing/Production/MJPR8.py
import pandas as pd
import os

CONFIG = {
    "id": "MJPR8",
    "name": "Low Shelf Life",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Remaining Shelf Life, Manufacturing Date (HSDAT) and Expiry Date (VFDAT) are Not Available",
            "cards": [
                {"id": "k1", "label": "Missing Shelf Life Records", "agg": "unique", "source": "message_row_id"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k4", "label": "Vendors Impacted", "agg": "unique", "source": "vendor_account_number"},
                {"id": "k5", "label": "Total Inventory Quantity", "agg": "total_value", "source": "quantity"},
                {"id": "k6", "label": "Inventory Value at Risk", "agg": "total_value", "source": "amount", "format": "currency"}
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
                    "x": "company_code",
                    "agg": "count",
                    "title": "Company-wise Missing Shelf Life Records"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "plant",
                    "agg": "count",
                    "title": "Plant-wise Missing Shelf Life Cases"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "name1",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Vendor-wise Exposure Analysis"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "material_number",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Material-wise Missing Information"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "ekgrp",
                    "agg": "count",
                    "title": "Purchasing Group Analysis"
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": "Manufacturing Date (HSDAT) Available but Expiry Date (VFDAT) Not Available",
            "cards": [
                {"id": "k1", "label": "Missing Expiry Date Records", "agg": "unique", "source": "message_row_id"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k4", "label": "Vendors Impacted", "agg": "unique", "source": "vendor_account_number"},
                {"id": "k5", "label": "Total Inventory Quantity", "agg": "total_value", "source": "quantity"},
                {"id": "k6", "label": "Inventory Value at Risk", "agg": "total_value", "source": "amount", "format": "currency"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Purchasing Group (EKGRP)", "source": "ekgrp", "all_label": "All Groups"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "name1",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Vendor-wise Missing Expiry Cases"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "plant",
                    "y": "amount",
                    "agg": "sum",
                    "title": "Plant-wise Exposure"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "material_number",
                    "y": "quantity",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Material Analysis"
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
                    "x": "ekgrp",
                    "agg": "count",
                    "title": "Purchasing Group Analysis"
                }
            ]
        },
        {
            "id": "3",
            "label": "Exception 03",
            "title": "Manufacturing Date (HSDAT) Not Available but Expiry Date (VFDAT) Available",
            "cards": [
                {"id": "k1", "label": "Missing Manufacturing Date Records", "agg": "unique", "source": "message_row_id"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k4", "label": "Vendors Impacted", "agg": "unique", "source": "vendor_account_number"},
                {"id": "k5", "label": "Total Inventory Quantity", "agg": "total_value", "source": "quantity"},
                {"id": "k6", "label": "Inventory Value at Risk", "agg": "total_value", "source": "amount", "format": "currency"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Purchasing Group", "source": "ekgrp", "all_label": "All Groups"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "name1",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Vendor-wise Missing Manufacturing Date Cases"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "plant",
                    "y": "amount",
                    "agg": "sum",
                    "title": "Plant-wise Exposure"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "material_number",
                    "y": "quantity",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Material-wise Quantity Analysis"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "expiry_date",
                    "agg": "count",
                    "title": "Expiry Date Distribution"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "ekgrp",
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
        "ekgrp": ["EKGRP"],
        "material_number": ["Material Number"],
        "batch_number": ["Batch Number"],
        "name1": ["NAME1"],
        "quantity": ["Quantity"],
        "amount": ["Amount in Local Currency"],
        "posting_date": ["Posting Date in the Document"],
        "expiry_date": ["Shelf Life Expiration or Best-Before Date"],
        "date": ["Posting Date in the Document"],
        # Helpers
        "message_row_id": ["Message Row ID"]
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
        rf"D:\off\JKC Dashboard\output\MJPR8_Exception{int(exc_id):02}.csv",
        rf"data_files/MJPR8_Exception{int(exc_id):02}.csv"
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
        "EKGRP": "EKGRP",
        "Purchasing Document Date": "Purchasing Document Date",
        "Account Number of Customer": "Account Number of Customer",
        "VAT Registration Number": "VAT Registration Number",
        "Name of Person Who Changed Object": "Name of Person Who Changed Object",
        "Purchasing Document Type": "Purchasing Document Type",
        "Purchasing Document Category": "Purchasing Document Category",
        "Short Description of Purchasing Document Type": "Short Description of Purchasing Document Type",
        "Name 1": "Name 1",
        "Region": "Region",
        "Total_Shelf_Life": "Total_Shelf_Life",
        "Remaining_Shelf_Days": "Remaining_Shelf_Days"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = 0.0 if "Qty" in col or "Quantity" in col or "Amount" in col else ""
            
    # Unique ID helper for exceptions
    row_ids = []
    for idx, _ in df.iterrows():
        row_ids.append(f"Exc{exc_id}_{idx}")
    df["Message Row ID"] = row_ids
    
    return df.fillna('')
