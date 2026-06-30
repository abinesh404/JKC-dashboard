# Taxation/GST/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Taxation/GST] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='t_gst',
        page_title='Taxation GST Insights',
        url_prefix='/Taxation/gst',
        category_folder='GST'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Taxation/GST] Registered at {prefix}")
