# Data Model

This document outlines the data entities for the arXiv Search UI feature.

## Paper

Represents a research paper.

| Attribute | Type | Description |
|---|---|---|
| `title` | String | The title of the paper. |
| `authors` | List[String] | A list of the paper's authors. |
| `publication_date` | Date | The date the paper was published. |
| `abstract` | String | The abstract or summary of the paper. |
| `url` | String | The URL to the paper on arXiv. |

## SearchParameters

Represents the user's search criteria.

| Attribute | Type | Description |
|---|---|---|
| `keywords` | String | The keywords to search for. |
| `start_date` | Date | The start of the date range for the search. |
| `end_date` | Date | The end of the date range for the search. |
| `author` | String | The author to filter by. |
| `max_results` | Integer | The maximum number of results to return. |
