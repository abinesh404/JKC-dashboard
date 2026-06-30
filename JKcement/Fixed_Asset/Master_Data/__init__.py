# Fixed_Asset/Master_Data/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Fixed_Asset/Master_Data] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='fa_master',
        page_title='Fixed Asset Master Data Insights',
        url_prefix='/Fixed_Asset/master_data',
        category_folder='Master_Data'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Fixed_Asset/Master_Data] Registered at {prefix}")
