# Taxation/Master_Data/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Taxation/Master_Data] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='t_master',
        page_title='Taxation Master Data Insights',
        url_prefix='/Taxation/master_data',
        category_folder='Master_Data'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Taxation/Master_Data] Registered at {prefix}")
