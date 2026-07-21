Trade Pilot AI v2
Market Engine
"""

from services.binance_service import binance_service
from services.indicator_service import indicator_service
from services.score_service import score_service


class MarketEngine:

    def analyze(
        self,
        symbol="BTCUSDT",
        timeframe="1h"
    ):
        """
        Повний аналіз ринку
        """

        # Отримуємо свічки
        df = binance_service.get_ohlcv(
            symbol=symbol,
            timeframe=timeframe,
            limit=300
        )

        # Розраховуємо індикатори
        df = indicator_service.calculate(df)

        # Розрахунок Score
        score = score_service.calculate(df)

        # Остання свічка
        last = df.iloc[-1]

        return {
            "symbol": symbol,
            "timeframe": timeframe,
            "price": round(float(last["close"]), 2),
            "ema20": round(float(last["EMA20"]), 2),
            "ema50": round(float(last["EMA50"]), 2),
            "ema200": round(float(last["EMA200"]), 2),
            "rsi": round(float(last["RSI"]), 2),
            "adx": round(float(last["ADX"]), 2),
            "macd": round(float(last["MACD"]), 4),
            "score": score
        }


market_engine = MarketEngine()

