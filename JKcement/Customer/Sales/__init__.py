# Customer/Sales/__init__.py

from .loader import create_blueprint


def register(app):

    print("[Customer/Sales] Discovering insights...")

    bp, prefix = create_blueprint(
        bp_name='customer_sales',
        page_title='Customer Sales Insights',
        url_prefix='/Customer/sales',
        category_folder='Sales'
    )

    app.register_blueprint(bp, url_prefix=prefix)

    print(f"[Customer/Sales] Registered at {prefix}")
