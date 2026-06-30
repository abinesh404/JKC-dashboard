# Payroll/Master_Data/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Payroll/Master_Data] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='p_master',
        page_title='Payroll Master Data Insights',
        url_prefix='/Payroll/master_data',
        category_folder='Master_Data'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Payroll/Master_Data] Registered at {prefix}")
