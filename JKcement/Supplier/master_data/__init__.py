# Supplier/master_data/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Supplier/master_data] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='s_master',
        page_title='Master Data Insights',
        url_prefix='/Supplier/master_data',
        category_folder='master_data'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Supplier/master_data] Registered at {prefix}")
