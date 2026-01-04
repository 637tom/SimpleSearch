# Simple Search Engine

A simple web search engine built with Python. The project consists of a crawler that downloads pages and a web interface (Flask) for searching them.

## How it works

The project is divided into several modules:
- **Crawler (`src/crawler.py`)**: Runs in the background (using threads). Visits seed URLs, downloads their content, and discovers new links.
- **Index (`src/models.py`)**: Downloaded text is stored in memory (RAM). An "inverted index" (map: word -> list of pages) is created for fast searching (O(1)).
- **Search Engine (`src/app.py`)**: Flask server that provides the web page and API endpoints.
- **Frontend (`src/static/`)**: Simple HTML/CSS/JS interface. Supports dark mode and shows text snippets in results.

## Setup

1. **Environment** (using Conda):
   ```bash
   conda env update --file environment.yml --prune
   conda activate search-engine
   ```

2. **Run**:
   ```bash
   python src/app.py
   ```
   
   Once running, the crawler will start downloading pages (check console logs). The server will be available at `http://127.0.0.1:5000`.

   > **Note:** The crawler runs continuously in the background. The longer you keep the application running, the more pages will be indexed and available for search.

## Tech Stack

- **Python 3.10+**
- **Flask** (Web Backend)
- **BeautifulSoup4** (HTML Parsing)
- **Vanilla JavaScript** (Frontend logic)

## File Structure

- `src/app.py` - Main server file.
- `src/crawler.py` - Crawling logic (BFS algorithm).
- `src/tokenizer.py` - Text tokenization helper.
- `src/models.py` - Data structures (`Document` and `SearchEngine`).
- `src/templates/` & `src/static/` - UI files (HTML/CSS/JS).
