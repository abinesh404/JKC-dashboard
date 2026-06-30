# Supplier/payment/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Supplier/payment] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='s_payment',
        page_title='Payment Insights',
        url_prefix='/Supplier/payment',
        category_folder='payment'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Supplier/payment] Registered at {prefix}")
