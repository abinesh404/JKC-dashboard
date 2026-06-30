# Customer/Invoice/__init__.py


from .loader import create_blueprint

def register(app):

    print("[Customer/Invoice] Discovering insights...")

    bp, prefix = create_blueprint(
        bp_name='customer_invoice',
        page_title='Customer Invoice Insights',
        url_prefix='/Customer/invoice',
        category_folder='Invoice'
    )

    app.register_blueprint(bp, url_prefix=prefix)

    print(f"[Customer/Invoice] Registered at {prefix}")

