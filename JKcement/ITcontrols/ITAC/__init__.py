# ITcontrols/ITAC/__init__.py
from .loader import create_blueprint

def register(app):
    print("[ITcontrols/ITAC] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='i_itac_ctrl',
        page_title='IT Controls ITAC Insights',
        url_prefix='/ITcontrols/itac',
        category_folder='ITAC'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[ITcontrols/ITAC] Registered at {prefix}")
