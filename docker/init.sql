-- ============================================================
-- BI Dashboard - Sample Database
-- Simulasi data penjualan e-commerce untuk demo visualisasi
-- ============================================================

USE bi_dashboard;

-- Tabel kategori produk
CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Tabel produk
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    category_id INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Tabel penjualan
CREATE TABLE IF NOT EXISTS sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    total_price DECIMAL(12,2) NOT NULL,
    sale_date DATE NOT NULL,
    region VARCHAR(50) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- ============================================================
-- Seed Data
-- ============================================================

INSERT INTO categories (name) VALUES
    ('Electronics'),
    ('Clothing'),
    ('Food & Beverage'),
    ('Books'),
    ('Sports');

INSERT INTO products (name, category_id, price) VALUES
    ('Laptop Pro 15"',       1, 12500000),
    ('Wireless Headphones',  1,  850000),
    ('Smartphone X12',       1,  7200000),
    ('Men T-Shirt',          2,   150000),
    ('Running Shoes',        2,   450000),
    ('Winter Jacket',        2,   890000),
    ('Organic Coffee 500g',  3,    85000),
    ('Green Tea Pack',       3,    45000),
    ('Programming PHP Book', 4,   120000),
    ('Data Science Book',    4,   135000),
    ('Yoga Mat',             5,   250000),
    ('Dumbbells 5kg',        5,   320000);

-- Generate penjualan 12 bulan terakhir (2025)
INSERT INTO sales (product_id, quantity, total_price, sale_date, region) VALUES
-- Januari
(1, 3, 37500000, '2025-01-05', 'Jakarta'),
(2, 10, 8500000, '2025-01-07', 'Surabaya'),
(3, 5, 36000000, '2025-01-10', 'Bandung'),
(4, 30, 4500000, '2025-01-12', 'Jakarta'),
(5, 15, 6750000, '2025-01-15', 'Medan'),
(7, 50, 4250000, '2025-01-18', 'Surabaya'),
(9, 20, 2400000, '2025-01-20', 'Jakarta'),
(11, 8, 2000000, '2025-01-25', 'Bandung'),

-- Februari
(1, 4, 50000000, '2025-02-03', 'Jakarta'),
(2, 12, 10200000, '2025-02-06', 'Bandung'),
(3, 6, 43200000, '2025-02-09', 'Surabaya'),
(4, 25, 3750000, '2025-02-11', 'Medan'),
(6, 10, 8900000, '2025-02-14', 'Jakarta'),
(8, 40, 1800000, '2025-02-17', 'Surabaya'),
(10, 15, 2025000, '2025-02-20', 'Bandung'),
(12, 6, 1920000, '2025-02-23', 'Jakarta'),

-- Maret
(1, 5, 62500000, '2025-03-02', 'Surabaya'),
(2, 8, 6800000, '2025-03-05', 'Jakarta'),
(3, 7, 50400000, '2025-03-08', 'Bandung'),
(5, 20, 9000000, '2025-03-11', 'Jakarta'),
(7, 60, 5100000, '2025-03-14', 'Medan'),
(9, 25, 3000000, '2025-03-17', 'Surabaya'),
(11, 12, 3000000, '2025-03-20', 'Jakarta'),
(4, 35, 5250000, '2025-03-25', 'Bandung'),

-- April
(1, 2, 25000000, '2025-04-02', 'Medan'),
(3, 8, 57600000, '2025-04-05', 'Jakarta'),
(2, 15, 12750000, '2025-04-08', 'Surabaya'),
(6, 12, 10680000, '2025-04-11', 'Bandung'),
(8, 55, 2475000, '2025-04-14', 'Jakarta'),
(10, 18, 2430000, '2025-04-17', 'Medan'),
(12, 9, 2880000, '2025-04-20', 'Surabaya'),
(5, 18, 8100000, '2025-04-24', 'Jakarta'),

-- Mei
(1, 6, 75000000, '2025-05-01', 'Jakarta'),
(3, 9, 64800000, '2025-05-04', 'Bandung'),
(2, 20, 17000000, '2025-05-07', 'Surabaya'),
(4, 40, 6000000, '2025-05-10', 'Jakarta'),
(7, 70, 5950000, '2025-05-13', 'Medan'),
(9, 30, 3600000, '2025-05-16', 'Bandung'),
(11, 15, 3750000, '2025-05-19', 'Surabaya'),
(6, 8, 7120000, '2025-05-22', 'Jakarta'),

