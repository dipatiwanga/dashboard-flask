from flask import Flask, render_template
from datetime import datetime
import config
import controllers.dashboard_controller as dashboard_controller
import controllers.sales_controller as sales_controller
import controllers.api_controller as api_controller

app = Flask(__name__)

# Context processor untuk variabel global di semua template
@app.context_processor
def inject_globals():
    return {
        'app_name': config.APP_NAME,
        'current_date': datetime.now().strftime('%d %b %Y')
    }

# ── Dashboard Routes ────────────────────────────────────────
@app.route('/')
def index():
    return dashboard_controller.index()

@app.route('/dashboard')
def dashboard():
    return dashboard_controller.index()

# ── Sales Routes ───────────────────────────────────────────
@app.route('/sales')
def sales_index():
    return sales_controller.index()

# ── API Routes ─────────────────────────────────────────────
@app.route('/api/sales-monthly')
def api_sales_monthly():
    return api_controller.sales_monthly()

@app.route('/api/sales-by-category')
def api_sales_by_category():
    return api_controller.sales_by_category()

@app.route('/api/sales-by-region')
def api_sales_by_region():
    return api_controller.sales_by_region()

@app.route('/api/top-products')
def api_top_products():
    return api_controller.top_products()

@app.route('/api/kpi')
def api_kpi():
    return api_controller.kpi()

# ── Error Handlers ─────────────────────────────────────────
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
