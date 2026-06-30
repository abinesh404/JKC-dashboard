# Supplier/invoice/SJIN41.py
import pandas as pd
import os

CONFIG = {
    "id": "SJIN41",
    "name": "PO Change After GRN",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "PO Changes After GRN",
            "cards": [
                {"id": "k1", "label": "Changed POs", "agg": "unique", "source": "po"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Vendors Impacted", "agg": "unique", "source": "vendor"},
                {"id": "k4", "label": "Total PO Value Changed", "agg": "sum", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Average Days After GRN", "agg": "avg", "source": "days_after_grn"},
                {"id": "k6", "label": "Fields Changed", "agg": "unique", "source": "field_description"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company", "all_label": "All Companies"},
                {"id": "f2", "label": "Vendor Code", "source": "vendor", "all_label": "All Vendors"},
                {"id": "f3", "label": "Purchasing Group", "source": "purchasing_group", "all_label": "All Purchasing Groups"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise PO Changes After GRN"},
                {"id": "c2", "type": "bar", "x": "vendor_name", "agg": "count", "top_n": 10, "horizontal": True, "title": "Top Vendors with PO Changes"},
                {"id": "c3", "type": "bar", "x": "field_description", "agg": "count", "title": "Field Change Distribution"},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Monthly PO Change Trend"},
                {"id": "c5", "type": "bar", "x": "purchasing_group", "agg": "count", "title": "Purchasing Group Analysis"}
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": "Re-Release Triggered Due to Change",
            "cards": [
                {"id": "k1", "label": "Re-Released POs", "agg": "unique", "source": "po"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Vendors Impacted", "agg": "unique", "source": "vendor"},
                {"id": "k4", "label": "Total PO Amount", "agg": "sum", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Re-Release Count", "agg": "row_count"},
                {"id": "k6", "label": "Average Change Value", "agg": "avg", "source": "amount", "format": "currency"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company", "all_label": "All Companies"},
                {"id": "f2", "label": "Vendor Code", "source": "vendor", "all_label": "All Vendors"},
                {"id": "f3", "label": "Re-Release Triggered", "source": "re_release_triggered", "all_label": "All Re-Release States"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise Re-Release Cases"},
                {"id": "c2", "type": "bar", "x": "vendor_name", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Vendors with Highest Re-Releases"},
                {"id": "c3", "type": "bar", "x": "field_description", "agg": "count", "title": "Changed Field Distribution"},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Monthly Re-Release Trend"},
                {"id": "c5", "type": "bar", "x": "purchasing_group", "agg": "count", "title": "Purchasing Group Analysis"}
            ]
        },
        {
            "id": "3",
            "label": "Exception 03",
            "title": "Re-Release Triggered Due to Change = 'No'",
            "cards": [
                {"id": "k1", "label": "Non Re-Released POs", "agg": "unique", "source": "po"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Vendors Impacted", "agg": "unique", "source": "vendor"},
                {"id": "k4", "label": "Total PO Amount", "agg": "sum", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "High Risk Changes", "agg": "row_count"},
                {"id": "k6", "label": "Approval Bypass Cases", "agg": "unique", "source": "document_number"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company", "all_label": "All Companies"},
                {"id": "f2", "label": "Vendor Code", "source": "vendor", "all_label": "All Vendors"},
                {"id": "f3", "label": "Purchasing Group", "source": "purchasing_group", "all_label": "All Purchasing Groups"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise Approval Bypass Cases"},
                {"id": "c2", "type": "bar", "x": "vendor_name", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Vendor-wise Approval Bypass"},
                {"id": "c3", "type": "bar", "x": "field_description", "agg": "count", "title": "Changed Field Analysis"},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Monthly Approval Bypass Trend"},
                {"id": "c5", "type": "bar", "x": "user", "agg": "count", "title": "User-wise Changes"}
            ]
        },
        {
            "id": "4",
            "label": "Exception 04",
            "title": "Re-Release Triggered Due to Change = 'Not Required'",
            "cards": [
                {"id": "k1", "label": "Not Required Cases", "agg": "row_count"},
                {"id": "k2", "label": "Companies Impacted", "agg": "unique", "source": "company"},
                {"id": "k3", "label": "Vendors Impacted", "agg": "unique", "source": "vendor"},
                {"id": "k4", "label": "Total PO Amount", "agg": "sum", "source": "amount", "format": "currency"},
                {"id": "k5", "label": "Changed POs", "agg": "unique", "source": "po"},
                {"id": "k6", "label": "Fields Changed", "agg": "unique", "source": "field_description"}
            ],
            "filters": [
                {"id": "f1", "label": "Company Code", "source": "company", "all_label": "All Companies"},
                {"id": "f2", "label": "Vendor Code", "source": "vendor", "all_label": "All Vendors"},
                {"id": "f3", "label": "Purchasing Group", "source": "purchasing_group", "all_label": "All Purchasing Groups"}
            ],
            "charts": [
                {"id": "c1", "type": "bar", "x": "company", "agg": "count", "title": "Company-wise Not Required Cases"},
                {"id": "c2", "type": "bar", "x": "vendor_name", "y": "amount", "agg": "sum", "top_n": 10, "horizontal": True, "title": "Vendor-wise Not Required Cases"},
                {"id": "c3", "type": "bar", "x": "field_description", "agg": "count", "title": "Field Change Distribution"},
                {"id": "c4", "type": "line", "x": "date", "agg": "count", "time_group": "month", "title": "Monthly Change Trend"},
                {"id": "c5", "type": "bar", "x": "user", "agg": "count", "title": "User-wise Changes"}
            ]
        }
    ],
    "columns": {
        "company": ["Company Name", "Company Code"],
        "vendor": ["Vendor Code"],
        "vendor_name": ["Vendor Name"],
        "po": ["Object Value (Purchase Order Number)"],
        "purchasing_group": ["Purchasing Group"],
        "amount": ["Amount in Local Currency", "Net Order Price"],
        "date": ["Date of change", "PO Document date"],
        "days_after_grn": ["Change Date - GRN Date"],
        "field_description": ["Field Description"],
        "re_release_triggered": ["Re-Release Trigerred", "Re-Release Triggered Due to Change"],
        "user": ["User"],
        "document_number": ["Document Number"]
    }
}

def meta():
    return {
        "id": CONFIG["id"],
        "name": CONFIG["name"],
        "category": "Supplier Invoice"
    }

def get_data(exc_id):
    paths = [
        f"data_files/SJIN41_Exception0{exc_id}.csv",
        f"data_files/SJIN41_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
