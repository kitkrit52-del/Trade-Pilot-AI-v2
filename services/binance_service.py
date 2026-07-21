"""
Trade Pilot AI v2
Binance Service
"""

import ccxt
import pandas as pd
import logging

logger = logging.getLogger(__name__)


class BinanceService:

    def __init__(self):
        self.exchange = ccxt.binance({
            "enableRateLimit": True,
            "options": {
                "defaultType": "future"
            }
        })

    def check_connection(self):
        """
        Перевірка з'єднання
        """

        try:
            self.exchange.load_markets()
            return True

        except Exception as e:
            logger.error(e)
            return False

    def get_price(self, symbol="BTCUSDT"):

        pair = symbol.replace("USDT", "/USDT")

        ticker = self.exchange.fetch_ticker(pair)

        return float(ticker["last"])

    def get_ticker(self, symbol="BTCUSDT"):

        pair = symbol.replace("USDT", "/USDT")

        return self.exchange.fetch_ticker(pair)

    def get_ohlcv(
            self,
            symbol="BTCUSDT",
            timeframe="1h",
            limit=500
    ):

        pair = symbol.replace("USDT", "/USDT")

        candles = self.exchange.fetch_ohlcv(
            pair,
            timeframe=timeframe,
            limit=limit
        )

        df = pd.DataFrame(
            candles,
            columns=[
                "timestamp",
                "open",
                "high",
                "low",
                "close",
                "volume"
            ]
        )

        df["timestamp"] = pd.to_datetime(
            df["timestamp"],
            unit="ms"
        )

        return df

    def markets(self):

        return self.exchange.load_markets()


binance_service = BinanceService()
