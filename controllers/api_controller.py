from flask import jsonify, request
from models.sales_model import SalesModel

def sales_monthly():
    """
    GET /api/sales-monthly
    Data revenue per bulan untuk line chart
    """
    year = request.args.get('year', 2025, type=int)
    sales_model = SalesModel()
    rows = sales_model.get_monthly_sales(year)
    
    labels = [row['month'] for row in rows]
    revenue = [float(row['revenue']) for row in rows]
    transactions = [int(row['transactions']) for row in rows]
    
    return jsonify({
        'labels': labels,
        'revenue': revenue,
        'transactions': transactions
    })

def sales_by_category():
    """
    GET /api/sales-by-category
    Data revenue per kategori untuk doughnut chart
    """
    sales_model = SalesModel()
    rows = sales_model.get_sales_by_category()
    
    return jsonify({
        'labels': [row['category'] for row in rows],
        'revenue': [float(row['revenue']) for row in rows]
    })

def sales_by_region():
    """
    GET /api/sales-by-region
    Data revenue per region untuk bar chart
    """
    sales_model = SalesModel()
    rows = sales_model.get_sales_by_region()
    
    return jsonify({
        'labels': [row['region'] for row in rows],
        'revenue': [float(row['revenue']) for row in rows]
    })

def top_products():
    """
    GET /api/top-products
    Top 5 produk untuk bar chart horizontal
    """
    sales_model = SalesModel()
    rows = sales_model.get_top_products(5)
    
    return jsonify({
        'labels': [row['product'] for row in rows],
        'revenue': [float(row['revenue']) for row in rows],
        'units': [int(row['units_sold']) for row in rows]
    })

def kpi():
    """
    GET /api/kpi
    Semua KPI dalam satu request
    """
    sales_model = SalesModel()
    
    return jsonify({
        'total_revenue': sales_model.get_total_revenue(),
        'total_transactions': sales_model.get_total_transactions(),
        'total_units': sales_model.get_total_units_sold(),
        'avg_transaction': sales_model.get_avg_transaction_value()
    })
