# Finance/Spend_Analysis/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Finance/Spend_Analysis] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='f_spend',
        page_title='Finance Spend Analysis Insights',
        url_prefix='/Finance/spend_analysis',
        category_folder='Spend_Analysis'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Finance/Spend_Analysis] Registered at {prefix}")
