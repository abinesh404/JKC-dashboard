# Finance/ITAC/template.py
# -------------------------------------------------------------
# TEMPLATE ENGINE for ITAC — Same generic engine as Accounting
# -------------------------------------------------------------
# Imports the shared engine from Accounting.
# If ITAC needs custom styling later, override get_html() here.

import Finance.Accounting.template

def get_html():
    return Finance.Accounting.template.get_html()

def get_chart_title(x, y=None, type='bar', top_n=None):
    return Finance.Accounting.template.get_chart_title(x, y, type, top_n)

def get_exception_title(label):
    return Finance.Accounting.template.get_exception_title(label)
