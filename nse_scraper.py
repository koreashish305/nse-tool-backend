import requests

BASE_URL = "https://www.nseindia.com"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
}

def get_sector_indices():
    """
    Fetch live NSE sector indices from NSE API.
    """
    url = f"{BASE_URL}/api/allIndices"
    session = requests.Session()
    session.headers.update(headers)
    res = session.get(url)
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
    """
    Fetch live stock constituents for a given NSE index.
    """
    url = f"{BASE_URL}/api/equity-stockIndices?index={index_name}"
    session = requests.Session()
    session.headers.update(headers)
    res = session.get(url)
    res.raise_for_status()
    data = res.json()

    stocks = []
    for item in data["data"]:
        stocks.append({
            "symbol": item["symbol"],
            "name": item["symbol"],
            "current_volume": item.get("quantityTraded", 0),
            "avg_volume": item.get("totalTradedVolume", 1),  # fallback to avoid divide by zero
            "prices": [item["lastPrice"]],  # placeholder for RSI calculation
        })
    return stocks
