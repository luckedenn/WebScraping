import pandas as pd
import logging

def clean_data(raw_data, kurs=16000):
    df = pd.DataFrame(raw_data)
    if df.empty:
        logging.warning("No data to clean.")
        return df
    df = df[df['title'].str.lower() != 'unknown product']
    df = df[df['price'].notna()]
    df = df[df['price'].str.contains('$')]
    df = df[~df['rating'].str.lower().str.contains('invalid')]
    df['price'] = df['price'].str.replace('$', '', regex=False).astype(float) * kurs
    df['price'] = df['price'].astype(int)
    df['rating'] = df['rating'].str.extract(r'(\d+\.\d+)').astype(float)
    df['colors'] = pd.to_numeric(df['colors'], errors='coerce').astype('Int64')
    df['size'] = df['size'].str.strip()
    df['gender'] = df['gender'].str.strip()
    df['clean_timestamp'] = pd.Timestamp.utcnow()
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    return df