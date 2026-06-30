# Taxation/GST/TJGS4.py
import pandas as pd
import os

CONFIG = {
    "id": "TJGS4",
    "name": "GST Duplicate Invoices",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "GST Duplicate Invoices",
            "cards": [
                {"id": "k1", "label": "Duplicate GST Invoices", "agg": "unique", "source": "doc_no"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "rec_co_code"},
                {"id": "k3", "label": "Users Involved", "agg": "unique", "source": "user_name"},
                {"id": "k4", "label": "Duplicate Invoice Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Reversed Duplicate Invoices", "agg": "unique", "source": "reversed_dup_invoices"},
                {"id": "k6", "label": "Open Duplicate Invoices", "agg": "unique", "source": "open_dup_invoices"}
            ],
            "filters": [
                {"id": "f1", "label": "Fiscal Year", "source": "fiscal_year", "all_label": "All Years"},
                {"id": "f2", "label": "User Name", "source": "user_name", "all_label": "All Users"},
                {"id": "f3", "label": "Currency", "source": "currency", "all_label": "All Currencies"},
                {"id": "f4", "label": "Document Type", "source": "type", "all_label": "All Types"},
                {"id": "f5", "label": "Reversal Flag", "source": "reversal_flag", "all_label": "All Statuses"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "fiscal_year",
                    "agg": "count",
                    "title": "Fiscal Year-wise Duplicate Invoices"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "user_name",
                    "agg": "count",
                    "top_n": 10,
                    "title": "User-wise Duplicate Invoice Posting"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "days_difference",
                    "agg": "count",
                    "title": "Duplicate Invoice Age Analysis"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "pstng_date",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Duplicate Invoice Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "reversal_flag",
                    "agg": "count",
                    "title": "Reversal Status Analysis"
                }
            ]
        }
    ],
    "columns": {
        "fiscal_year": ["Fiscal Year"],
        "user_name": ["User Name"],
        "currency": ["currency"],
        "type": ["Type"],
        "reversal_flag": ["Reversal Flag"],
        "doc_no": ["Doc No"],
        "rec_co_code": ["Rec Co Code"],
        "days_difference": ["Days_Difference"],
        "pstng_date": ["Pstng Date"],
        "date": ["Pstng Date"],
        "amount": ["Amount"],
        # Helpers
        "reversed_dup_invoices": ["Reversed Dup Invoices"],
        "open_dup_invoices": ["Open Dup Invoices"]
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
        rf"D:\off\JKC Dashboard\output\TJGS4_Exception{int(exc_id):02}.csv",
        rf"data_files/TJGS4_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to standard schema
    rename_map = {
        "Doc No": "Doc No",
        "Document Header Text": "Document Header Text",
        "Purch.Doc.": "Purch.Doc.",
        "Grouping Key": "Grouping Key",
        "Object key": "Object key",
        "Type": "Type",
        "Period": "Period",
        "Parked By": "Parked By",
        "Doc..Date": "Doc..Date",
        "Pstng Date": "Pstng Date",
        "Entry Date": "Entry Date",
        "Time": "Time",
        "Rec Ent Doc": "Rec Ent Doc",
        "Rec Co Code": "Rec Co Code",
        "Rec Year": "Rec Year",
        "Exch. rate": "Exch. rate",
        "Reversal_": "Reversal_",
        "Reason": "Reason",
        "Revers. Dte": "Revers. Dte",
        "User Name": "User Name",
        "currency": "currency",
        "Reference": "Reference",
        "Reversal": "Reversal",
        "Rve": "Rve",
        "RvD": "RvD",
        "Reversal Flag": "Reversal Flag",
        "Days_Difference": "Days_Difference",
        "Rev. Org.": "Rev. Org.",
        "Rev. Ref.": "Rev. Ref.",
        "Fiscal Year": "Fiscal Year"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = ""
            
    df["Amount"] = 0.0
    
    # Calculate reversed/open duplicate helpers
    rev_dup = []
    open_dup = []
    for idx, row in df.iterrows():
        doc = str(row.get("Doc No", "")).strip()
        flag = str(row.get("Reversal Flag", "")).strip().lower()
        
        if flag == "yes":
            rev_dup.append(doc)
            open_dup.append("")
        else:
            rev_dup.append("")
            open_dup.append(doc)
            
    df["Reversed Dup Invoices"] = rev_dup
    df["Open Dup Invoices"] = open_dup
    
    return df.fillna('')
