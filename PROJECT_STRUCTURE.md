# Analisis & Struktur Project - BI Dashboard Flask

## 📊 Overview

**BI Dashboard Flask** adalah aplikasi Business Intelligence berbasis web yang dibangun dengan arsitektur MVC sederhana menggunakan Flask. Aplikasi ini menyediakan visualisasi data penjualan dengan chart interaktif dan tabel data.

### Tech Stack

- **Backend**: Flask 3.0.0 (native, tanpa SQLAlchemy, tanpa Blueprint)
- **Database**: MySQL 8.0 dengan mysql-connector-python 8.2.0
- **Frontend**: 
  - Bootstrap 5.3.3
  - Bootstrap Icons 1.11.3
  - Chart.js 4.4.3
- **Containerization**: Docker & Docker Compose
- **Environment**: python-dotenv 1.0.0

---

## 🏗️ Arsitektur

### Pattern: MVC (Model-View-Controller)

```
┌─────────────┐
│   View      │  Templates (HTML/Jinja2)
│  (Templates)│
└──────┬──────┘
       │
┌──────▼──────┐
│ Controller  │  Route handlers di app.py + controllers/
└──────┬──────┘
       │
┌──────▼──────┐
│   Model     │  Data access layer di models/
└──────┬──────┘
       │
┌──────▼──────┐
│  Database   │  MySQL (mysql-connector-python)
└─────────────┘
```

### Design Philosophy

- **Flask Native**: Tidak menggunakan Blueprint atau SQLAlchemy ORM
- **Junior Friendly**: Struktur sederhana, mudah dipahami
- **No Overengineering**: Hanya fitur yang diperlukan
- **Mock Data Support**: Dapat berjalan tanpa database untuk testing

---

## 📁 Struktur Directory

```
bi-dashboard-flask/
│
├── 📄 app.py                      # Entry point Flask + Route definitions
├── 📄 config.py                   # Configuration loader (environment variables)
├── 📄 requirements.txt            # Python dependencies
├── 📄 .env                        # Environment variables (actual config)
├── 📄 .env.example               # Template environment variables
├── 📄 README.md                   # Project documentation
├── 📄 catatan.md                  # Catatan perbaikan (Indonesian)
├── 📄 TEST_REPORT.md              # Test report documentation
│
├── 📂 controllers/                # Controller layer (business logic)
│   ├── __init__.py
│   ├── dashboard_controller.py   # Dashboard overview page
│   ├── sales_controller.py       # Sales data table page
│   └── api_controller.py         # JSON API endpoints
│
├── 📂 models/                     # Model layer (data access)
│   ├── __init__.py               # Database connection helper
│   └── sales_model.py            # Sales data queries with mock data
│
├── 📂 templates/                  # View layer (Jinja2 templates)
│   ├── 404.html                  # Error page
│   ├── layout/
│   │   └── base.html             # Base layout with sidebar
│   ├── dashboard/
│   │   └── index.html            # Dashboard overview (KPI + charts)
│   └── sales/
│       └── index.html            # Sales data table
│
├── 📂 static/                     # Static assets
│   ├── css/
│   │   └── app.css               # Custom styles (Metabase-inspired)
│   └── js/
│       └── app.js                # Chart.js initialization + sidebar toggle
│
├── 📂 docker/                     # Docker configuration
│   ├── Dockerfile                # Python 3.11 image build
│   └── init.sql                  # Database schema + seed data
│
├── 📄 docker-compose.yml          # Service orchestration (app + db)
│
└── 📂 __pycache__/               # Python bytecode (generated)
```

---

## 📝 Detail File

### Core Application Files

#### `app.py` (60 lines)
- **Purpose**: Entry point aplikasi Flask dan definisi routes
- **Key Components**:
  - Flask app initialization
  - Context processor untuk variabel global (`app_name`, `current_date`)
  - Route definitions untuk dashboard, sales, dan API
  - Error handler untuk 404
- **Routes**:
  - `GET /` - Dashboard overview
  - `GET /dashboard` - Dashboard overview (alias)
  - `GET /sales` - Sales data table
  - `GET /api/sales-monthly` - Monthly revenue JSON
  - `GET /api/sales-by-category` - Category revenue JSON
  - `GET /api/sales-by-region` - Region revenue JSON
  - `GET /api/top-products` - Top products JSON
  - `GET /api/kpi` - All KPI JSON

#### `config.py` (20 lines)
- **Purpose**: Centralized configuration dari environment variables
- **Configuration**:
  - `APP_NAME`: Nama aplikasi (default: "BI Dashboard")
  - `BASE_URL`: Base URL aplikasi
  - `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASS`: Database config
  - `TIMEZONE`: Timezone (Asia/Jakarta)

