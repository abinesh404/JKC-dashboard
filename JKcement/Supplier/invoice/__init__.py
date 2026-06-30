# Supplier/invoice/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Supplier/invoice] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='s_invoice',
        page_title='Invoice Insights',
        url_prefix='/Supplier/invoice',
        category_folder='invoice'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Supplier/invoice] Registered at {prefix}")
