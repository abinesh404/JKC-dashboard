# Manufacturing/ITAC/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Manufacturing/ITAC] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='m_itac',
        page_title='Manufacturing ITAC Insights',
        url_prefix='/Manufacturing/itac',
        category_folder='ITAC'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Manufacturing/ITAC] Registered at {prefix}")
