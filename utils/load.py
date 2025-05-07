import pandas as pd
import logging
import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

def save_to_csv(df: pd.DataFrame, path: str = 'products.csv'):
    try:
        df.to_csv(path, index=False)
        logging.info(f"✅ Data saved to {path} ({len(df)} rows)")
    except Exception as e:
        logging.error(f"❌ Failed to save data to CSV: {e}")

def save_to_google_sheets(df: pd.DataFrame, sheet_name: str, credentials_path: str = 'google-sheets-api.json'):
    try:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
        client = gspread.authorize(creds)

        sheet = client.create(sheet_name)
        sheet.share('lucaschandra18@gmail.com', perm_type='user', role='writer')  # Supaya bisa diakses
        worksheet = sheet.sheet1
        set_with_dataframe(worksheet, df)

        logging.info(f"✅ Data saved to Google Sheets: {sheet_name} ({len(df)} rows)")
        logging.info(f"🔗 Google Sheet URL: {sheet.url}")  # Menampilkan URL
    except Exception as e:
        logging.error(f"❌ Failed to save to Google Sheets: {e}")


def save_to_postgresql(df: pd.DataFrame, table_name: str = 'fashion_products'):
    try:
        db_url = os.getenv("POSTGRES_URL")
        engine = create_engine(db_url)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        logging.info(f"✅ Data saved to PostgreSQL table: {table_name} ({len(df)} rows)")
    except Exception as e:
        logging.error(f"❌ Failed to save data to PostgreSQL: {e}")