-- Juni
(1, 4, 50000000, '2025-06-03', 'Surabaya'),
(3, 10, 72000000, '2025-06-06', 'Jakarta'),
(2, 18, 15300000, '2025-06-09', 'Bandung'),
(5, 22, 9900000, '2025-06-12', 'Medan'),
(8, 45, 2025000, '2025-06-15', 'Jakarta'),
(10, 20, 2700000, '2025-06-18', 'Surabaya'),
(12, 11, 3520000, '2025-06-21', 'Bandung'),
(4, 28, 4200000, '2025-06-25', 'Jakarta'),

-- Juli
(1, 7, 87500000, '2025-07-02', 'Jakarta'),
(3, 11, 79200000, '2025-07-05', 'Surabaya'),
(2, 22, 18700000, '2025-07-08', 'Bandung'),
(6, 14, 12460000, '2025-07-11', 'Jakarta'),
(7, 80, 6800000, '2025-07-14', 'Medan'),
(9, 35, 4200000, '2025-07-17', 'Surabaya'),
(11, 18, 4500000, '2025-07-20', 'Jakarta'),
(5, 25, 11250000, '2025-07-24', 'Bandung'),

-- Agustus
(1, 5, 62500000, '2025-08-01', 'Bandung'),
(3, 12, 86400000, '2025-08-04', 'Jakarta'),
(2, 16, 13600000, '2025-08-07', 'Surabaya'),
(4, 45, 6750000, '2025-08-10', 'Medan'),
(8, 60, 2700000, '2025-08-13', 'Jakarta'),
(10, 22, 2970000, '2025-08-16', 'Bandung'),
(12, 13, 4160000, '2025-08-19', 'Surabaya'),
(6, 16, 14240000, '2025-08-23', 'Jakarta'),

-- September
(1, 8, 100000000, '2025-09-02', 'Jakarta'),
(3, 13, 93600000, '2025-09-05', 'Bandung'),
(2, 25, 21250000, '2025-09-08', 'Surabaya'),
(5, 28, 12600000, '2025-09-11', 'Jakarta'),
(7, 90, 7650000, '2025-09-14', 'Medan'),
(9, 40, 4800000, '2025-09-17', 'Bandung'),
(11, 20, 5000000, '2025-09-20', 'Surabaya'),
(4, 50, 7500000, '2025-09-25', 'Jakarta'),

-- Oktober
(1, 6, 75000000, '2025-10-01', 'Surabaya'),
(3, 14, 100800000, '2025-10-04', 'Jakarta'),
(2, 28, 23800000, '2025-10-07', 'Bandung'),
(6, 18, 16020000, '2025-10-10', 'Jakarta'),
(8, 70, 3150000, '2025-10-13', 'Medan'),
(10, 25, 3375000, '2025-10-16', 'Surabaya'),
(12, 15, 4800000, '2025-10-19', 'Bandung'),
(5, 30, 13500000, '2025-10-23', 'Jakarta'),

-- November
(1, 10, 125000000, '2025-11-02', 'Jakarta'),
(3, 15, 108000000, '2025-11-05', 'Surabaya'),
(2, 30, 25500000, '2025-11-08', 'Bandung'),
(4, 55, 8250000, '2025-11-11', 'Medan'),
(7, 100, 8500000, '2025-11-14', 'Jakarta'),
(9, 45, 5400000, '2025-11-17', 'Bandung'),
(11, 25, 6250000, '2025-11-20', 'Surabaya'),
(6, 20, 17800000, '2025-11-25', 'Jakarta'),

-- Desember
(1, 12, 150000000, '2025-12-01', 'Jakarta'),
(3, 16, 115200000, '2025-12-04', 'Bandung'),
(2, 35, 29750000, '2025-12-07', 'Surabaya'),
(5, 35, 15750000, '2025-12-10', 'Jakarta'),
(8, 80, 3600000, '2025-12-13', 'Medan'),
(10, 30, 4050000, '2025-12-16', 'Bandung'),
(12, 18, 5760000, '2025-12-19', 'Surabaya'),
(4, 60, 9000000, '2025-12-24', 'Jakarta');
