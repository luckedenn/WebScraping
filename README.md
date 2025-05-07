# Web Scraping
## ETL Pipeline Project

## Cara Menjalankan Script ETL Pipeline

1.  **Aktifkan virtual environment** (jika belum):
    * **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

2.  **Jalankan pipeline utama:**
    ```bash
    python main.py
    ```

## Cara Menjalankan Unit Test

1.  **Jalankan unit test** dengan `unittest`:
    ```bash
    python -m unittest discover -s tests
    ```

## Cara Menjalankan Test Coverage

1.  **Pastikan `coverage` sudah terinstal:**
    ```bash
    pip install coverage
    ```

2.  **Jalankan coverage** untuk direktori `utils` dan folder `tests`:
    ```bash
    coverage run -m unittest discover -s tests
    ```

3.  **Tampilkan laporan coverage:**
    ```bash
    coverage report -m
    ```

## URL Google Sheets

Data hasil ETL dapat dilihat di:
[https://docs.google.com/spreadsheets/d/1bx-TIm7zvBMdYr4qkbKkpK-TGUnuvCG8HH8FV00xCDw/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1bx-TIm7zvBMdYr4qkbKkpK-TGUnuvCG8HH8FV00xCDw/edit?usp=sharing)
