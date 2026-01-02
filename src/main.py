from models import SearchEngine
from crawler import crawl

def run_search_engine():
    engine = SearchEngine()

    seeds = [
        "https://en.wikipedia.org/wiki/Python_(programming_language)",
        "https://www.python.org/downloads/",
        "https://www.apple.com/",
    ]
    
    crawl(seeds, max_pages=100, engine=engine)

    while True:
        query = input("Enter search query (or 'exit' to quit): ")
        query = query.lower()
        if query == 'exit':
            break

        if query in engine.index:
            results_ids =  engine.index[query]
            print(f"Found {len(results_ids)} results for '{query}':")
            for doc_id in results_ids:
                doc = engine.documents[doc_id]
                print(f"- {doc.title} ({doc.url})")
        else:
            print(f"No results found for '{query}'.")

        print("-" * 30)

if __name__ == "__main__":
    run_search_engine()