import unittest
from unittest.mock import patch, MagicMock
from src.utils.csv_exporter import CsvExporter

class TestCsvExporter(unittest.TestCase):

    def setUp(self):
        self.exporter = CsvExporter()
        # Create a mock for the arxiv.Result object
        self.mock_result = MagicMock()
        self.mock_result.title = "Test Title"
        author1 = MagicMock()
        author1.name = "Author 1"
        author2 = MagicMock()
        author2.name = "Author 2"
        self.mock_result.authors = [author1, author2]
        self.mock_result.published = "2023-01-01"
        self.mock_result.summary = "This is a test summary."
        self.mock_result.entry_id = "http://arxiv.org/abs/2301.00001"

        self.mock_results = [self.mock_result]

    @patch('csv.DictWriter')
    def test_export_success(self, mock_dict_writer):
        """Test successful CSV export."""
        # Mock the writer instance and its methods
        mock_writer_instance = MagicMock()
        mock_dict_writer.return_value = mock_writer_instance

        with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            filename = "test_export.csv"
            self.exporter.export(self.mock_results, filename)

            # Check that open was called correctly
            mock_file.assert_called_once_with(filename, "w", newline="", encoding="utf-8")

            # Check that DictWriter was called with the correct fieldnames
            mock_dict_writer.assert_called_with(mock_file(), fieldnames=["title", "authors", "published", "summary", "entry_id"])

            # Check that writeheader and writerow were called
            mock_writer_instance.writeheader.assert_called_once()
            mock_writer_instance.writerow.assert_called_once_with({
                "title": "Test Title",
                "authors": "Author 1, Author 2",
                "published": "2023-01-01",
                "summary": "This is a test summary.",
                "entry_id": "http://arxiv.org/abs/2301.00001"
            })

    @patch('builtins.open')
    def test_export_error(self, mock_open):
        """Test that an error during file write is handled."""
        mock_open.side_effect = IOError("File write error")
        with patch('builtins.print') as mock_print:
            self.exporter.export(self.mock_results)
            mock_print.assert_called_with("An error occurred during CSV export: File write error")

if __name__ == '__main__':
    unittest.main()