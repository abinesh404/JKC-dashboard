# Supplier/s_itac.py
# -------------------------------------------------------------
# Dynamic loader routing to ITAC sub-package configurations
# -------------------------------------------------------------

from .ITAC.loader import create_blueprint

s_itac_bp, _ = create_blueprint(
    bp_name='s_itac',
    page_title='ITAC Configuration Insights',
    url_prefix='/Supplier/itac',
    category_folder='ITAC'
)