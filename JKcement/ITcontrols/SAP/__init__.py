# ITcontrols/SAP/__init__.py
from .loader import create_blueprint

def register(app):
    print("[ITcontrols/SAP] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='i_sap',
        page_title='IT Controls SAP Insights',
        url_prefix='/ITcontrols/sap',
        category_folder='SAP'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[ITcontrols/SAP] Registered at {prefix}")
