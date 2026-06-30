from flask import Flask, render_template
import webbrowser
from threading import Timer
import os

# Import Supplier Blueprints
from Supplier.procurement import register as reg_s_procurement
from Supplier.payment import register as reg_s_payment
from Supplier.master_data import register as reg_s_master
from Supplier.invoice import register as reg_s_invoice
from Supplier.s_itac import s_itac_bp



# ── Customer ──




# Finance blueprints are loaded dynamically via Finance/loader.py


app = Flask(__name__)

# ── Supplier ──
reg_s_procurement(app)
reg_s_payment(app)
reg_s_master(app)
reg_s_invoice(app)
app.register_blueprint(s_itac_bp, url_prefix='/Supplier/itac')

# ── Customer ──
#app.register_blueprint(c_invoice_bp, url_prefix='/Customer/invoice')
#app.register_blueprint(c_itac_bp, url_prefix='/Customer/itac')

from Customer.Invoice import register as reg_c_invoice
from Customer.ITAC import register as reg_c_itac
from Customer.Master_Data import register as reg_c_master_data
from Customer.Sales import register as reg_c_sales


reg_c_invoice(app)
reg_c_itac(app)
reg_c_master_data(app)
reg_c_sales(app)


# ── Finance (Payment — standalone) ──


# ── Finance (Accounting, ITAC, Spend_Analysis — plugin architecture) ──
from Finance.Accounting import register as reg_accounting
from Finance.ITAC import register as reg_itac
from Finance.Spend_Analysis import register as reg_spend

reg_accounting(app)
reg_itac(app)
reg_spend(app)

# ── IT Controls ──
from ITcontrols.SAP import register as reg_it_sap
from ITcontrols.ITAC import register as reg_it_itac

reg_it_sap(app)
reg_it_itac(app)

# ── Manufacturing ──
from Manufacturing.Production import register as reg_m_prod
from Manufacturing.Inventory_Movement import register as reg_m_inv
from Manufacturing.ITAC import register as reg_m_itac
from Manufacturing.Manufacturing_Efficiency import register as reg_m_eff
from Manufacturing.Others import register as reg_m_others

reg_m_prod(app)
reg_m_inv(app)
reg_m_itac(app)
reg_m_eff(app)
reg_m_others(app)

# ── Payroll ──
from Payroll.SoD import register as reg_p_sod
from Payroll.Master_Data import register as reg_p_master
from Payroll.Payment import register as reg_p_payment
from Payroll.Termination import register as reg_p_term

reg_p_sod(app)
reg_p_master(app)
reg_p_payment(app)
reg_p_term(app)

# ── Taxation ──
from Taxation.GST import register as reg_t_gst
from Taxation.Master_Data import register as reg_t_master

reg_t_gst(app)
reg_t_master(app)

# ── Fixed Asset ──
from Fixed_Asset.Capitalization import register as reg_fa_cap
from Fixed_Asset.ITAC import register as reg_fa_itac
from Fixed_Asset.Depreciation import register as reg_fa_dep
from Fixed_Asset.Master_Data import register as reg_fa_master

reg_fa_cap(app)
reg_fa_itac(app)
reg_fa_dep(app)
reg_fa_master(app)

@app.route('/')
def home():
    return render_template('home.html')

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    if not os.path.exists('data_files'):
        print("Warning: 'data_files' folder not found.")
    
    print("Starting JK Cement Dashboard...")
    Timer(1.5, open_browser).start()
    app.run(debug=True, use_reloader=False)