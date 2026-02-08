import arxiv

class ArxivSearch:
    def search(self, query, max_results=10):
        try:
            search = arxiv.Search(
                query=query,
                max_results=max_results,
                sort_by=arxiv.SortCriterion.SubmittedDate
            )
            return search.results()
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
