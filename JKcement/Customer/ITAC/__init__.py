# Customer/ITAC/__init__.py

from .loader import create_blueprint


def register(app):

    print("[Customer/ITAC] Discovering insights...")

    bp, prefix = create_blueprint(
        bp_name='customer_itac',
        page_title='Customer ITAC Insights',
        url_prefix='/Customer/itac',
        category_folder='ITAC'
    )

    app.register_blueprint(bp, url_prefix=prefix)

    print(f"[Customer/ITAC] Registered at {prefix}")

