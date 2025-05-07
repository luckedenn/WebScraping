import unittest
import pandas as pd
from utils.transform import clean_data

class TestTransform(unittest.TestCase):
    def test_clean_data(self):
        dummy_data = pd.DataFrame({
            'title': ['Product A', 'Unknown Product'],
            'price': ['$10', '$20'],
            'rating': ['4.5 stars', 'invalid'],
            'colors': ['5', 'NaN'],
            'size': ['L', 'M'],
            'gender': ['Men', 'Women']
        })

        df = clean_data(dummy_data, kurs=15000)

        # Cek bahwa hanya 1 baris valid yang tersisa
        self.assertEqual(len(df), 1)

        # Cek apakah harga sudah dikonversi ke rupiah (150000 untuk $10)
        self.assertEqual(df['price'].iloc[0], 150000)

        # Pastikan rating dikonversi ke float
        self.assertIsInstance(df['rating'].iloc[0], float)

        # Cek apakah kolom baru 'clean_timestamp' ditambahkan
        self.assertIn('clean_timestamp', df.columns)

        # Pastikan tidak ada missing values
        self.assertFalse(df.isnull().values.any())
