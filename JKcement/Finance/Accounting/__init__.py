# Finance/Accounting/__init__.py
# Wires Insight -> Loader -> Template for this category

from .loader import create_blueprint

def register(app):
    """Register the Accounting blueprint with the Flask app."""
    print("[Finance/Accounting] Discovering insights...")
    bp, prefix = create_blueprint(
        bp_name='f_accounting',
        page_title='Finance Accounting Insights',
        url_prefix='/Finance/accounting',
        category_folder='Accounting'
    )
    app.register_blueprint(bp, url_prefix=prefix)
    print(f"[Finance/Accounting] Registered at {prefix}")
