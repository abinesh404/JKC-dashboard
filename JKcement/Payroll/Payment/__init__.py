# Payroll/Payment/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Payroll/Payment] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='p_payment',
        page_title='Payroll Payment Insights',
        url_prefix='/Payroll/payment',
        category_folder='Payment'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Payroll/Payment] Registered at {prefix}")
