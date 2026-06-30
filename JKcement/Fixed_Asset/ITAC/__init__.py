# Fixed_Asset/ITAC/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Fixed_Asset/ITAC] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='fa_itac',
        page_title='Fixed Asset ITAC Insights',
        url_prefix='/Fixed_Asset/itac',
        category_folder='ITAC'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Fixed_Asset/ITAC] Registered at {prefix}")
