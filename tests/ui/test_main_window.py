import unittest
from unittest.mock import patch, MagicMock
import customtkinter
from src.ui.main_window import MainWindow

class TestMainWindow(unittest.TestCase):
    @patch('src.ui.main_window.ArxivSearch')
    @patch('src.ui.main_window.CsvExporter')
    def setUp(self, mock_csv_exporter, mock_arxiv_search):
        self.app = MainWindow()

    def tearDown(self):
        self.app.destroy()

    @patch('src.ui.main_window.threading.Thread')
    def test_start_search_thread(self, mock_thread):
        """Test that a search thread is started."""
        self.app.search_entry.get = MagicMock(return_value="test query")
        self.app.validate_inputs = MagicMock(return_value=True)
        self.app.start_search_thread()
        mock_thread.assert_called_once()

    def test_validate_inputs_valid(self):
        """Test input validation with valid inputs."""
        self.app.start_date_entry.get = MagicMock(return_value="2023-01-01")
        self.app.end_date_entry.get = MagicMock(return_value="2023-01-31")
        self.app.max_results_entry.get = MagicMock(return_value="10")
        self.assertTrue(self.app.validate_inputs())

    @patch('tkinter.messagebox.showerror')
    def test_validate_inputs_invalid_date(self, mock_showerror):
        """Test input validation with an invalid date."""
        self.app.start_date_entry.get = MagicMock(return_value="2023-01-01")
        self.app.end_date_entry.get = MagicMock(return_value="invalid-date")
        self.app.max_results_entry.get = MagicMock(return_value="10")
        self.assertFalse(self.app.validate_inputs())
        mock_showerror.assert_called_once()

    @patch('tkinter.messagebox.showerror')
    def test_validate_inputs_invalid_max_results(self, mock_showerror):
        """Test input validation with an invalid max results."""
        self.app.start_date_entry.get = MagicMock(return_value="2023-01-01")
        self.app.end_date_entry.get = MagicMock(return_value="2023-01-31")
        self.app.max_results_entry.get = MagicMock(return_value="abc")
        self.assertFalse(self.app.validate_inputs())
        mock_showerror.assert_called_once()

if __name__ == '__main__':
    unittest.main()