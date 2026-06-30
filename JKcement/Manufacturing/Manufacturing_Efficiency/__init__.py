# Manufacturing/Manufacturing_Efficiency/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Manufacturing/Manufacturing_Efficiency] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='m_efficiency',
        page_title='Manufacturing Efficiency Insights',
        url_prefix='/Manufacturing/manufacturing_efficiency',
        category_folder='Manufacturing_Efficiency'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Manufacturing/Manufacturing_Efficiency] Registered at {prefix}")
