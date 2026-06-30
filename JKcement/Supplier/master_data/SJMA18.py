# Supplier/master_data/SJMA18.py
import pandas as pd
import os

CONFIG = {
    "id": "SJMA18",
    "name": "Vendor Bank Information Changed for Releasing the Payment and After Payout the Original Details Updated - II",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Vendor Bank Information Changed for Releasing the Payment",
            "cards": [
                {"id": "k1", "label": "Vendors Affected", "agg": "unique", "source": "vendor"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Bank Detail Changes", "agg": "unique", "source": "change_num"},
                {"id": "k4", "label": "Payments Released", "agg": "unique", "source": "document"},
                {"id": "k5", "label": "Total Payment Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k6", "label": "Users Performing Changes", "agg": "unique", "source": "user"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "User Name", "source": "user"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise Bank Detail Changes"},
                {"id": "c2", "type": "bar", "x": "vendor", "agg": "count", "top_n": 10, "horizontal": True, "title": "Top Vendors with Bank Detail Changes"},
                {"id": "c3", "type": "doughnut", "x": "change_type", "agg": "count", "title": "Bank Change Type Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Monthly Bank Change Trend"},
                {"id": "c5", "type": "bar", "x": "user", "agg": "count", "title": "Users Performing Bank Changes"}
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": "Vendor Bank Information Changed for Payment and Restored After Payout",
            "cards": [
                {"id": "k1", "label": "Vendors Affected", "agg": "unique", "source": "vendor"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Bank Details Restored", "agg": "unique", "source": "change_num"},
                {"id": "k4", "label": "Payments Released", "agg": "unique", "source": "document"},
                {"id": "k5", "label": "Total Payment Amount", "agg": "total_value", "source": "amount", "format": "currency"},
                {"id": "k6", "label": "High Risk Changes", "agg": "total_rows"}
            ],
            "filters": [
                {"id": "f1", "label": "Company", "source": "company"},
                {"id": "f2", "label": "Vendor", "source": "vendor"},
                {"id": "f3", "label": "User Name", "source": "user"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise Temporary Bank Changes"},
                {"id": "c2", "type": "bar", "x": "vendor", "agg": "count", "top_n": 10, "horizontal": True, "title": "Vendors with Multiple Bank Changes"},
                {"id": "c3", "type": "doughnut", "x": "change_type", "agg": "count", "title": "Change Type Distribution", "legend": True},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Monthly Temporary Bank Change Trend"},
                {"id": "c5", "type": "bar", "x": "user", "agg": "count", "title": "Users Performing Temporary Bank Changes"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Description", "Company Code"],
        "vendor": ["Vendor Name", "Vendor Code"],
        "user": ["User name of the person responsible in change document", "Name of Person who Created the Object"],
        "change_type": ["Change Type (U, I, S, D)", "Application object change type (U, I, E, D)"],
        "date": ["Creation date of the change document", "Creation date of the change document (Change 2)"],
        "amount": ["Amount in Local Currency"],
        "document": ["Accounting Document Number", "Document Number of the Clearing Document"],
        "bank_acc": ["Bank account number"],
        "change_num": ["Document change number"]
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
        f"data_files/SJMA18_Exception0{exc_id}.csv",
        f"data_files/SJMA18_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
