from flask import Flask, render_template, request, jsonify
from models import SearchEngine
from crawler import crawl
import threading

app = Flask(__name__)
engine = SearchEngine()

def init_crawler():
    seeds = [
        "https://en.wikipedia.org/wiki/Python_(programming_language)",
        "https://www.python.org/downloads/",
        "https://www.apple.com/",
        "https://github.com/explore",
        "https://stackoverflow.com/",
        "https://www.bbc.com/news",
        "https://www.onet.pl",
        "https://codeforces.com",
        "https://atcoder.jp",
        "https://www.wikipedia.org/",
        "https://www.khanacademy.org/",
        "https://www.nasa.gov/",
        "https://www.nationalgeographic.com/",
        "https://www.ted.com/",
        "https://www.youtube.com/",
        "https://usaco.guide/dashboard/",
        "https://www.w3schools.com",
        "https://leetcode.com"
    ]

    print("Starting initial crawl...")
    crawl(seeds, max_pages=1000, engine=engine)
    print("Initial crawl finished!")

@app.route('/')
def home():
    return render_template('index.html')

def get_snippet(text: str, query: str) -> str:
    query_lower = query.lower()
    text_lower = text.lower()
    
    try:
        start_index = text_lower.index(query_lower)
        start = max(0, start_index - 50)
        end = min(len(text), start_index + len(query) + 50)
        snippet = text[start:end]
        
        if start > 0:
            snippet = "..." + snippet
        if end < len(text):
            snippet = snippet + "..."
            
        return snippet
    except ValueError:
        return text[:100] + "..."

@app.route('/api/search')
def search():
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify([])

    results = []
    if query in engine.index:
        results_ids = engine.index[query]
        for doc_id in results_ids:
            doc = engine.documents[doc_id]
            results.append({
                'title': doc.title,
                'url': doc.url,
                'snippet': get_snippet(doc.content, query)
            })
    
    return jsonify(results)

if __name__ == '__main__':
    crawler_thread = threading.Thread(target=init_crawler)
    crawler_thread.start()
    app.run(debug=True, use_reloader=False)
