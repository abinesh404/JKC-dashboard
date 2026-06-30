# Manufacturing/Inventory_Movement/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Manufacturing/Inventory_Movement] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='m_inv_move',
        page_title='Manufacturing Inventory Movement Insights',
        url_prefix='/Manufacturing/inventory_movement',
        category_folder='Inventory_Movement'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Manufacturing/Inventory_Movement] Registered at {prefix}")
