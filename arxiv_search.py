import arxiv

def search_arxiv(query, max_results=5):
    """
    Searches arXiv for articles matching the query and prints their details.
    """
    print(f"Searching arXiv for '{query}'...")

    # Construct the default API client.
    client = arxiv.Client()

    # Search for articles.
    # The query can be a simple string or a more complex arXiv API query.
    # For example, 'cat:cs.AI' for AI papers, or 'au:"John Doe"' for a specific author.
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance,
        sort_order=arxiv.SortOrder.Descending
    )

    results_list = list(client.results(search))
    print(f"Found {len(results_list)} results for '{query}':")
    for i, result in enumerate(results_list):
        print(f"--- Result {i+1} ---")
        print(f"Title: {result.title}")
        print(f"Abstract: {result.summary}")
        print(f"PDF Link: {result.pdf_url}")

if __name__ == "__main__":
    # Example 1: Search for papers in Life Sciences (Quantitative Biology)
    search_arxiv("cat:q-bio", max_results=3)

    print("\n" + "="*50 + "\n")

    # Example 2: Search for papers by a specific author in a specific category
    # Note: The query syntax follows the arXiv API guidelines.
    # 'au:kording' for author Kording, 'ti:deep+AND+ti:learning' for title with 'deep' and 'learning'
    search_arxiv("cat:cs.AI AND ti:'large language model'", max_results=2)

    print("\n" + "="*50 + "\n")

    # Example 3: You can also ask the user for a custom query
    # custom_query = input("Enter your arXiv search query: ")
    # search_arxiv(custom_query, max_results=5)
