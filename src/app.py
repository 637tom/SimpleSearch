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
    ]
    print("Starting initial crawl...")
    crawl(seeds, max_pages=50, engine=engine)
    print("Initial crawl finished!")

@app.route('/')
def home():
    return render_template('index.html')

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
                'url': doc.url
            })
    
    return jsonify(results)

if __name__ == '__main__':
    init_crawler()
    app.run(debug=True, use_reloader=False)
