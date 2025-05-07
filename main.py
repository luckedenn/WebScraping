import argparse
import logging
from utils.extract import scrape_all
from utils.transform import clean_data
from utils.load import save_to_csv, save_to_google_sheets, save_to_postgresql

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler()]
    )

def main(pages, kurs, output, sheet_name, table_name):
    setup_logger()
    logging.info("🚀 Starting ETL Process...")

    raw_data = scrape_all(pages)
    cleaned_data = clean_data(raw_data, kurs=kurs)

    save_to_csv(cleaned_data, path=output)
    save_to_google_sheets(cleaned_data, sheet_name=sheet_name)
    save_to_postgresql(cleaned_data, table_name=table_name)

    logging.info("✅ ETL Process Completed!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fashion Studio ETL Pipeline")
    parser.add_argument("--pages", type=int, default=51, help="Number of pages to scrape")
    parser.add_argument("--kurs", type=int, default=16000, help="Dollar to Rupiah conversion rate")
    parser.add_argument("--output", type=str, default="products.csv", help="Output CSV filename")
    parser.add_argument("--sheet", type=str, default="Fashion Studio Data", help="Google Sheet name")
    parser.add_argument("--table", type=str, default="fashion_products", help="PostgreSQL table name")

    args = parser.parse_args()
    main(args.pages, args.kurs, args.output, args.sheet, args.table)
