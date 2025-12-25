import re
from typing import List

def tokenize(text: str):
    text = text.lower()
    tokens = re.findall(r'[a-z]'{3,}, text)
    return list(set(tokens))