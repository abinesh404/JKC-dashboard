import Customer.Invoice.template

def get_html():
    return Customer.Invoice.template.get_html()

def get_chart_title(x, y=None, type='bar', top_n=None):
    return Customer.Invoice.template.get_chart_title(x, y, type, top_n)

def get_exception_title(label):
    return Customer.Invoice.template.get_exception_title(label)