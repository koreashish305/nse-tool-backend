from fastapi import FastAPI
from nse_scraper import get_sector_indices, get_stocks_in_index
import math

app = FastAPI()

def calculate_rsi(prices):
    gains = [max(0, prices[i+1]-prices[i]) for i in range(len(prices)-1)]
    losses = [max(0, prices[i]-prices[i+1]) for i in range(len(prices)-1)]
    avg_gain = sum(gains)/len(gains) if gains else 0
    avg_loss = sum(losses)/len(losses) if losses else 0
    rs = avg_gain / avg_loss if avg_loss != 0 else math.inf
    return round(100 - (100/(1+rs)), 2)

@app.get("/indices")
def list_indices():
    return get_sector_indices()

@app.get("/stocks")
def list_stocks(index: str):
    data = get_stocks_in_index(index)
    results = []
    for stock in data:
        volume_ratio = stock['current_volume'] / stock['avg_volume']
        if volume_ratio > 2:  # High volume threshold
            results.append({
                "name": stock['name'],
                "symbol": stock['symbol'],
                "volume_ratio": round(volume_ratio, 2),
                "momentum": calculate_rsi(stock['prices']),
                "link": f"https://www.tradingview.com/chart/?symbol=NSE:{stock['symbol']}"
            })
    return results
