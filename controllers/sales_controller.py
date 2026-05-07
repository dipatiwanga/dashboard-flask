from flask import render_template
from models.sales_model import SalesModel
import config

def index():
    """
    Halaman tabel data penjualan lengkap
    """
    sales_model = SalesModel()
    
    data = {
        'title': 'Sales Data',
        'app_name': config.APP_NAME,
        'sales': sales_model.get_all_sales(),
    }
    
    return render_template('sales/index.html', **data)
