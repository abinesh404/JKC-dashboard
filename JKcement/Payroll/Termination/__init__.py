# Payroll/Termination/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Payroll/Termination] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='p_termination',
        page_title='Payroll Termination Insights',
        url_prefix='/Payroll/termination',
        category_folder='Termination'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Payroll/Termination] Registered at {prefix}")
