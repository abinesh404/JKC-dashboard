# Finance/ITAC/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Finance/ITAC] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='f_itac',
        page_title='Finance ITAC Insights',
        url_prefix='/Finance/itac',
        category_folder='ITAC'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Finance/ITAC] Registered at {prefix}")
