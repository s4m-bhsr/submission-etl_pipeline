import unittest
from unittest.mock import patch, MagicMock
from utils.extract import fetch_products_from_url

class TestExtract(unittest.TestCase):

    @patch('utils.extract.requests.get')
    def test_fetch_products_from_url_success(self, mock_get):
        # Arrange
        url = "https://fashion-studio.dicoding.dev/"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = """
        <html>
            <body>
                <div class="collection-card">
                    <h3 class="product-title">Test Product</h3>
                    <div class="price-container">$10</div>
                    <p>Rating: 5 stars</p>
                    <p>Colors: Red, Blue</p>
                    <p>Size: M, L</p>
                    <p>Gender: Unisex</p>
                </div>
            </body>
        </html>
        """
        mock_get.return_value = mock_response

        # Act
        result = fetch_products_from_url(url)

        # Assert
        self.assertIsInstance(result, list)  # Memastikan hasil adalah list
        self.assertGreater(len(result), 0)  # Memastikan ada produk yang ditemukan
        self.assertIn('title', result[0])  # Memastikan ada field 'title' pada produk
        self.assertEqual(result[0]['title'], 'Test Product')  # Memastikan judul produk benar

    @patch('utils.extract.requests.get')
    def test_fetch_products_from_url_failure(self, mock_get):
        # Arrange
        url = "https://fashion-studio.dicoding.dev/"
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = Exception("404 Client Error")  # Simulasikan error
        mock_get.return_value = mock_response

        # Act & Assert
        with self.assertRaises(RuntimeError) as context:
            fetch_products_from_url(url)
        self.assertIn("Unable to access", str(context.exception))

    @patch('utils.extract.fetch_products_from_url')
    def test_collect_all_products(self, mock_fetch):
        mock_fetch.return_value = [{'title': 'Product', 'price': '10000', 'rating': '4', 'colors': '3', 'size': 'M', 'gender': 'Men'}]
    
        from utils.extract import collect_all_products
        result = collect_all_products(max_pages=3)
    
        self.assertEqual(len(result), 3)  # 1 item per page × 3 pages
        self.assertEqual(mock_fetch.call_count, 3)



if __name__ == '__main__':
    unittest.main()
