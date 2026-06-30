# Fixed_Asset/Depreciation/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Fixed_Asset/Depreciation] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='fa_dep',
        page_title='Fixed Asset Depreciation Insights',
        url_prefix='/Fixed_Asset/depreciation',
        category_folder='Depreciation'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Fixed_Asset/Depreciation] Registered at {prefix}")
