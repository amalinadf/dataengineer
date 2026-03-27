from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# URL Berita Mudik
URL_TARGET = "https://www.cnnindonesia.com/ekonomi/20260326132653-92-1341478/volume-kendaraan-tol-kartasura-prambanan-naik-99-hingga-h-3-lebaran"

def scrape_cnn_mudik():
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(URL_TARGET, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Ambil Judul
        judul_tag = soup.find('h1')
        judul = judul_tag.get_text(strip=True) if judul_tag else "Judul Tidak Ditemukan"
        print(f"HASIL SCRAPE: {judul}")
        return {"judul": judul}
    else:
        raise Exception(f"Gagal akses web, Status Code: {response.status_code}")

def save_to_log(**context):
    # 1. Ambil data dari task sebelumnya
    data_berita = context['ti'].xcom_pull(task_ids='scraping_berita_mudik')
    
    # 2. Setup Kredensial
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    # Path ini harus sama dengan yang di COPY di Dockerfile tadi
    creds = ServiceAccountCredentials.from_json_keyfile_name('/usr/local/airflow/kunci_google.json', scope)
    client = gspread.authorize(creds)
    
    # 3. Buka Spreadsheet
    sheet = client.open_by_key("1I5VzSKkB5qqbQKwuOWLdJ0FhbR7GDrr_r0U_9SDmlQs").sheet1
    
    # 4. Append Data (Waktu & Judul)
    waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([waktu_sekarang, data_berita['judul']])
    print(f"Gokil Mal! Berita '{data_berita['judul']}' udah masuk ke Sheets!")

with DAG(
    dag_id='monitoring_mudik_2026',
    start_date=datetime(2026, 3, 27),
    schedule=None,
    catchup=False
) as dag:

    task_scrape = PythonOperator(
        task_id='scraping_berita_mudik',
        python_callable=scrape_cnn_mudik
    )

    task_save = PythonOperator(
        task_id='simpan_log_berita',
        python_callable=save_to_log
    )

    task_scrape >> task_save
