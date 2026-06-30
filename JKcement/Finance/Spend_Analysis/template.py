# Finance/Spend_Analysis/template.py
# Imports shared engine from Accounting
import Finance.Accounting.template

def get_html():
    return Finance.Accounting.template.get_html()

def get_chart_title(x, y=None, type='bar', top_n=None):
    return Finance.Accounting.template.get_chart_title(x, y, type, top_n)

def get_exception_title(label):
    return Finance.Accounting.template.get_exception_title(label)
