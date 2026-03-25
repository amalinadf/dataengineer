# Simple ETL Pipeline: Retail Data Transformation 🚀

Project ini mendemonstrasikan implementasi dasar arsitektur **ETL (Extract, Transform, Load)** menggunakan Python dan SQL. Fokus utama project ini adalah menangani tantangan umum dalam integrasi data, yaitu **data cleaning** dan **standardization**.

## 📌 Overview
Dalam skenario ini, saya membangun pipeline otomatis yang mengambil data transaksi mentah yang tidak terstruktur, membersihkannya dari anomali format, dan menyimpannya ke dalam database relasional yang siap digunakan untuk analisis (Analytic-ready data).

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas (Data Manipulation), SQLAlchemy/SQLite3 (Database Engine)
- **Database:** SQLite (Local Data Warehouse)
- **Tools:** Jupyter Notebook & DBeaver

## ⚙️ ETL Workflow

### 1. Extract
Mengambil data mentah (raw) yang memiliki format tidak konsisten pada kolom harga dan tanggal.

### 2. Transform (The Core Logic)
Proses pembersihan data meliputi:
- **String Cleaning:** Menghapus karakter non-numerik (seperti "Rp", titik, dan kata "Gratis") pada kolom harga dan mengonversinya menjadi tipe data *Integer*.
- **Date Standardization:** Menggunakan fungsi `to_datetime` dengan parameter `format='mixed'` untuk menangani berbagai variasi format penulisan tanggal dalam satu kolom.
- **Handling Missing Values:** Melakukan filtering pada baris yang tidak memiliki informasi produk yang valid.

### 3. Load
Data yang telah divalidasi dan dibersihkan kemudian di-load ke dalam tabel `clean_transactions` di database **SQLite**. Proses ini menggunakan mode `if_exists='replace'` untuk memastikan ketersediaan data terbaru.

## 📊 How to Run
1. Clone repository ini:
   ```bash
   git clone [https://github.com/amalinadf/dataengineer.git](https://github.com/amalinadf/dataengineer.git)

2. Pastikan dependencies sudah terinstall:
   ```bash
    pip install pandas sqlalchemy
4. Jalankan notebook melalui Jupyter:
   ```bash
   jupyter notebook
5. Jalankan notebook melalui Jupyter:
   ```bash
   jupyter notebook

   
   
  
