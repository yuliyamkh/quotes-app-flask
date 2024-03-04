import pandas as pd
from typing import List

DATA = pd.read_json('data/quotes.json')
CATEGORIES = [c for c in DATA.Category.unique().tolist() if c and c != 'quotes']


def get_quotes(category: str) -> List:

    quotes = DATA.loc[DATA['Category'] == category, 'Quote'].sample(n=10)
    return quotes.tolist(