import pandas as pd
from sqlalchemy import create_engine
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def save_to_csv(df, filename="products.csv"):
    try:
        df.to_csv(filename, index=False)
        print(f"✔️ Data exported to {filename}")
    except Exception as e:
        print(f"❌ CSV export failed: {e}")

def save_to_google_sheets(df, spreadsheet_id, range_name, service_file="service-account-gsheets-api.json"):
    try:
        creds = Credentials.from_service_account_file(service_file)
        service = build("sheets", "v4", credentials=creds)
        values = [df.columns.tolist()] + df.values.tolist()
        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="RAW",
            body={"values": values}
        ).execute()
        print("✔️ Google Sheets updated successfully.")
    except Exception as e:
        print(f"❌ Failed to update Google Sheets: {e}")

def save_to_postgres(df, table_name='products', db_config=None):
    try:
        config = db_config or {
            "user": "dev_etl",
            "password": "etldeveloper",
            "host": "localhost",
            "port": "5432",
            "database": "submission_etl"
        }
        url = f"postgresql+psycopg2://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
        engine = create_engine(url)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"✔️ Data saved to PostgreSQL table: {table_name}")
    except Exception as e:
        print(f"❌ PostgreSQL error: {e}")
