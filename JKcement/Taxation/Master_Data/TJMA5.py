# Taxation/Master_Data/TJMA5.py
import pandas as pd
import os

CONFIG = {
    "id": "TJMA5",
    "name": "Customer Reconciliation Account Not Defined",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Cases Where the Customer is Active but Has No Reconciliation Account Defined",
            "cards": [
                {"id": "k1", "label": "Customers Without Recon Account", "agg": "unique", "source": "customer_number"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Active Customers", "agg": "unique", "source": "active_customer_id"},
                {"id": "k4", "label": "Outstanding Balance", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Customers with Transactions", "agg": "unique", "source": "accounting_doc_num"},
                {"id": "k6", "label": "High Risk Customers", "agg": "unique", "source": "high_risk_customer_id"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Customer Number", "source": "customer_number", "all_label": "All Customers"},
                {"id": "f3", "label": "Region", "source": "region", "all_label": "All Regions"},
                {"id": "f4", "label": "Terms of Payment Key", "source": "payment_terms", "all_label": "All Payment Terms"},
                {"id": "f5", "label": "Document Status", "source": "doc_status", "all_label": "All Statuses"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "company_code",
                    "agg": "count",
                    "title": "Company-wise Missing Reconciliation Accounts"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "region",
                    "agg": "count",
                    "title": "Region-wise Customer Distribution"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "name1",
                    "y": "amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Customer Outstanding Exposure"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "posting_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Transaction Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "payment_terms",
                    "agg": "count",
                    "title": "Payment Terms Analysis"
                }
            ]
        }
    ],
    "columns": {
        "company_code": ["Company Code"],
        "customer_number": ["Customer Number"],
        "region": ["Region"],
        "payment_terms": ["Terms of Payment Key"],
        "doc_status": ["Document Status"],
        "name1": ["Name1"],
        "amount": ["Amount in Local Currency"],
        "accounting_doc_num": ["Accounting Document Number"],
        "posting_date": ["Posting Date in the Document"],
        "date": ["Posting Date in the Document"],
        # Helpers
        "active_customer_id": ["Active Customer ID"],
        "high_risk_customer_id": ["High Risk Customer ID"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Master_Data"
    }

def get_data(exc_id):
    paths = [
        rf"D:\off\JKC Dashboard\output\TJMA5_Exception{int(exc_id):02}.csv",
        rf"data_files/TJMA5_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to standard schema
    rename_map = {
        "Customer Number": "Customer Number",
        "Company Code": "Company Code",
        "Name of Person Created  Object": "Name of Person Created  Object",
        "Date on Record Created": "Date on Record Created",
        "Central posting block": "Central posting block",
        "Deletion Flag for Master Record": "Deletion Flag for Master Record",
        "Reconciliation Account in General Ledger": "Reconciliation Account in General Ledger",
        "Block Key for Payment": "Block Key for Payment",
        "Terms of Payment Key": "Terms of Payment Key",
        "Name1": "Name1",
        "City": "City",
        "Region": "Region",
        "Account Number of Vendor": "Account Number of Vendor",
        "Tax Number 1": "Tax Number 1",
        "VAT Registration Number": "VAT Registration Number",
        "Document Number of the Clearing Document": "Document Number of the Clearing Document",
        "Fiscal Year": "Fiscal Year",
        "Accounting Document Number": "Accounting Document Number",
        "Num. Line Item Within Acc. Doc.": "Num. Line Item Within Acc. Doc.",
        "Posting Date in the Document": "Posting Date in the Document",
        "Document Date in Document": "Document Date in Document",
        "Day Accounting Document Entered": "Day Accounting Document Entered",
        "Currency Key": "Currency Key",
        "Reference Document Number": "Reference Document Number",
        "Document Type": "Document Type",
        "Debit/Credit Indicator": "Debit/Credit Indicator",
        "Amount in Local Currency": "Amount in Local Currency",
        "General Ledger Account": "General Ledger Account",
        "Payment Block Key": "Payment Block Key",
        "Document Status": "Document Status"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = 0.0 if "Amount" in col else ""
            
    # Calculate active and high risk helper columns
    active_custs = []
    high_risk_custs = []
    
    for idx, row in df.iterrows():
        cust = str(row.get("Customer Number", "")).strip()
        block = str(row.get("Central posting block", "")).strip()
        delflag = str(row.get("Deletion Flag for Master Record", "")).strip()
        acct_doc = str(row.get("Accounting Document Number", "")).strip()
        
        # Active: block and delflag are blank
        if not block and not delflag:
            active_custs.append(cust)
        else:
            active_custs.append("")
            
        # High Risk: Has transactions (accounting doc exists) but missing reconciliation account (all here are missing)
        if acct_doc:
            high_risk_custs.append(cust)
        else:
            high_risk_custs.append("")
            
    df["Active Customer ID"] = active_custs
    df["High Risk Customer ID"] = high_risk_custs
    
    return df.fillna('')
