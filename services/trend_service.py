"""
Trade Pilot AI v2
Trend Service
"""

import logging

logger = logging.getLogger(__name__)


class TrendService:

    def analyze(self, market):

        ema20 = market["ema20"]
        ema50 = market["ema50"]
        ema200 = market["ema200"]

        adx = market["adx"]
        rsi = market["rsi"]

        trend = "SIDEWAYS"
        strength = "WEAK"
        rating = "C"

        # Bull Trend
        if ema20 > ema50 > ema200:

            trend = "BULLISH"

            if adx >= 30:
                strength = "STRONG"
                rating = "A+"

            elif adx >= 25:
                strength = "MEDIUM"
                rating = "A"

            else:
                strength = "WEAK"
                rating = "B"

        # Bear Trend
        elif ema20 < ema50 < ema200:

            trend = "BEARISH"

            if adx >= 30:
                strength = "STRONG"
                rating = "A+"

            elif adx >= 25:
                strength = "MEDIUM"
                rating = "A"

            else:
                strength = "WEAK"
                rating = "B"

        # RSI Warning
        warning = None

        if rsi > 75:
            warning = "Overbought"

        elif rsi < 25:
            warning = "Oversold"

        return {

            "trend": trend,
            "strength": strength,
            "rating": rating,
            "warning": warning

        }


trend_service = TrendService()
