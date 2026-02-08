import csv

class CsvExporter:
    def export(self, results, filename="arxiv_results.csv"):
        try:
            with open(filename, "w", newline="", encoding="utf-8") as csvfile:
                fieldnames = ["title", "authors", "published", "summary", "entry_id"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for result in results:
                    writer.writerow({
                        "title": result.title,
                        "authors": ", ".join(author.name for author in result.authors),
                        "published": result.published,
                        "summary": result.summary,
                        "entry_id": result.entry_id
                    })
            print(f"Successfully exported results to {filename}")
        except Exception as e:
            print(f"An error occurred during CSV export: {e}")
