"""
Trade Pilot AI v2
Market Engine
"""

import logging

from services.binance_service import binance_service
from services.indicator_service import indicator_service
from services.volume_service import volume_service
from services.score_service import score_service
from services.open_interest_service import open_interest_service
from services.cvd_service import cvd_service
from services.liquidation_service import liquidation_service
from services.ai_service import ai_service
from services.trend_service import trend_service
from services.risk_service import risk_service

logger = logging.getLogger(__name__)


class MarketEngine:

    def analyze(self, symbol="BTCUSDT", timeframe="1h"):

        try:

            # ==========================
            # Market Data
            # ==========================

            df = binance_service.get_ohlcv(
                symbol=symbol,
                timeframe=timeframe,
                limit=300
            )

            # ==========================
            # Indicators
            # ==========================

            df = indicator_service.calculate(df)

            last = df.iloc[-1]

            # ==========================
            # Volume
            # ==========================

            volume = volume_service.analyze(df)

            # ==========================
            # Trade Score
            # ==========================

            score = score_service.calculate(df)

            # ==========================
            # Open Interest
            # ==========================

            try:
                open_interest = open_interest_service.get_open_interest(symbol)
            except Exception:
                open_interest = None

            # ==========================
            # CVD
            # ==========================

            try:
                cvd = cvd_service.calculate(df)
            except Exception:
                cvd = None

            # ==========================
            # Long / Short Ratio
            # ==========================

            try:
                liquidation = liquidation_service.get_long_short_ratio(symbol)
            except Exception:
                liquidation = None

            # ==========================
            # Market Object
            # ==========================

            market = {

                "symbol": symbol,
                "timeframe": timeframe,

                "price": round(float(last["close"]), 2),

                "ema20": round(float(last["EMA20"]), 2),
                "ema50": round(float(last["EMA50"]), 2),
                "ema200": round(float(last["EMA200"]), 2),

                "rsi": round(float(last["RSI"]), 2),

                "macd": round(float(last["MACD"]), 4),
                "macd_signal": round(float(last["MACD_SIGNAL"]), 4),

                "atr": round(float(last["ATR"]), 2),

                "adx": round(float(last["ADX"]), 2),

                "score": score

            }

            # ==========================
            # Trend Analysis
            # ==========================

            trend = trend_service.analyze(market)

            # ==========================
            # Risk Analysis
            # ==========================

            risk = risk_service.calculate(
                market=market,
                trend=trend
            )

            # ==========================
            # AI Analysis
            # ==========================

            ai = ai_service.analyze(
                market=market,
                open_interest=open_interest,
                cvd=cvd,
                liquidation=liquidation
            )

            # ==========================
            # Final Result
            # ==========================

            return {

                "market": market,

                "volume": volume,

                "open_interest": open_interest,

                "cvd": cvd,

                "liquidation": liquidation,

                "trend": trend,

                "risk": risk,

                "ai": ai

            }

        except Exception as e:

            logger.exception("Market Engine Error")

            raise Exception(f"Market Engine Error: {e}")


market_engine = MarketEngine()
