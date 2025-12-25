import requests
from bs4 import BeautifulSoup
from models import SearchEngine, Document
from tokenizer import tokenize

def crawl(seeds: list, max_pages: int, engine: SearchEngine):
    queue = seeds[:]
    seen = set()

    while queue and len(engine.documents) < max_pages:
        url = queue.pop(0)

        if url in seen:
            continue
        
        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                continue

            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else 'No Title'
            text_content = soup.get_text()

            doc_id = len(engine.documents)
            new_doc = Document(id=doc_id, url=url, title=title, content=text_content)
            engine.documents.append(new_doc)

            words = tokenize(text_content)
            for word in words:
                if word not in engine.index:
                    engine.index[word] = []

                engine.index[word].append(doc_id)
                
            seen.add(url)   
            printf(f"Crawled: {url}")

            for link in soup.find_all('a', href=True):
                full_url = urljoin(url, link['href'])
                if full_url not in seen:
                    queue.append(full_url)
        except Exception as e:
            print(f"Failed to crawl {url}: {e}")    