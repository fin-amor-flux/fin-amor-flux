"""
OCR pipeline - female jongleurs
CC-BY-NC-SA 4.0
"""
import pandas as pd
from bs4 import BeautifulSoup

def extract_females(html_path):
    with open(html_path, encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')
    rows = []
    # exemple très simplifié
    for li in soup.select('li'):
        txt = li.get_text().lower()
        if 'cantadeira' in txt or 'jugleressa' in txt:
            rows.append({'raw': txt, 'tag': 'F'})
    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = extract_females('../data/01_raw/rolls_oleron.html')
    df.to_csv('../data/02_processed/females_oleron.csv', index=False)
