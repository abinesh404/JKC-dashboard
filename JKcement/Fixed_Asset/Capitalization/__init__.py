# Fixed_Asset/Capitalization/__init__.py
from .loader import create_blueprint

def register(app):
    print("[Fixed_Asset/Capitalization] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='fa_cap',
        page_title='Fixed Asset Capitalization Insights',
        url_prefix='/Fixed_Asset/capitalization',
        category_folder='Capitalization'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Fixed_Asset/Capitalization] Registered at {prefix}")
