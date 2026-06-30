# Supplier/master_data/SJMA14.py
import pandas as pd
import os

CONFIG = {
    "id": "SJMA14",
    "name": "Vendor Details Matching with Employees",
    "active_exceptions": [
        {
            "id": "1",
            "label": "Exception 01",
            "title": "Vendor with Same Name as Employee",
            "cards": [
                {
                    "id": "k1",
                    "label": "Matching Vendors",
                    "agg": "unique",
                    "source": "vendor"
                },
                {
                    "id": "k2",
                    "label": "Matching Employees",
                    "agg": "unique",
                    "source": "employee"
                },
                {
                    "id": "k3",
                    "label": "Vendor Account Groups",
                    "agg": "unique",
                    "source": "vendor_acct_grp"
                },
                {
                    "id": "k4",
                    "label": "Countries Impacted",
                    "agg": "unique",
                    "source": "vendor_country"
                },
                {
                    "id": "k5",
                    "label": "Newly Created Vendors",
                    "agg": "unique",
                    "source": "vendor"
                },
                {
                    "id": "k6",
                    "label": "Total Exceptions",
                    "agg": "total_rows"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Vendor Account Group", "source": "vendor_acct_grp"},
                {"id": "f2", "label": "Vendor Country", "source": "vendor_country"},
                {"id": "f3", "label": "Employee Country", "source": "employee_country"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "vendor_acct_grp",
                    "agg": "count",
                    "title": "Vendor Account Group Distribution"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "vendor_created_by",
                    "agg": "count",
                    "horizontal": True,
                    "title": "Top Vendor Creators"
                },
                {
                    "id": "c3",
                    "type": "doughnut",
                    "x": "vendor_country",
                    "agg": "count",
                    "title": "Country-wise Name Matches"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "vendor_created_on",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Vendor Creation Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "vendor_city",
                    "agg": "count",
                    "title": "City-wise Name Matches"
                }
            ]
        },
        {
            "id": "2",
            "label": "Exception 02",
            "title": "Vendor with Same Address as Employee",
            "cards": [
                {
                    "id": "k1",
                    "label": "Address Matches",
                    "agg": "total_rows"
                },
                {
                    "id": "k2",
                    "label": "Matching Vendors",
                    "agg": "unique",
                    "source": "vendor"
                },
                {
                    "id": "k3",
                    "label": "Matching Employees",
                    "agg": "unique",
                    "source": "employee"
                },
                {
                    "id": "k4",
                    "label": "Cities Impacted",
                    "agg": "unique",
                    "source": "vendor_city"
                },
                {
                    "id": "k5",
                    "label": "Vendor Account Groups",
                    "agg": "unique",
                    "source": "vendor_acct_grp"
                },
                {
                    "id": "k6",
                    "label": "Total Exceptions",
                    "agg": "total_rows"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Vendor Country", "source": "vendor_country"},
                {"id": "f2", "label": "Employee Country", "source": "employee_country"},
                {"id": "f3", "label": "Vendor Account Group", "source": "vendor_acct_grp"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "vendor_city",
                    "agg": "count",
                    "title": "Count of Address Matches by Vendor City"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "vendor_created_by",
                    "agg": "count",
                    "horizontal": True,
                    "title": "Top Vendor Creators"
                },
                {
                    "id": "c3",
                    "type": "doughnut",
                    "x": "vendor_acct_grp",
                    "agg": "count",
                    "title": "Vendor Account Group Distribution"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "vendor_created_on",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Vendor Creation Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "vendor_country",
                    "agg": "count",
                    "title": "Country-wise Address Matches"
                }
            ]
        },
        {
            "id": "3",
            "label": "Exception 03",
            "title": "Vendor with Same PAN as Employee",
            "cards": [
                {
                    "id": "k1",
                    "label": "PAN Matches",
                    "agg": "total_rows"
                },
                {
                    "id": "k2",
                    "label": "Matching Vendors",
                    "agg": "unique",
                    "source": "vendor"
                },
                {
                    "id": "k3",
                    "label": "Matching Employees",
                    "agg": "unique",
                    "source": "employee"
                },
                {
                    "id": "k4",
                    "label": "Vendor Account Groups",
                    "agg": "unique",
                    "source": "vendor_acct_grp"
                },
                {
                    "id": "k5",
                    "label": "Countries Impacted",
                    "agg": "unique",
                    "source": "vendor_country"
                },
                {
                    "id": "k6",
                    "label": "Total Exceptions",
                    "agg": "total_rows"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Vendor Country", "source": "vendor_country"},
                {"id": "f2", "label": "Employee Country", "source": "employee_country"},
                {"id": "f3", "label": "Vendor Account Group", "source": "vendor_acct_grp"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "vendor_acct_grp",
                    "agg": "count",
                    "title": "Count of PAN Matches by Vendor Account Group"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "vendor_created_by",
                    "agg": "count",
                    "horizontal": True,
                    "title": "Top Vendor Creators"
                },
                {
                    "id": "c3",
                    "type": "doughnut",
                    "x": "vendor_country",
                    "agg": "count",
                    "title": "Country-wise PAN Matches"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "vendor_created_on",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Vendor Creation Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "vendor_city",
                    "agg": "count",
                    "title": "City-wise PAN Matches"
                }
            ]
        },
        {
            "id": "4",
            "label": "Exception 04",
            "title": "Vendor with Same Bank as Employee",
            "cards": [
                {
                    "id": "k1",
                    "label": "Bank Matches",
                    "agg": "total_rows"
                },
                {
                    "id": "k2",
                    "label": "Matching Vendors",
                    "agg": "unique",
                    "source": "vendor"
                },
                {
                    "id": "k3",
                    "label": "Matching Employees",
                    "agg": "unique",
                    "source": "employee"
                },
                {
                    "id": "k4",
                    "label": "Shared Bank Accounts",
                    "agg": "unique",
                    "source": "bank"
                },
                {
                    "id": "k5",
                    "label": "Vendor Account Groups",
                    "agg": "unique",
                    "source": "vendor_acct_grp"
                },
                {
                    "id": "k6",
                    "label": "Total Exceptions",
                    "agg": "total_rows"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Vendor Bank Country", "source": "vendor_bank_country"},
                {"id": "f2", "label": "Employee Bank Country", "source": "employee_bank_country"},
                {"id": "f3", "label": "Vendor Account Group", "source": "vendor_acct_grp"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "vendor_bank_country",
                    "agg": "count",
                    "title": "Count of Bank Matches by Vendor Bank Country"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "vendor_created_by",
                    "agg": "count",
                    "horizontal": True,
                    "title": "Top Vendor Creators"
                },
                {
                    "id": "c3",
                    "type": "doughnut",
                    "x": "vendor_acct_grp",
                    "agg": "count",
                    "title": "Vendor Account Group Distribution"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "vendor_created_on",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Vendor Creation Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "vendor_bank_key",
                    "agg": "count",
                    "title": "Bank Key-wise Name Matches"
                }
            ]
        },
        {
            "id": "5",
            "label": "Exception 05",
            "title": "Vendor with Same GST as Employee",
            "cards": [
                {
                    "id": "k1",
                    "label": "GST Matches",
                    "agg": "total_rows"
                },
                {
                    "id": "k2",
                    "label": "Matching Vendors",
                    "agg": "unique",
                    "source": "vendor"
                },
                {
                    "id": "k3",
                    "label": "Matching Employees",
                    "agg": "unique",
                    "source": "employee"
                },
                {
                    "id": "k4",
                    "label": "Vendor Account Groups",
                    "agg": "unique",
                    "source": "vendor_acct_grp"
                },
                {
                    "id": "k5",
                    "label": "Countries Impacted",
                    "agg": "unique",
                    "source": "vendor_country"
                },
                {
                    "id": "k6",
                    "label": "Total Exceptions",
                    "agg": "total_rows"
                }
            ],
            "filters": [
                {"id": "f1", "label": "Vendor Country", "source": "vendor_country"},
                {"id": "f2", "label": "Employee Country", "source": "employee_country"},
                {"id": "f3", "label": "Vendor Account Group", "source": "vendor_acct_grp"}
            ],
            "charts": [
                {
                    "id": "c1",
                    "type": "bar",
                    "x": "vendor_acct_grp",
                    "agg": "count",
                    "title": "Count of GST Matches by Vendor Account Group"
                },
                {
                    "id": "c2",
                    "type": "bar",
                    "x": "vendor_created_by",
                    "agg": "count",
                    "horizontal": True,
                    "title": "Top Vendor Creators"
                },
                {
                    "id": "c3",
                    "type": "doughnut",
                    "x": "vendor_country",
                    "agg": "count",
                    "title": "Country-wise GST Matches"
                },
                {
                    "id": "c4",
                    "type": "line",
                    "x": "vendor_created_on",
                    "agg": "count",
                    "time_group": "month",
                    "title": "Monthly Vendor Creation Trend"
                },
                {
                    "id": "c5",
                    "type": "bar",
                    "x": "vendor_country",
                    "agg": "count",
                    "title": "Country-wise GST Matches"
                }
            ]
        }
    ],
    "columns": {
        "vendor": [
            "Vendor code",
            "Vendor_Name",
            "Vendor Name 1",
            "Vendor Name 2"
        ],
        "employee": [
            "Employee code",
            "Employee_Name",
            "Employee Name 1",
            "Employee Name 2"
        ],
        "vendor_country": [
            "Vendor Country"
        ],
        "employee_country": [
            "Employee Country"
        ],
        "vendor_city": [
            "Vendor City"
        ],
        "location": [
            "Vendor Country",
            "Vendor City",
            "Vendor District",
            "Employee Country",
            "Employee City",
            "Employee District"
        ],
        "address": [
            "Vendor_address",
            "Employee_address",
            "Vendor Street",
            "Employee Street"
        ],
        "pan": [
            "Vendor_PAN",
            "Employee_PAN"
        ],
        "bank": [
            "Vendor Bank Account",
            "Employee Bank Account"
        ],
        "vendor_bank_country": [
            "Vendor Bank Country"
        ],
        "employee_bank_country": [
            "Employee Bank Country"
        ],
        "vendor_bank_key": [
            "Vendor  Bank Key",
            "Vendor Bank Key"
        ],
        "gst": [
            "GST_Vendor",
            "GST_Employee"
        ],
        "vendor_created_by": [
            "Vendor Created by"
        ],
        "user": [
            "Vendor Created by",
            "Employee Created by"
        ],
        "vendor_acct_grp": [
            "Vendor Account group"
        ],
        "account_group": [
            "Vendor Account group",
            "Employee Account group"
        ],
        "vendor_created_on": [
            "Vendor Created on"
        ],
        "date": [
            "Vendor Created on",
            "Employee Created on"
        ],
        "remark": [
            "Remark"
        ]
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
        f"data_files/SJMA14_Exception0{exc_id}.csv",
        f"data_files/SJMA14_Exception{exc_id}.csv"
    ]
    path = next((p for p in paths if os.path.exists(p)), None)
    if not path:
        return None
    return pd.read_csv(path, encoding='latin1', low_memory=False).fillna('')
