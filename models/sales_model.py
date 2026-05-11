from models import get_db_connection

class SalesModel:
    """
    Semua query yang berhubungan dengan data penjualan ada di sini.
    Controller tidak boleh menulis SQL langsung — selalu lewat model.
    """
    
    def __init__(self):
        self.db = get_db_connection()
        self.use_mock_data = (self.db is None)
    
    # ── KPI Cards ─────────────────────────────────────────────
    
    def get_total_revenue(self):
        """Total revenue keseluruhan"""
        if self.use_mock_data:
            return 125000000.0  # Mock data: Rp 125 juta
        cursor = self.db.cursor()
        cursor.execute("SELECT COALESCE(SUM(total_price), 0) FROM sales")
        result = cursor.fetchone()
        cursor.close()
        return float(result[0]) if result else 0.0
    
    def get_total_transactions(self):
        """Total transaksi"""
        if self.use_mock_data:
            return 96  # Mock data
        cursor = self.db.cursor()
        cursor.execute("SELECT COUNT(*) FROM sales")
        result = cursor.fetchone()
        cursor.close()
        return int(result[0]) if result else 0
    
    def get_total_units_sold(self):
        """Total unit terjual"""
        if self.use_mock_data:
            return 342  # Mock data
        cursor = self.db.cursor()
        cursor.execute("SELECT COALESCE(SUM(quantity), 0) FROM sales")
        result = cursor.fetchone()
        cursor.close()
        return int(result[0]) if result else 0
    
    def get_avg_transaction_value(self):
        """Rata-rata nilai transaksi"""
        if self.use_mock_data:
            return 1302083.33  # Mock data
        cursor = self.db.cursor()
        cursor.execute("SELECT COALESCE(AVG(total_price), 0) FROM sales")
        result = cursor.fetchone()
        cursor.close()
        return float(result[0]) if result else 0.0
    
    # ── Chart Data ────────────────────────────────────────────
    
    def get_monthly_sales(self, year=2025):
        """
        Revenue per bulan (untuk line/bar chart)
        Return: list of dicts with keys: month, revenue, transactions
        """
        if self.use_mock_data:
            return [
                {'month': 'Jan 2025', 'revenue': 8500000, 'transactions': 8},
                {'month': 'Feb 2025', 'revenue': 9200000, 'transactions': 9},
                {'month': 'Mar 2025', 'revenue': 11000000, 'transactions': 10},
                {'month': 'Apr 2025', 'revenue': 10500000, 'transactions': 9},
                {'month': 'May 2025', 'revenue': 12000000, 'transactions': 11},
            ]
        cursor = self.db.cursor(dictionary=True)
        query = """
            SELECT
                DATE_FORMAT(sale_date, '%b %Y') AS month,
                DATE_FORMAT(sale_date, '%Y-%m') AS sort_key,
                SUM(total_price) AS revenue,
                COUNT(*) AS transactions
            FROM sales
            WHERE YEAR(sale_date) = %s
            GROUP BY sort_key, month
            ORDER BY sort_key ASC
        """
        cursor.execute(query, (year,))
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def get_sales_by_category(self):
        """
        Revenue per kategori (untuk pie/doughnut chart)
        """
        if self.use_mock_data:
            return [
                {'category': 'Electronics', 'revenue': 45000000},
                {'category': 'Clothing', 'revenue': 32000000},
                {'category': 'Food', 'revenue': 28000000},
                {'category': 'Books', 'revenue': 12000000},
                {'category': 'Other', 'revenue': 8000000},
            ]
        cursor = self.db.cursor(dictionary=True)
        query = """
            SELECT
                c.name AS category,
                SUM(s.total_price) AS revenue
            FROM sales s
            JOIN products p ON s.product_id = p.id
            JOIN categories c ON p.category_id = c.id
            GROUP BY c.id, c.name
            ORDER BY revenue DESC
        """
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def get_sales_by_region(self):
        """
        Revenue per region (untuk bar chart horizontal)
        """
        if self.use_mock_data:
            return [
                {'region': 'Jakarta', 'revenue': 45000000, 'transactions': 35},
                {'region': 'Surabaya', 'revenue': 32000000, 'transactions': 28},
                {'region': 'Bandung', 'revenue': 25000000, 'transactions': 22},
                {'region': 'Medan', 'revenue': 15000000, 'transactions': 11},
            ]
        cursor = self.db.cursor(dictionary=True)
        query = """
            SELECT
                region,
                SUM(total_price) AS revenue,
                COUNT(*) AS transactions
            FROM sales
            GROUP BY region
            ORDER BY revenue DESC
        """
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def get_top_products(self, limit=5):
        """
        Top N produk berdasarkan revenue
        """
        if self.use_mock_data:
            return [
                {'product': 'Laptop Pro', 'revenue': 35000000, 'units_sold': 25},
                {'product': 'Smartphone X', 'revenue': 28000000, 'units_sold': 40},
                {'product': 'Wireless Headphones', 'revenue': 15000000, 'units_sold': 50},
                {'product': 'Tablet Mini', 'revenue': 12000000, 'units_sold': 30},
                {'product': 'Smart Watch', 'revenue': 10000000, 'units_sold': 35},
            ]
        cursor = self.db.cursor(dictionary=True)
        query = """
            SELECT
                p.name AS product,
                SUM(s.total_price) AS revenue,
                SUM(s.quantity) AS units_sold
            FROM sales s
            JOIN products p ON s.product_id = p.id
            GROUP BY p.id, p.name
            ORDER BY revenue DESC
            LIMIT %s
        """
        cursor.execute(query, (limit,))
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def get_all_sales(self):
        """
        Data tabel penjualan lengkap (dengan join)
        """
        if self.use_mock_data:
            from datetime import datetime, timedelta
            base_date = datetime.now()
            return [
                {'id': 1, 'product': 'Laptop Pro', 'category': 'Electronics', 'quantity': 2, 'total_price': 2800000, 'sale_date': (base_date - timedelta(days=1)), 'region': 'Jakarta'},
                {'id': 2, 'product': 'Smartphone X', 'category': 'Electronics', 'quantity': 3, 'total_price': 2100000, 'sale_date': (base_date - timedelta(days=2)), 'region': 'Surabaya'},
                {'id': 3, 'product': 'Wireless Headphones', 'category': 'Electronics', 'quantity': 5, 'total_price': 1500000, 'sale_date': (base_date - timedelta(days=3)), 'region': 'Bandung'},
                {'id': 4, 'product': 'T-Shirt', 'category': 'Clothing', 'quantity': 10, 'total_price': 500000, 'sale_date': (base_date - timedelta(days=4)), 'region': 'Jakarta'},
                {'id': 5, 'product': 'Jeans', 'category': 'Clothing', 'quantity': 5, 'total_price': 750000, 'sale_date': (base_date - timedelta(days=5)), 'region': 'Medan'},
            ]
        cursor = self.db.cursor(dictionary=True)
        query = """
            SELECT
                s.id,
                p.name AS product,
                c.name AS category,
                s.quantity,
                s.total_price,
                s.sale_date,
                s.region
            FROM sales s
            JOIN products p ON s.product_id = p.id
            JOIN categories c ON p.category_id = c.id
            ORDER BY s.sale_date DESC
        """
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results
