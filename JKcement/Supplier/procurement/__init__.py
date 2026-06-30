# Supplier/procurement/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Supplier/procurement] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='supplier_procurement',
        page_title='Procurement Insights',
        url_prefix='/Supplier/procurement',
        category_folder='procurement'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Supplier/procurement] Registered at {prefix}")