### Controllers Layer

#### `controllers/dashboard_controller.py` (22 lines)
- **Purpose**: Handle dashboard overview page
- **Function**: `index()` 
  - Mengambil KPI data (revenue, transactions, units, avg transaction)
  - Mengambil top 5 products
  - Render `dashboard/index.html`

#### `controllers/sales_controller.py` (18 lines)
- **Purpose**: Handle sales data table page
- **Function**: `index()`
  - Mengambil semua data penjualan
  - Render `sales/index.html`

#### `controllers/api_controller.py` (76 lines)
- **Purpose**: Handle JSON API endpoints untuk Chart.js
- **Functions**:
  - `sales_monthly()` - Revenue per bulan (line chart)
  - `sales_by_category()` - Revenue per kategori (doughnut chart)
  - `sales_by_region()` - Revenue per region (bar chart)
  - `top_products()` - Top 5 products (horizontal bar)
  - `kpi()` - Semua KPI dalam satu request

### Models Layer

#### `models/__init__.py` (26 lines)
- **Purpose**: Database connection helper
- **Function**: `get_db_connection()`
  - Membuat koneksi MySQL menggunakan config dari `config.py`
  - Return `None` jika koneksi gagal (untuk mock data support)
  - Menggunakan mysql-connector-python dengan autocommit

#### `models/sales_model.py` (203 lines)
- **Purpose**: Sales data queries dengan mock data fallback
- **Class**: `SalesModel`
  - `__init__()`: Inisialisasi koneksi database dan deteksi mock mode
  - **KPI Methods**:
    - `get_total_revenue()` - Total revenue keseluruhan
    - `get_total_transactions()` - Total transaksi
    - `get_total_units_sold()` - Total unit terjual
    - `get_avg_transaction_value()` - Rata-rata nilai transaksi
  - **Chart Data Methods**:
    - `get_monthly_sales(year)` - Revenue per bulan
    - `get_sales_by_category()` - Revenue per kategori
    - `get_sales_by_region()` - Revenue per region
    - `get_top_products(limit)` - Top N produk
  - **Table Data Methods**:
    - `get_all_sales()` - Data tabel penjualan lengkap
- **Mock Data**: Semua method memiliki fallback mock data jika database tidak tersedia

### Templates Layer

#### `templates/layout/base.html` (92 lines)
- **Purpose**: Base layout template dengan sidebar
- **Components**:
  - Sidebar navigation (Overview, Sales Data)
  - Top navbar dengan toggle sidebar
  - Bootstrap 5 CSS/JS CDN
  - Chart.js CDN
  - Custom CSS/JS references

#### `templates/dashboard/index.html` (176 lines)
- **Purpose**: Dashboard overview page
- **Components**:
  - 4 KPI Cards (Revenue, Transactions, Units, Avg Transaction)
  - Monthly Revenue Line Chart
  - Revenue by Category Doughnut Chart
  - Revenue by Region Bar Chart
  - Top 5 Products Horizontal Bar Chart
  - Top Products Detail Table
  - Chart initialization script

#### `templates/sales/index.html` (87 lines)
- **Purpose**: Sales data table page
- **Components**:
  - Search box untuk filter client-side
  - Responsive table dengan semua kolom penjualan
  - Badges untuk kategori dan region
  - Client-side search JavaScript

### Static Assets

#### `static/css/app.css` (269 lines)
- **Purpose**: Custom styles dengan tema Metabase-inspired
- **Features**:
  - CSS variables untuk konsistensi
  - Dark sidebar dengan active states
  - KPI card styling dengan soft background colors
  - Responsive design dengan mobile sidebar
  - Custom badge styles
  - Table styling

#### `static/js/app.js` (253 lines)
- **Purpose**: Chart.js initialization dan sidebar toggle
- **Functions**:
  - Sidebar toggle (desktop collapsed / mobile slide-in)
  - `initDashboardCharts()` - Fetch semua data API secara paralel
  - `renderMonthlyChart()` - Line chart untuk monthly revenue
  - `renderCategoryChart()` - Doughnut chart untuk category
  - `renderRegionChart()` - Bar chart untuk region
  - `renderTopProductsChart()` - Horizontal bar untuk top products
  - `formatRupiah()` - Helper untuk format currency IDR
- **Features**:
  - Async data fetching dengan Promise.all
  - Chart.js global defaults untuk styling konsisten
  - Custom tooltip dengan format Rupiah
  - Responsive charts

