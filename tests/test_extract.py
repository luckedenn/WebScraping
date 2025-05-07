import unittest
from utils.extract import scrape_all

class TestExtract(unittest.TestCase):
    def test_scrape_all(self):
        data = scrape_all(pages=1)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIn('title', data[0])
        self.assertIn('price', data[0])

if __name__ == "__main__":
    unittest.main()
