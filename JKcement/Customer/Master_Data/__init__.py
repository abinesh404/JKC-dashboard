# Customer/MasterData/__init__.py

from .loader import create_blueprint


def register(app):

    print("[Customer/MasterData] Discovering insights...")

    bp, prefix = create_blueprint(
        bp_name='customer_masterdata',
        page_title='Customer Master Data Insights',
        url_prefix='/Customer/master_data',
        category_folder='Master_Data',
    )

    app.register_blueprint(bp, url_prefix=prefix)

    print(f"[Customer/MasterData] Registered at {prefix}")
