import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from utils.load import save_to_csv, save_to_google_sheets

class TestLoad(unittest.TestCase):

    @patch('utils.load.pd.DataFrame.to_csv')
    def test_save_to_csv(self, mock_to_csv):
        # Arrange
        df = pd.DataFrame({
            'title': ['Product 1', 'Product 2'],
            'price': [10000, 20000],
            'rating': [4.5, 5.0]
        })
        
        # Act
        save_to_csv(df, 'test.csv')
        
        # Assert
        mock_to_csv.assert_called_once_with('test.csv', index=False)

    @patch('utils.load.build')
    @patch('utils.load.Credentials.from_service_account_file')
    def test_save_to_google_sheets(self, mock_creds, mock_build):
        # Arrange
        df = pd.DataFrame({
            'title': ['Product 1', 'Product 2'],
            'price': [10000, 20000],
            'rating': [4.5, 5.0]
        })
        
        mock_creds.return_value = MagicMock()
        mock_service = MagicMock()
        mock_build.return_value = mock_service
        
        # Act
        save_to_google_sheets(df, 'spreadsheet_id', 'Sheet1!A2')
        
        # Assert
        mock_service.spreadsheets.return_value.values.return_value.update.assert_called_once()

    @patch('utils.load.create_engine')
    def test_save_to_postgres(self, mock_engine):
        import pandas as pd
        from utils.load import save_to_postgres
    
        df = pd.DataFrame({
            'title': ['Product'],
            'price': [10000],
            'rating': [4.5]
        })
    
        mock_conn = MagicMock()
        mock_engine.return_value = mock_conn
    
        save_to_postgres(df, table_name='test_products')
        mock_conn.dispose.assert_not_called()  # Just example check


if __name__ == '__main__':
    unittest.main()