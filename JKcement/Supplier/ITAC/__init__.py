# Supplier/ITAC/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Supplier/ITAC] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='s_itac',
        page_title='ITAC Configuration Insights',
        url_prefix='/Supplier/itac',
        category_folder='ITAC'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Supplier/ITAC] Registered at {prefix}")
