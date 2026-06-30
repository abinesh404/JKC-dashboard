# Taxation/GST/TJGS1.py
import pandas as pd
import os

CONFIG = {
    "id": "TJGS1",
    "name": "GST - Identify Instances Where Payment Made Beyond 180 Days from Invoice Date",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Instances Where Payment Has Been Made After 180 Days from the Invoice Date and Resultant Interest Loss on GST",
            "cards": [
                {"id": "k1", "label": "Delayed GST Payments", "agg": "unique", "source": "accounting_document_number"},
                {"id": "k2", "label": "Vendors Impacted", "agg": "unique", "source": "vendor"},
                {"id": "k3", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k4", "label": "Total GST Amount", "agg": "total_value", "source": "gst_amount", "format": "currency"},
                {"id": "k5", "label": "Total Interest Loss", "agg": "total_value", "source": "interest_loss", "format": "currency"},
                {"id": "k6", "label": "Average Delay Days", "agg": "avg", "source": "days_delay"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Vendor", "source": "vendor", "all_label": "All Vendors"},
                {"id": "f3", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f4", "label": "GST Status", "source": "gst_status", "all_label": "All Statuses"},
                {"id": "f5", "label": "User Name", "source": "user_name", "all_label": "All Users"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "vendor",
                    "y": "interest_loss",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Vendor-wise Interest Loss"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "name_of_company",
                    "y": "gst_amount",
                    "agg": "sum",
                    "title": "Company-wise GST Exposure"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "days_delay",
                    "agg": "count",
                    "title": "Delay Bucket Analysis"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "posting_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Delayed Payment Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "plant",
                    "y": "interest_loss",
                    "agg": "sum",
                    "title": "Plant-wise GST Interest Exposure"
                }
            ]
        }
    ],
    "columns": {
        "company_code": ["Company Code"],
        "vendor": ["Vendor"],
        "plant": ["Plant"],
        "gst_status": ["GST_STATUS"],
        "user_name": ["User name"],
        "accounting_document_number": ["Accounting Document Number"],
        "gst_amount": ["GST_Amount"],
        "interest_loss": ["Interest_Loss"],
        "days_delay": ["Days_Delay"],
        "name_of_company": ["Name of Company"],
        "posting_date": ["Posting Date in the Document"],
        "date": ["Posting Date in the Document"]
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
        rf"D:\off\JKC Dashboard\output\TJGS1_Exception{int(exc_id):02}.csv",
        rf"data_files/TJGS1_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to standard schema
    rename_map = {
        "Document Number of the Clearing Document": "Document Number of the Clearing Document",
        "Clearing Entry Date": "Clearing Entry Date",
        "Clearing Date": "Clearing Date",
        "Reference Key": "Reference Key",
        "Accounting Document Number": "Accounting Document Number",
        "Posting Key": "Posting Key",
        "Company Code": "Company Code",
        "Number of Line Item Within Accounting Document": "Number of Line Item Within Accounting Document",
        "Identification of the Line Item": "Identification of the Line Item",
        "Amount in Local Currency": "Amount in Local Currency",
        "Fiscal Year": "Fiscal Year",
        "Doc Type_Bseg": "Doc Type_Bseg",
        "General Ledger Account": "General Ledger Account",
        "Vendor": "Vendor",
        "Due On": "Due On",
        "Debit/Credit Indicator": "Debit/Credit Indicator",
        "Billing Document": "Billing Document",
        "Plant": "Plant",
        "Amount in document currency": "Amount in document currency",
        "Days_Delay": "Days_Delay",
        "Name of Company": "Name of Company",
        "City": "City",
        "Country Key": "Country Key",
        "Language Key": "Language Key",
        "VAT Registration Number": "VAT Registration Number",
        "Document Type_Bkpf": "Document Type_Bkpf",
        "Document Date in Document": "Document Date in Document",
        "Posting Date in the Document": "Posting Date in the Document",
        "Day On Which Accounting Document Was Entered": "Day On Which Accounting Document Was Entered",
        "Transaction Code": "Transaction Code",
        "User name": "User name",
        "G/L Account Number": "G/L Account Number",
        "G/L Account Description": "G/L Account Description",
        "GST_STATUS": "GST_STATUS",
        "GST_Amount": "GST_Amount",
        "Interest_Loss": "Interest_Loss"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = 0.0 if "Amount" in col or "Loss" in col or "Delay" in col else ""
            
    return df.fillna('')
