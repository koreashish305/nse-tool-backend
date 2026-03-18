import requests

BASE_URL = "https://www.nseindia.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Referer": BASE_URL,
    "Accept-Encoding": "gzip, deflate, br",
}

def get_session():
    session = requests.Session()
    session.headers.update(headers)
    # Load homepage to get cookies
    session.get(BASE_URL, timeout=5)
    return session

def get_sector_indices():
    session = get_session()
    url = f"{BASE_URL}/api/allIndices"
    res = session.get(url, timeout=10)
    res.raise_for_status()
    data = res.json()

    indices = []
    for item in data["data"]:
        indices.append({
            "name": item["indexName"],
            "last_price": item["last"],
            "change_pct": item["variation"],
        })
    return indices

def get_stocks_in_index(index_name: str):
    session = get_session()
    url = f"{BASE_URL}/api/equity-stockIndices?index={index_name}"
    res = session.get(url, timeout=10)
    res.raise_for_status()
    data = res.json()

    stocks = []
    for item in data["data"]:
        stocks.append({
            "symbol": item["symbol"],
            "name": item["symbol"],
            "current_volume": item.get("quantityTraded", 0),
            "avg_volume": item.get("totalTradedVolume", 1),
            "prices": [item["lastPrice"]],
        })
    return stocks
