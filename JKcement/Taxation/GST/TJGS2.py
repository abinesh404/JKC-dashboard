# Taxation/GST/TJGS2.py
import pandas as pd
import os

CONFIG = {
    "id": "TJGS2",
    "name": "GST Query",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Cases Where GST Invoices Have the Same Vendor Invoice Number (Reference Number) in the Same Fiscal Year",
            "cards": [
                {"id": "k1", "label": "Duplicate GST Invoices", "agg": "unique", "source": "accounting_doc_num"},
                {"id": "k2", "label": "Vendors Impacted", "agg": "unique", "source": "vendor_code"},
                {"id": "k3", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k4", "label": "Total GST Amount", "agg": "total_value", "source": "total_gst", "format": "currency"},
                {"id": "k5", "label": "Duplicate Invoice Amount", "agg": "total_value", "source": "dup_inv_amt", "format": "currency"},
                {"id": "k6", "label": "Fiscal Years Impacted", "agg": "unique", "source": "fiscal_year"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Vendor Code", "source": "vendor_code", "all_label": "All Vendors"},
                {"id": "f3", "label": "Fiscal Year", "source": "fiscal_year", "all_label": "All Years"},
                {"id": "f4", "label": "User Name", "source": "user_name", "all_label": "All Users"},
                {"id": "f5", "label": "Account Group", "source": "account_group", "all_label": "All Groups"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "vendor_name",
                    "y": "reference",
                    "agg": "count",
                    "top_n": 10,
                    "title": "Vendor Duplicate Analysis"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "company_desc",
                    "y": "total_gst",
                    "agg": "sum",
                    "title": "Company Exposure"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "fiscal_year",
                    "agg": "count",
                    "title": "Fiscal Year Trend"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "user_name",
                    "agg": "count",
                    "top_n": 10,
                    "title": "User Analysis"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "gl_long_text",
                    "y": "total_gst",
                    "agg": "sum",
                    "title": "GST Component Analysis"
                }
            ]
        }
    ],
    "columns": {
        "company_code": ["Company Code"],
        "company_desc": ["Company Description"],
        "vendor_code": ["Vendor Code"],
        "vendor_name": ["Vendor Name"],
        "fiscal_year": ["Fiscal Year"],
        "user_name": ["User Name"],
        "account_group": ["Account group"],
        "accounting_doc_num": ["Accounting Document Number"],
        "total_gst": ["Total GST"],
        "dup_inv_amt": ["Duplicate Invoice Amount"],
        "reference": ["Reference"],
        "gl_long_text": ["G/L Account Long Text"],
        "date": ["Posting Date"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "GST"
    }

def get_data(exc_id):
    paths = [
        rf"D:\off\JKC Dashboard\output\TJGS2_Exception{int(exc_id):02}.csv",
        rf"data_files/TJGS2_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to standard schema
    rename_map = {
        "Company Code": "Company Code",
        "Company Description": "Company Description",
        "Company City": "Company City",
        "Accounting Document Number": "Accounting Document Number",
        "Document Date": "Document Date",
        "Document type": "Document type",
        "Posting Date": "Posting Date",
        "Fiscal Year": "Fiscal Year",
        "Vendor Code": "Vendor Code",
        "Vendor Name": "Vendor Name",
        "Vendor City": "Vendor City",
        "Account group": "Account group",
        "Account Type": "Account Type",
        "Account Description": "Account Description",
        "G/L": "G/L",
        "G/L Account Long Text": "G/L Account Long Text",
        "Reference": "Reference",
        "Currency Key": "Currency Key",
        "ITC-CGST": "ITC-CGST",
        "ITC-SGST": "ITC-SGST",
        "ITC-IGST": "ITC-IGST",
        "Total GST": "Total GST",
        "User Name": "User Name",
        "Item Text": "Item Text",
        "Search Term for Matchcode Search": "Search Term for Matchcode Search"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = 0.0 if "GST" in col or "ITC" in col else ""
            
    # Calculate Duplicate Invoice Amount (ITC-CGST + ITC-SGST + ITC-IGST)
    cgst = pd.to_numeric(df["ITC-CGST"], errors='coerce').fillna(0)
    sgst = pd.to_numeric(df["ITC-SGST"], errors='coerce').fillna(0)
    igst = pd.to_numeric(df["ITC-IGST"], errors='coerce').fillna(0)
    df["Duplicate Invoice Amount"] = cgst + sgst + igst
    
    return df.fillna('')