### Docker Configuration

#### `docker/Dockerfile` (25 lines)
- **Purpose**: Build image untuk Flask app
- **Base Image**: python:3.11-slim
- **Steps**:
  - Install system dependencies (gcc, mysql client)
  - Install Python dependencies dari requirements.txt
  - Copy application code
  - Expose port 5000
  - Run `python app.py`

#### `docker/init.sql` (180 lines)
- **Purpose**: Database schema dan seed data
- **Tables**:
  - `categories` - Kategori produk
  - `products` - Produk dengan harga
  - `sales` - Transaksi penjualan
- **Seed Data**:
  - 5 kategori (Electronics, Clothing, Food & Beverage, Books, Sports)
  - 12 produk dengan harga berbeda
  - 96 transaksi penjualan untuk 12 bulan (2025)
  - Data tersebar di 4 region (Jakarta, Surabaya, Bandung, Medan)

#### `docker-compose.yml` (37 lines)
- **Purpose**: Orchestrate app dan database services
- **Services**:
  - `app`: Flask app container
    - Build dari docker/Dockerfile
    - Port mapping 5000:5000
    - Volume mount untuk development
    - Environment variables untuk database
    - Depends on db service
  - `db`: MySQL 8.0 container
    - Image mysql:8.0
    - Port mapping 3306:3306
    - Persistent volume untuk data
    - Init script dari docker/init.sql

### Configuration Files

#### `requirements.txt` (4 lines)
```
Flask==3.0.0
mysql-connector-python==8.2.0
python-dotenv==1.0.0
```

#### `.env.example` (11 lines)
Template untuk environment variables:
- APP_NAME, BASE_URL
- DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS

---

## 🔌 API Endpoints

Semua endpoint mengembalikan JSON untuk Chart.js:

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| GET | `/api/kpi` | Semua KPI dalam satu request | `{total_revenue, total_transactions, total_units, avg_transaction}` |
| GET | `/api/sales-monthly?year=2025` | Revenue per bulan | `{labels[], revenue[], transactions[]}` |
| GET | `/api/sales-by-category` | Revenue per kategori | `{labels[], revenue[]}` |
| GET | `/api/sales-by-region` | Revenue per region | `{labels[], revenue[]}` |
| GET | `/api/top-products` | Top 5 produk | `{labels[], revenue[], units[]}` |

---

## 🗄️ Database Schema

### Tables

#### `categories`
```sql
id INT AUTO_INCREMENT PRIMARY KEY
name VARCHAR(100) NOT NULL
```

#### `products`
```sql
id INT AUTO_INCREMENT PRIMARY KEY
name VARCHAR(150) NOT NULL
category_id INT NOT NULL (FK -> categories.id)
price DECIMAL(10,2) NOT NULL
```

#### `sales`
```sql
id INT AUTO_INCREMENT PRIMARY KEY
product_id INT NOT NULL (FK -> products.id)
quantity INT NOT NULL
total_price DECIMAL(12,2) NOT NULL
sale_date DATE NOT NULL
region VARCHAR(50) NOT NULL
```

---

## 🎯 Key Features

### 1. Dashboard Overview
- **KPI Cards**: Total Revenue, Total Transactions, Units Sold, Average Transaction
- **Charts**:
  - Monthly Revenue (Line Chart)
  - Revenue by Category (Doughnut Chart)
  - Revenue by Region (Bar Chart)
  - Top 5 Products (Horizontal Bar Chart)
- **Top Products Table**: Detail top 5 produk dengan revenue dan units sold

### 2. Sales Data Table
- Tabel lengkap semua transaksi penjualan
- Client-side search untuk filter product, category, region
- Responsive design
- Badges untuk kategori dan region

### 3. Mock Data Mode
- Aplikasi dapat berjalan tanpa database
- Otomatis menggunakan mock data jika koneksi database gagal
- Berguna untuk development dan testing

### 4. Responsive Design
- Desktop: Sidebar dapat di-collapse
- Mobile: Sidebar slide-in/off-canvas
- Charts responsive dengan Chart.js

### 5. Docker Support
- One-command deployment dengan `docker-compose up`
- MySQL container dengan auto-initialization
- Volume mount untuk development

---

## 🚀 Cara Menjalankan

### Dengan Docker (Recommended)
```bash
docker-compose up --build
```
Akses di http://localhost:5000

### Tanpa Docker (Local Python)
```bash
pip install -r requirements.txt
python app.py
```
Akses di http://localhost:5000

---

## 📊 Data Flow

