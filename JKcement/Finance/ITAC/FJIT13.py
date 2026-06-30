# Finance/ITAC/FJIT13.py
import pandas as pd
import os

CONFIG = {
    "id": "FJIT13",
    "name": "Payment Has Been Made Against PO Without Adjusting Advance",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Cases Where Payment is Made Against PO Invoice but Advance Remains Open or Unadjusted",
            "cards": [
                {"id": "k1", "label": "Unadjusted Advance Cases", "agg": "row_count"},
                {"id": "k2", "label": "Vendors Impacted", "agg": "unique", "source": "vendor_code"},
                {"id": "k3", "label": "Total Advance Amount", "agg": "total_value", "source": "advance_amount", "format": "currency"},
                {"id": "k4", "label": "Total Invoice Amount", "agg": "total_value", "source": "gross_amount", "format": "currency"},
                {"id": "k5", "label": "Total Final Payments", "agg": "total_value", "source": "fi_amount", "format": "currency"},
                {"id": "k6", "label": "Average Advance Age (Days)", "agg": "avg", "source": "advance_age_days"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Vendor Code", "source": "vendor_code", "all_label": "All Vendors"},
                {"id": "f3", "label": "Vendor Country", "source": "vendor_country", "all_label": "All Countries"},
                {"id": "f4", "label": "Currency", "source": "currency", "all_label": "All Currencies"},
                {"id": "f5", "label": "Special GL Indicator", "source": "special_gl", "all_label": "All Indicators"},
                {"id": "f6", "label": "Fiscal Year", "source": "fiscal_year", "all_label": "All Years"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "vendor_name",
                    "y": "advance_amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Vendor-wise Unadjusted Advance Amount"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "company_name",
                    "y": "advance_amount",
                    "agg": "sum",
                    "title": "Company-wise Advance Exposure"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "advance_date",
                    "y": "advance_amount",
                    "agg": "sum",
                    "time_group": "month",
                    "title": "Monthly Advance Posting Trend"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "po_creator",
                    "y": "po_number",
                    "agg": "count",
                    "top_n": 10,
                    "title": "PO Creator Analysis"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "special_gl",
                    "y": "mm_invoice",
                    "agg": "count",
                    "title": "Special GL Indicator Analysis"
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": "Cases Where Advance Exists but Adjustment Posting Document is Missing",
            "cards": [
                {"id": "k1", "label": "Missing Adjustment Documents", "agg": "unique", "source": "missing_clearing_doc_id"},
                {"id": "k2", "label": "Vendors Impacted", "agg": "unique", "source": "vendor_code"},
                {"id": "k3", "label": "Open Advance Amount", "agg": "total_value", "source": "advance_amount", "format": "currency"},
                {"id": "k4", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k5", "label": "Advance Transactions", "agg": "unique", "source": "fi_invoice"},
                {"id": "k6", "label": "Average Open Advance Age", "agg": "avg", "source": "open_advance_age"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Vendor Code", "source": "vendor_code", "all_label": "All Vendors"},
                {"id": "f3", "label": "Vendor Country", "source": "vendor_country", "all_label": "All Countries"},
                {"id": "f4", "label": "Currency", "source": "currency", "all_label": "All Currencies"},
                {"id": "f5", "label": "Special GL Indicator", "source": "special_gl", "all_label": "All Indicators"},
                {"id": "f6", "label": "Fiscal Year", "source": "fiscal_year", "all_label": "All Years"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "vendor_name",
                    "y": "advance_amount",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Vendor-wise Missing Adjustment Amount"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "company_name",
                    "y": "advance_amount",
                    "agg": "sum",
                    "title": "Company-wise Open Advance Exposure"
                },
                {
                    "id": "c3",
                    "type": "line",
                    "x": "advance_date",
                    "y": "advance_clearing_doc",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Advance Ageing Analysis"
                },
                {
                    "id": "c4",
                    "type": "bar",
                    "x": "vendor_country",
                    "y": "advance_amount",
                    "agg": "sum",
                    "title": "Country-wise Open Advances"
                },
                {
                    "id": "c5",
                    "type": "line",
                    "x": "po_creation_date",
                    "y": "po_number",
                    "agg": "count",
                    "time_group": "month",
                    "title": "PO Creation Trend"
                }
            ]
        }
    ],
    "columns": {
        "company_code": ["Company Code"],
        "vendor_code": ["Vendor Code"],
        "vendor_country": ["Vendor Country"],
        "currency": ["Currency"],
        "special_gl": ["Special_GL_Ind"],
        "fiscal_year": ["Fiscal Year"],
        "vendor_name": ["Vendor Name"],
        "company_name": ["Company"],
        "po_creator": ["PO Creator ID"],
        "po_number": ["PO_Number"],
        "mm_invoice": ["MM Invoice"],
        "fi_invoice": ["FI Invoice"],
        "advance_clearing_doc": ["Advance_Clearing_Doc"],
        "advance_amount": ["Advance_Amount_LC"],
        "gross_amount": ["MM_Gross_Amount"],
        "fi_amount": ["FI_Amount_LC"],
        "advance_date": ["Advance_Posting_Date"],
        "po_creation_date": ["PO Creation Date"],
        "date": ["Advance_Posting_Date"],
        # Helpers
        "advance_age_days": ["Advance Age Days"],
        "missing_clearing_doc_id": ["Missing Clearing Doc ID"],
        "open_advance_age": ["Open Advance Age"]
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
        rf"D:\off\JKC Dashboard\output\FJIT13_Exception{int(exc_id):02}.csv",
        rf"data_files/FJIT13_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to standard schema
    rename_map = {
        "MM Invoice": "MM Invoice",
        "Fiscal Year": "Fiscal Year",
        "MM_Doc_Type": "MM_Doc_Type",
        "MM Doc Date": "MM Doc Date",
        "FI_Posting_Date": "FI_Posting_Date",
        "MM_Entered_By": "MM_Entered_By",
        "Vendor_Ref_Number": "Vendor_Ref_Number",
        "Vendor Code": "Vendor Code",
        "Vendor_Currency": "Vendor_Currency",
        "MM_Gross_Amount": "MM_Gross_Amount",
        "PO_Number": "PO_Number",
        "Final_Payment_Doc": "Final_Payment_Doc",
        "Final_Payment_Date": "Final_Payment_Date",
        "FI_Amount_LC": "FI_Amount_LC",
        "Advance_Clearing_Doc": "Advance_Clearing_Doc",
        "Advance_Clearing_Date": "Advance_Clearing_Date",
        "FI Invoice": "FI Invoice",
        "FI_Doc_Type": "FI_Doc_Type",
        "Advance_Posting_Date": "Advance_Posting_Date",
        "Advance_Amount_LC": "Advance_Amount_LC",
        "Special_GL_Ind": "Special_GL_Ind",
        "Exception": "Exception",
        "Vendor Country": "Vendor Country",
        "Vendor Name": "Vendor Name",
        "Vendor City": "Vendor City",
        "PO Creator ID": "PO Creator ID",
        "PO Creation Date": "PO Creation Date",
        "Company Code": "Company Code",
        "Company": "Company",
        "Company City": "Company City",
        "Company Country": "Company Country",
        "Currency": "Currency"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = 0.0 if "LC" in col or "Amount" in col else ""
            
    # Parse numbers to float
    for c in ["Advance_Amount_LC", "MM_Gross_Amount", "FI_Amount_LC"]:
        df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0.0)
        
    # Calculate helpers for Exception 01
    if int(exc_id) == 1:
        age_days = []
        for idx, row in df.iterrows():
            pay_dt = str(row.get("Final_Payment_Date", "")).strip()
            adv_dt = str(row.get("Advance_Posting_Date", "")).strip()
            try:
                p_val = pd.to_datetime(pay_dt, errors='coerce')
                a_val = pd.to_datetime(adv_dt, errors='coerce')
                if pd.notna(p_val) and pd.notna(a_val):
                    age_days.append(float(max(0, (p_val - a_val).days)))
                else:
                    age_days.append(0.0)
            except Exception:
                age_days.append(0.0)
        df["Advance Age Days"] = age_days
        
    # Calculate helpers for Exception 02
    elif int(exc_id) == 2:
        missing_ids = []
        open_ages = []
        current_date = pd.to_datetime('2026-06-29')
        
        for idx, row in df.iterrows():
            clearing = str(row.get("Advance_Clearing_Doc", "")).strip()
            fi_inv = str(row.get("FI Invoice", "")).strip()
            adv_dt = str(row.get("Advance_Posting_Date", "")).strip()
            
            if not clearing or clearing == "0" or clearing == "nan":
                missing_ids.append(fi_inv if fi_inv else f"FI_{idx}")
            else:
                missing_ids.append("")
                
            try:
                a_val = pd.to_datetime(adv_dt, errors='coerce')
                if pd.notna(a_val):
                    open_ages.append(float(max(0, (current_date - a_val).days)))
                else:
                    open_ages.append(0.0)
            except Exception:
                open_ages.append(0.0)
                
        df["Missing Clearing Doc ID"] = missing_ids
        df["Open Advance Age"] = open_ages
        
    return df.fillna('')
