# Supplier/master_data/SJMA45.py
import pandas as pd
import os

CONFIG = {
    "id": "SJMA45",
    "name": "Variation in Payment terms in Invoice vs Masters",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Variation in Payment Terms in Invoice vs Master",
            "cards": [
                {"id": "k1", "label": "Customers Impacted", "agg": "unique", "source": "customer"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Billing Documents", "agg": "unique", "source": "billing_doc"},
                {"id": "k4", "label": "Total Invoice Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Average Overdue Days", "agg": "avg", "source": "overdue_days"},
                {"id": "k6", "label": "Payment Term Variations", "agg": "total_rows"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Customer", "source": "customer"},
                {"id": "f3", "label": "Payment Terms (Invoice)", "source": "pay_terms_inv"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company_name", "agg": "count", "title": "Company-wise Payment Term Variations"},
                {"id": "c2", "type": "bar", "x": "customer_name", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Top Customers by Invoice Amount"},
                {"id": "c3", "type": "doughnut", "x": "ageing_bracket", "agg": "count", "title": "Ageing Bracket Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "payment_date", "agg": "count", "time_group": "month", "title": "Monthly Payment Term Variation Trend"},
                {"id": "c5", "type": "bar", "x": "pay_terms_inv", "y": "overdue_days", "agg": "avg", "title": "Payment Term Difference Analysis"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Name", "Company Code"],
        "company_name": ["Company Name"],
        "customer": ["Customer Name", "Customer Number"],
        "customer_name": ["Customer Name"],
        "billing_doc": ["Billing Document"],
        "amount": ["Amount in Local Currency"],
        "overdue_days": ["Overdue_Days"],
        "pay_terms_inv": ["Terms of Payment Key (Invoice)"],
        "ageing_bracket": ["Ageing Bracket"],
        "payment_date": ["Payment Date"],
        "date": ["Payment Date", "Clearing Date", "Baseline Date for Due Date Calculation", "Net Due Date", "Net Due Date as per Customer Master"],
        "user": ["Name of Person who Created the Object"],
        "document": ["Accounting Document Number", "Billing Document"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Supplier Master Data"
    }

def get_data(exc_id):
    paths = [
        f"data_files/SJMA45_Exception0{exc_id}.csv",
        f"data_files/SJMA45_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
