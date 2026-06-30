# Taxation/GST/TJGS3.py
import pandas as pd
import os

CONFIG = {
    "id": "TJGS3",
    "name": "GST Interest Loss Due to Non Payment",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Identify Unpaid GST Invoices Beyond 180 Days and Compute the Resulting GST Interest Loss",
            "cards": [
                {"id": "k1", "label": "Unpaid GST Invoices >180 Days", "agg": "unique", "source": "accounting_doc_num"},
                {"id": "k2", "label": "Vendors Impacted", "agg": "unique", "source": "vendor"},
                {"id": "k3", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k4", "label": "Total GST Amount", "agg": "total_value", "source": "gst_amount", "format": "currency"},
                {"id": "k5", "label": "Total Interest Loss", "agg": "total_value", "source": "interest_loss", "format": "currency"},
                {"id": "k6", "label": "Average Delay Days", "agg": "avg", "source": "days_delay"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Vendor", "source": "vendor", "all_label": "All Vendors"},
                {"id": "f3", "label": "GST Status", "source": "gst_status", "all_label": "All Statuses"},
                {"id": "f4", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f5", "label": "Fiscal Year", "source": "fiscal_year", "all_label": "All Years"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "vendor",
                    "y": "interest_loss",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Vendor-wise GST Interest Loss"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "company_code",
                    "y": "gst_amount",
                    "agg": "sum",
                    "title": "Company-wise GST Exposure"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "days_delay",
                    "agg": "count",
                    "title": "Delay Analysis"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "posting_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Trend of Delayed GST Invoices"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "plant",
                    "y": "interest_loss",
                    "agg": "sum",
                    "title": "Plant-wise GST Risk Exposure"
                }
            ]
        }
    ],
    "columns": {
        "company_code": ["Company Code"],
        "vendor": ["Vendor"],
        "gst_status": ["GST_STATUS"],
        "plant": ["Plant"],
        "fiscal_year": ["Fiscal Year"],
        "accounting_doc_num": ["Accounting Document Number"],
        "gst_amount": ["GST_Amount"],
        "interest_loss": ["Interest_Loss"],
        "days_delay": ["Days_Delay"],
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
        rf"D:\off\JKC Dashboard\output\TJGS3_Exception{int(exc_id):02}.csv",
        rf"data_files/TJGS3_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to standard schema
    rename_map = {
        "Company Code": "Company Code",
        "Vendor": "Vendor",
        "Clearing Date": "Clearing Date",
        "Document Number of the Clearing Document": "Document Number of the Clearing Document",
        "Fiscal Year": "Fiscal Year",
        "Accounting Document Number": "Accounting Document Number",
        "Number of Line Item Within Accounting Document": "Number of Line Item Within Accounting Document",
        "Posting Date in the Document": "Posting Date in the Document",
        "Document Date in Document": "Document Date in Document",
        "Day On Which Accounting Document Was Entered": "Day On Which Accounting Document Was Entered",
        "Currency": "Currency",
        "Doc Type_Bseg": "Doc Type_Bseg",
        "Posting Key": "Posting Key",
        "Debit/Credit Indicator": "Debit/Credit Indicator",
        "Amount in Local Currency": "Amount in Local Currency",
        "Amount in document currency": "Amount in document currency",
        "General Ledger Account": "General Ledger Account",
        "Identification of the Line Item": "Identification of the Line Item",
        "Days_Delay": "Days_Delay",
        "City": "City",
        "Country Key": "Country Key",
        "Language Key": "Language Key",
        "VAT Registration Number": "VAT Registration Number",
        "Clearing Entry Date": "Clearing Entry Date",
        "Reference Key": "Reference Key",
        "Due On": "Due On",
        "Billing Document": "Billing Document",
        "Plant": "Plant",
        "G/L Account Number": "G/L Account Number",
        "G/L Account Description": "G/L Account Description",
        "RCM_FLAG": "RCM_FLAG",
        "Amount_LC_Corrected": "Amount_LC_Corrected",
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
