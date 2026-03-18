import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.nseindia.com"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
}

def get_sector_indices():
    # Placeholder scraping logic (NSE HTML may change)
    url = f"{BASE_URL}/market-data/live-equity-market?tab=sectorIndices"
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    indices = []
    for row in soup.select("table tr"):
        cols = [c.get_text(strip=True) for c in row.select("td")]
        if len(cols) >= 3:
            indices.append({
                "name": cols[0],
                "last_price": cols[1],
                "change_pct": cols[2],
            })
    return indices

def get_stocks_in_index(index_name):
    # Dummy data for now (replace with NSE API calls later)
    return [
        {"symbol": "RELIANCE", "name": "Reliance Industries", "current_volume": 5000000, "avg_volume": 2000000, "prices": [2500, 2520, 2550]},
        {"symbol": "TATASTEEL", "name": "Tata Steel", "current_volume": 3000000, "avg_volume": 1000000, "prices": [100, 105, 110]},
    ]
