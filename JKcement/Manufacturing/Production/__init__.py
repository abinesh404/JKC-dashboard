# Manufacturing/Production/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Manufacturing/Production] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='m_production',
        page_title='Manufacturing Production Insights',
        url_prefix='/Manufacturing/production',
        category_folder='Production'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Manufacturing/Production] Registered at {prefix}")
