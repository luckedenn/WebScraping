import unittest
import pandas as pd
import os
from utils.load import save_to_csv

class TestLoad(unittest.TestCase):
    def setUp(self):
        self.test_df = pd.DataFrame({'title': ['Shirt'], 'price_rp': [150000]})
        self.test_file = 'test_products.csv'

    def test_save_to_csv(self):
        save_to_csv(self.test_df, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))
        df_loaded = pd.read_csv(self.test_file)
        self.assertEqual(len(df_loaded), 1)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == "__main__":
    unittest.main()
