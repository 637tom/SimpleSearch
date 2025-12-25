from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class Document:
    id: int
    url: str
    title: str
    content: str

class SearchEngine:

    def __init__(self):
        self.documents: List[Document]
        self.index: Dict[str, List[int]] = {}