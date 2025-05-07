import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import logging

def scrape_page(page_num, retries=3, delay=2):
    url = "https://fashion-studio.dicoding.dev/" if page_num == 1 else f"https://fashion-studio.dicoding.dev/page{page_num}"
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            products = soup.select(".collection-card")
            data = []
            for product in products:
                title_tag = product.select_one(".product-title")
                price_span = product.select_one(".price-container .price")
                price_p = product.select_one("p.price")
                ps = product.find_all("p")
                title = title_tag.text.strip() if title_tag else None
                price = price_span.text.strip() if price_span else (None if price_p and "Unavailable" in price_p.text else price_p.text.strip())
                rating = ps[0].text.split(":")[-1].strip() if len(ps) > 0 else None
                colors = ps[1].text.split()[0] if len(ps) > 1 else None
                size = ps[2].text.split(":")[-1].strip() if len(ps) > 2 else None
                gender = ps[3].text.split(":")[-1].strip() if len(ps) > 3 else None
                data.append({
                    "title": title,
                    "price": price,
                    "rating": rating,
                    "colors": colors,
                    "size": size,
                    "gender": gender,
                    "scrape_timestamp": datetime.utcnow().isoformat()
                })
            return data
        except Exception as e:
            attempt += 1
            logging.warning(f"Attempt {attempt} failed for page {page_num}: {e}")
            time.sleep(delay)
    logging.error(f"Failed to fetch page {page_num} after {retries} attempts.")
    return []

def scrape_all(pages=50):
    all_data = []
    for i in range(1, pages + 1):
        logging.info(f"Scraping page {i}...")
        all_data.extend(scrape_page(i))
    return all_data
