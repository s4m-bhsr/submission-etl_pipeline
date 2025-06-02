
# 🧵 Fashion Product ETL Pipeline

**ETL Pipeline Sederhana** untuk mengekstrak data produk fashion dari situs kompetitor [Fashion Studio Dicoding](https://fashion-studio.dicoding.dev), melakukan transformasi data, dan memuatnya ke dalam berbagai format seperti **CSV**, **Google Sheets**, dan **PostgreSQL**.

---

## 🚀 Features

- 🧽 **Extract**: Web scraping produk dari beberapa halaman katalog.
- 🛠️ **Transform**: Data cleaning, konversi harga USD ke IDR, normalisasi gender/size, dan penambahan timestamp.
- 📦 **Load**: 
  - Simpan ke file `.csv`
  - Upload ke **Google Sheets** (via Google Sheets API)
  - Insert ke **PostgreSQL** (via SQLAlchemy)

---

## 📁 Project Structure

```
SubmissionFundamentalPemrosesanData/
├── utils/
│   ├── extract.py         # Logika web scraping
│   ├── transform.py       # Data cleaning & transformasi
│   └── load.py            # Penyimpanan ke CSV, Google Sheets, dan PostgreSQL
├── tests/
│   ├── test_extract.py    # Unit test untuk modul extract
│   ├── test_transform.py  # Unit test untuk modul transform
│   └── test_load.py       # Unit test untuk modul load
└── README.md
└── main.py
└── requirements.txt
└── submission.txt
└── service-acc-key.json
└── products.csv
```

---

## ⚙️ Requirements

Install dependensi dengan:

```bash
pip install -r requirements.txt
```

**Library utama:**

* `requests`, `beautifulsoup4` – untuk scraping  
* `pandas`, `numpy` – untuk transformasi data  
* `sqlalchemy`, `psycopg2` – untuk koneksi PostgreSQL  
* `google-api-python-client`, `google-auth` – untuk akses Google Sheets  
* `unittest` , `pytest` , `pytest-cov`– untuk testing  

---

## 🧪 Running Unit Tests

### 🔹 Menggunakan `unittest`:

```bash
python -m unittest discover tests
```

### 🔹 Dengan Coverage:

```bash
coverage run -m unittest discover tests
coverage report
coverage html
start htmlcov/index.html  # buka report di browser (Windows)
```

---

## 📌 Contoh Penggunaan

### Ekstrak Data:

```python
from utils.extract import collect_all_products

data = collect_all_products(max_pages=5)
```

### Transformasi:

```python
from utils.transform import transform_data

clean_df = transform_data(data)
```

### Load ke CSV:

```python
from utils.load import save_to_csv

save_to_csv(clean_df, filename="products.csv")
```

### Load ke Google Sheets:

```python
from utils.load import save_to_google_sheets

save_to_google_sheets(clean_df, "your_spreadsheet_id", "Sheet1!A2")
```

---

## 📈 Test Coverage Status

| File         | Coverage Status                  |
| ------------ | -------------------------------- |
| test_extract.py   | ✅ 97%              |
| test_transform.py | ✅ 96%      |
| test_load.py      | ✅ 97% |

*Coverage dapat dilihat dengan `coverage html` dan dibuka via browser.*

---

## 🔐 Google Sheets Setup (Optional)

Untuk menggunakan `save_to_google_sheets`:

1. Buat service account di Google Cloud Console.
2. Aktifkan Google Sheets API.
3. Unduh file JSON Key dari service account.
4. Share spreadsheet ke email service account.
5. Letakkan file JSON di root project.

---

## 📬 License

Project ini dibuat untuk keperluan pembelajaran dan submission. Bebas dikembangkan lebih lanjut.

---

