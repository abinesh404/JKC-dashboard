# Payroll/SoD/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Payroll/SoD] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='p_sod',
        page_title='Payroll SoD Insights',
        url_prefix='/Payroll/sod',
        category_folder='SoD'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Payroll/SoD] Registered at {prefix}")
