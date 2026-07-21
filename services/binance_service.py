"""
Trade Pilot AI v2
Binance Service
"""

import logging

import ccxt
import pandas as pd

from config import (
    BINANCE_DEFAULT_TYPE,
    BINANCE_RATE_LIMIT,
)

logger = logging.getLogger(__name__)


class BinanceService:

    def __init__(self):

        self.exchange = ccxt.binance({
            "enableRateLimit": BINANCE_RATE_LIMIT,
            "options": {
                "defaultType": BINANCE_DEFAULT_TYPE
            }
        })

    def check_connection(self):
        """Перевірка підключення до Binance"""

        try:
            self.exchange.load_markets()
            logger.info("Binance connection successful.")
            return True

        except Exception as e:
            logger.exception("Binance connection failed.")
            raise Exception(f"Binance connection error: {e}")

    def get_price(self, symbol="BTCUSDT"):
        """Поточна ціна"""

        try:

            pair = symbol.replace("USDT", "/USDT")

            ticker = self.exchange.fetch_ticker(pair)

            return float(ticker["last"])

        except Exception as e:
            logger.exception("Price error")
            raise Exception(f"Price error: {e}")

    def get_ticker(self, symbol="BTCUSDT"):
        """Повний тикер"""

        try:

            pair = symbol.replace("USDT", "/USDT")

            return self.exchange.fetch_ticker(pair)

        except Exception as e:
            logger.exception("Ticker error")
            raise Exception(f"Ticker error: {e}")

    def get_ohlcv(
        self,
        symbol="BTCUSDT",
        timeframe="1h",
        limit=300
    ):
        """Отримання історії свічок"""

        try:

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

            df = df.astype({
                "open": float,
                "high": float,
                "low": float,
                "close": float,
                "volume": float
            })

            return df

        except Exception as e:
            logger.exception("OHLCV error")
            raise Exception(f"OHLCV error: {e}")

    def get_markets(self):
        """Список доступних ринків"""

        try:

            return self.exchange.load_markets()

        except Exception as e:
            logger.exception("Markets error")
            raise Exception(f"Markets error: {e}")


binance_service = BinanceService()
