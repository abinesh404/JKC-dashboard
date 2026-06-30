# Manufacturing/Others/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Manufacturing/Others] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='m_others',
        page_title='Manufacturing Other Insights',
        url_prefix='/Manufacturing/others',
        category_folder='Others'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Manufacturing/Others] Registered at {prefix}")