### Dashboard Page Load
1. User mengakses `/`
2. `app.py` route ke `dashboard_controller.index()`
3. Controller memanggil `SalesModel` untuk KPI dan top products
4. Model query database atau return mock data
5. Controller render `dashboard/index.html` dengan data
6. Browser load page dan execute JavaScript
7. `initDashboardCharts()` fetch data dari API endpoints
8. Chart.js render charts dengan data dari API

### API Request
1. Chart.js fetch data dari `/api/*`
2. `app.py` route ke `api_controller` function
3. Controller memanggil `SalesModel` method
4. Model query database atau return mock data
5. Controller format data dan return JSON
6. Chart.js update chart dengan JSON response

---

## 🔧 Configuration

### Environment Variables
Dikonfigurasi melalui file `.env`:
- `APP_NAME`: Nama aplikasi
- `BASE_URL`: Base URL
- `DB_HOST`: Database host (default: `db` untuk Docker, `localhost` untuk local)
- `DB_PORT`: Database port (default: 3306)
- `DB_NAME`: Database name (default: bi_dashboard)
- `DB_USER`: Database user (default: bi_user)
- `DB_PASS`: Database password (default: bi_password)

---

## 📈 Status Project

Berdasarkan `catatan.md`:
- ✅ Flask app berjalan dan dapat diakses
- ✅ Mock data berfungsi untuk testing tanpa database
- ✅ Semua routes dan API endpoints berfungsi
- ⚠️ Database asli belum terhubung (opsional untuk production)
- ✅ Template Jinja2 error sudah diperbaiki
- ✅ Dependencies sudah terinstall

---

## 🎨 Design Style

### UI/UX
- **Inspiration**: Metabase-inspired dashboard
- **Color Palette**: 
  - Primary: Indigo (#6366f1)
  - Success: Emerald (#10b981)
  - Warning: Amber (#f59e0b)
  - Danger: Red (#ef4444)
  - Info: Cyan (#06b6d4)
- **Typography**: Inter font family
- **Layout**: Sidebar navigation + main content area
- **Components**: Cards, badges, tables, charts

---

## 🔄 Konversi dari PHP

Project ini adalah konversi dari versi PHP ke Flask MVC dengan constraint:
- Flask native (tanpa Blueprint)
- MVC sederhana
- Tidak menggunakan SQLAlchemy (menggunakan mysql-connector-python langsung)
- Junior friendly
- Hindari overengineering

---

## 📝 Catatan Penting

### Untuk Production
1. Setup MySQL lokal atau gunakan Docker
2. Hapus mock data code jika database sudah tersedia
3. Deploy dengan Docker Compose
4. Tambah error handling yang lebih robust
5. Tambah logging untuk debugging
6. Gunakan environment variables yang aman
7. Implementasi authentication/authorization jika diperlukan

### Mock Data Mode
Aplikasi saat ini berjalan dalam **Mock Data Mode** karena:
- MySQL tidak tersedia secara lokal
- Konfigurasi `.env` masih menggunakan `DB_HOST=db` (untuk Docker)

Untuk menggunakan database asli, update `.env`:
```
DB_HOST=localhost
DB_PORT=3306
DB_NAME=bi_dashboard
DB_USER=bi_user
DB_PASS=bi_password
```

---

## 📚 Dependencies Detail

### Flask 3.0.0
- Web framework untuk Python
- Routing, templating, request handling

### mysql-connector-python 8.2.0
- MySQL driver untuk Python
- Koneksi database dan query execution

### python-dotenv 1.0.0
- Load environment variables dari .env file
- Manajemen configuration

---

## 🎯 Future Enhancements (Opsional)

1. **Authentication**: Login system dengan role-based access
2. **Data Export**: Export ke CSV/Excel
3. **Date Range Filter**: Filter data berdasarkan tanggal
4. **More Charts**: Tambah jenis visualisasi lain
5. **Real-time Updates**: WebSocket untuk real-time data
6. **Admin Panel**: CRUD untuk products dan categories
7. **API Documentation**: Swagger/OpenAPI docs
8. **Unit Tests**: Test coverage untuk controllers dan models
9. **CI/CD Pipeline**: Automated testing dan deployment
10. **Monitoring**: APM dan error tracking

---

## 📞 Contact & Support

Untuk pertanyaan atau issue, refer ke:
- `README.md` - Dokumentasi resmi
- `catatan.md` - Catatan perbaikan (Indonesian)
- `TEST_REPORT.md` - Test report

---

**Generated**: May 7, 2026  
**Project Version**: Flask MVC  
**Status**: Active Development
