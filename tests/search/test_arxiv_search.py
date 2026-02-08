import unittest
from unittest.mock import patch, MagicMock
import arxiv
from src.search.arxiv_search import ArxivSearch

class TestArxivSearch(unittest.TestCase):
    @patch('arxiv.Search')
    def test_search_success(self, mock_search):
        # Mock the arxiv.Search object and its results
        mock_results = [MagicMock(), MagicMock()]
        mock_search.return_value.results.return_value = mock_results

        # Create an instance of our class and call the search method
        searcher = ArxivSearch()
        results = searcher.search(query="test query", max_results=2)

        # Assert that arxiv.Search was called with the correct parameters
        mock_search.assert_called_with(
            query="test query",
            max_results=2,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )

        # Assert that we got back the mocked results
        self.assertEqual(len(results), 2)
        self.assertEqual(results, mock_results)

    @patch('arxiv.Search')
    def test_search_error(self, mock_search):
        # Configure the mock to raise an exception
        mock_search.side_effect = Exception("Test error")

        # Create an instance of our class and call the search method
        searcher = ArxivSearch()
        results = searcher.search(query="test query")

        # Assert that the method returns an empty list
        self.assertEqual(results, [])

if __name__ == '__main__':
    unittest.main()
