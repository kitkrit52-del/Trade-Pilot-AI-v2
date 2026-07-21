"""
Trade Pilot AI v2
Binance Service
"""

import ccxt


class BinanceService:

    def __init__(self):
        self.exchange = ccxt.binance({
            "enableRateLimit": True
        })

    def get_ohlcv(self, symbol="BTC/USDT", timeframe="1h", limit=200):
        return self.exchange.fetch_ohlcv(
            symbol=symbol,
            timeframe=timeframe,
            limit=limit
        )


binance_service = BinanceService()
