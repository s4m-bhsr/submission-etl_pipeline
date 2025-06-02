import unittest
import pandas as pd
from utils.transform import transform_data

class TestTransform(unittest.TestCase):

    def test_transform_data(self):
        # Arrange
        products = [
            {'title': 'Product 1', 'price': '10000', 'rating': '4.5', 'colors': '3', 'size': 'M', 'gender': 'Men'},
            {'title': 'Product 2', 'price': '20000', 'rating': '5.0', 'colors': '3', 'size': 'L', 'gender': 'Women'}
        ]
        
        # Act
        df = transform_data(products)
        
        # Assert
        self.assertEqual(len(df), 2)
        self.assertIn('price', df.columns)
        self.assertIn('rating', df.columns)
        self.assertIn('timestamp', df.columns)
        self.assertTrue(df['price'].iloc[0] > 0)
        self.assertTrue(df['rating'].iloc[0] > 0)

    def test_invalid_price(self):
        # Arrange
        products = [
            {'title': 'Product 1', 'price': 'invalid_price', 'rating': '4.5', 'colors': '3', 'size': 'M', 'gender': 'Men'}
        ]
        
        # Act
        df = transform_data(products)
        
        # Assert
        self.assertEqual(len(df), 0)  # The product should be dropped due to invalid price

    def test_transform_data_with_unknown_product_and_duplicates(self):
        products = [
            {'title': 'Unknown Product', 'price': '10000', 'rating': '5.0', 'colors': '3', 'size': 'M', 'gender': 'Men'},
            {'title': 'Product 1', 'price': '10000', 'rating': '5.0', 'colors': '3', 'size': 'M', 'gender': 'Men'},
            {'title': 'Product 1', 'price': '10000', 'rating': '5.0', 'colors': '3', 'size': 'M', 'gender': 'Men'},  # Duplicate
        ]
        df = transform_data(products)
        self.assertEqual(len(df), 1)  # Harus tersisa 1 baris

if __name__ == '__main__':
    unittest.main()