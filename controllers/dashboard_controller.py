from flask import render_template
from models.sales_model import SalesModel
import config

def index():
    """
    Halaman utama dashboard (overview / KPI cards + charts)
    """
    sales_model = SalesModel()
    
    data = {
        'title': 'Dashboard Overview',
        'app_name': config.APP_NAME,
        'total_revenue': sales_model.get_total_revenue(),
        'total_transactions': sales_model.get_total_transactions(),
        'total_units': sales_model.get_total_units_sold(),
        'avg_transaction': sales_model.get_avg_transaction_value(),
        'top_products': sales_model.get_top_products(5),
    }
    
    return render_template('dashboard/index.html', **data)
