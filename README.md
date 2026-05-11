# BI Dashboard - Flask MVC Version

Business Intelligence Dashboard dengan Flask, MySQL, dan Chart.js.

Note: minor README update to create a pull request branch.

## Tech Stack

- **Backend**: Flask 3.0 (native, tanpa SQLAlchemy, tanpa Blueprint)
- **Database**: MySQL 8.0 dengan mysql-connector-python
- **Frontend**: Bootstrap 5, Bootstrap Icons, Chart.js
- **Containerization**: Docker & Docker Compose

## Struktur Project

```
bi-dashboard-flask/
├── app.py                    # Entry point + Flask routes
├── config.py                 # Konfigurasi aplikasi
├── requirements.txt          # Python dependencies
├── .env.example             # Template environment variables
├── controllers/
│   ├── dashboard_controller.py  # Halaman dashboard
│   ├── sales_controller.py      # Halaman sales data
│   └── api_controller.py        # API endpoints JSON
├── models/
│   ├── __init__.py               # Koneksi database
│   └── sales_model.py            # Query SQL
├── templates/
│   ├── layout/
│   │   └── base.html             # Layout utama
│   ├── dashboard/
│   │   └── index.html            # View dashboard
│   ├── sales/
│   │   └── index.html            # View sales
│   └── 404.html                  # Halaman error
├── static/
│   ├── css/app.css               # Stylesheet
│   └── js/app.js                 # JavaScript
├── docker/
│   ├── Dockerfile                # Python image
│   └── init.sql                  # Database schema + seed data
└── docker-compose.yml            # Service definitions
```

## Cara Menjalankan

### Menggunakan Docker (Recommended)

1. Clone atau copy project ini:
```bash
cd bi-dashboard-flask
```

2. Jalankan dengan Docker Compose:
```bash
docker-compose up --build
```

3. Akses aplikasi di browser:
- Dashboard: http://localhost:5000
- Sales Data: http://localhost:5000/sales

4. Stop aplikasi:
```bash
docker-compose down
```

### Menggunakan Local Python (Tanpa Docker)

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Setup database MySQL secara manual (jalankan `docker/init.sql`)

3. Copy `.env.example` ke `.env` dan sesuaikan konfigurasi:
```bash
cp .env.example .env
```

4. Jalankan aplikasi:
```bash
python app.py
```

5. Akses di http://localhost:5000

## API Endpoints

Semua endpoint mengembalikan JSON untuk Chart.js:

- `GET /api/sales-monthly?year=2025` - Revenue per bulan
- `GET /api/sales-by-category` - Revenue per kategori
- `GET /api/sales-by-region` - Revenue per region
- `GET /api/top-products` - Top 5 produk
- `GET /api/kpi` - Semua KPI dalam satu request

## Konversi dari PHP

Project ini adalah konversi dari versi PHP ke Flask MVC dengan constraint:

- Flask native (tanpa Blueprint)
- MVC sederhana
- Tidak menggunakan SQLAlchemy (menggunakan mysql-connector-python langsung)
- Junior friendly
- Hindari overengineering

Lihat `../issue.md` untuk detail mapping konversi.
