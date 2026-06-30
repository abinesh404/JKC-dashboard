# Manufacturing/Others/MJOT11.py
import pandas as pd
import os

CONFIG = {
    "id": "MJOT11",
    "name": "Scrap Sales Procedure Audit",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Same Plant Scrap Sales Pricing Deviation",
            "cards": [
                {"id": "k1", "label": "Scrap Sale Transactions", "agg": "unique", "source": "billing_doc_num"},
                {"id": "k2", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k3", "label": "Materials Impacted", "agg": "unique", "source": "material_number"},
                {"id": "k4", "label": "Total Scrap Sales Value", "agg": "total_value", "source": "net_lc", "format": "currency"},
                {"id": "k5", "label": "Total Price Impact", "agg": "total_value", "source": "impact", "format": "currency"},
                {"id": "k6", "label": "Average Variation %", "agg": "avg", "source": "variation_pct", "format": "percentage"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Material Number", "source": "material_number", "all_label": "All Materials"},
                {"id": "f4", "label": "Billing Month", "source": "billing_month", "all_label": "All Months"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "plant",
                    "y": "net_lc",
                    "agg": "sum",
                    "title": "Plant-wise Scrap Sales Value"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "material_number",
                    "y": "variation_pct",
                    "agg": "avg",
                    "top_n": 10,
                    "title": "Material-wise Price Variation"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "material_number",
                    "y": "net_value",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Top Scrap Materials by Revenue"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "billing_month",
                    "y": "net_lc",
                    "agg": "sum",
                    "title": "Monthly Scrap Sales Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "sold_to_party",
                    "y": "net_lc",
                    "agg": "sum",
                    "top_n": 10,
                    "title": "Customer-wise Scrap Sales Analysis"
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": "Scrap Sales Across All Plants Pricing Deviation",
            "cards": [
                {"id": "k1", "label": "Scrap Sale Transactions", "agg": "unique", "source": "billing_doc_num"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company_code"},
                {"id": "k3", "label": "Plants Impacted", "agg": "unique", "source": "plant"},
                {"id": "k4", "label": "Total Scrap Revenue", "agg": "total_value", "source": "net_lc", "format": "currency"},
                {"id": "k5", "label": "Total Financial Impact", "agg": "total_value", "source": "impact", "format": "currency"},
                {"id": "k6", "label": "Average Price Variation %", "agg": "avg", "source": "variation_pct", "format": "percentage"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company_code", "all_label": "All Companies"},
                {"id": "f2", "label": "Plant", "source": "plant", "all_label": "All Plants"},
                {"id": "f3", "label": "Sales Organization", "source": "sales_org", "all_label": "All Orgs"},
                {"id": "f4", "label": "Material Number", "source": "material_number", "all_label": "All Materials"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "plant",
                    "y": "net_lc",
                    "agg": "sum",
                    "title": "Plant-wise Scrap Revenue Comparison"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "plant",
                    "y": "price_diff",
                    "agg": "avg",
                    "title": "Cross-Plant Price Variation Analysis"
                },
                {
                    "id": "c3",
                    "type": "bar",
                    "x": "material_number",
                    "y": "net_price_unit",
                    "agg": "avg",
                    "top_n": 10,
                    "title": "Material-wise Scrap Price Comparison"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "billing_month",
                    "y": "net_value",
                    "agg": "sum",
                    "title": "Monthly Scrap Sales Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "sales_org",
                    "y": "net_lc",
                    "agg": "sum",
                    "title": "Sales Organization Analysis"
                }
            ]
        }
    ],
    "columns": {
        "company_code": ["Company Code"],
        "plant": ["Plant"],
        "material_number": ["Material Number"],
        "sales_org": ["Sales Organization"],
        "billing_month": ["Billing Month"],
        "billing_doc_num": ["Billing Document Number"],
        "net_lc": ["Net_LC"],
        "net_value": ["Net Value"],
        "net_price_unit": ["Net_Price_Unit"],
        "price_diff": ["Price_Diff"],
        "impact": ["Impact"],
        "variation_pct": ["Variation_%"],
        "sold_to_party": ["Sold-to Party"],
        "date": ["Billing Date"]
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
        rf"D:\off\JKC Dashboard\output\MJOT11_Exception{int(exc_id):02}.csv",
        rf"data_files/MJOT11_Exception{int(exc_id):02}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
        
    df = pd.read_csv(path, encoding='latin1', low_memory=False)
    df.columns = [str(c).strip() for c in df.columns]
    
    # Rename columns to standard schema
    rename_map = {
        "Company Code": "Company Code",
        "Company Name": "Company Name",
        "Plant": "Plant",
        "City": "City",
        "Country Key": "Country Key",
        "Language Key": "Language Key",
        "Chart of Accounts": "Chart of Accounts",
        "Material Type": "Material Type",
        "Billing Category": "Billing Category",
        "Billing Type": "Billing Type",
        "Document Category": "Document Category",
        "Document Currency": "Document Currency",
        "Sales Organization": "Sales Organization",
        "Distribution Channel": "Distribution Channel",
        "Pricing Procedure": "Pricing Procedure",
        "Pricing Document Number": "Pricing Document Number",
        "Exchange Rate for FI Posting": "Exchange Rate for FI Posting",
        "Payment Terms": "Payment Terms",
        "Customer Account Assignment Group": "Customer Account Assignment Group",
        "Created the Record": "Created the Record",
        "Time of Creation": "Time of Creation",
        "Date of Creation": "Date of Creation",
        "Payer": "Payer",
        "Sold-to Party": "Sold-to Party",
        "Cancellation Billing Document": "Cancellation Billing Document",
        "Credit Memo Currency": "Credit Memo Currency",
        "Billing Document Cancelled Indicator": "Billing Document Cancelled Indicator",
        "Item Number": "Item Number",
        "Sales Unit": "Sales Unit",
        "Numerator for Conversion to Base Unit": "Numerator for Conversion to Base Unit",
        "Denominator for Conversion to Base Unit": "Denominator for Conversion to Base Unit",
        "Material Number": "Material Number",
        "Unit of Measure": "Unit of Measure",
        "Exchange Rate for Pricing": "Exchange Rate for Pricing",
        "Short Text for Sales Document Item": "Short Text for Sales Document Item",
        "Batch Number": "Batch Number",
        "Billing Document Number": "Billing Document Number",
        "Billing Quantity": "Billing Quantity",
        "Billing Date": "Billing Date",
        "Billing Month": "Billing Month",
        "Net Value": "Net Value",
        "Net_LC": "Net_LC",
        "Net_Price_Unit": "Net_Price_Unit",
        "Avg_Net Price": "Avg_Net Price",
        "MAX_Net Price": "MAX_Net Price",
        "Price_Diff": "Price_Diff",
        "Impact": "Impact",
        "Avg_Impact": "Avg_Impact",
        "Variation_%": "Variation_%"
    }
    df = df.rename(columns=rename_map)
    
    # Ensure all required standard columns exist
    for col in rename_map.values():
        if col not in df.columns:
            df[col] = 0.0 if "Net" in col or "Price" in col or "Diff" in col or "Impact" in col or "Variation" in col or "Qty" in col or "Quantity" in col else ""
            
    return df.fillna('')
