"""
Trade Pilot AI v2
Score Service
"""

import logging

logger = logging.getLogger(__name__)


class ScoreService:

    def calculate(self, df):
        """
        Trade Score (0-100)
        """

        last = df.iloc[-1]

        score = 0

        # ==========================
        # EMA Trend (40)
        # ==========================

        if last["EMA20"] > last["EMA50"]:
            score += 20

        if last["EMA50"] > last["EMA200"]:
            score += 20

        # ==========================
        # RSI (20)
        # ==========================

        if 50 <= last["RSI"] <= 70:
            score += 20

        # ==========================
        # MACD (20)
        # ==========================

        if last["MACD"] > last["MACD_SIGNAL"]:
            score += 20

        # ==========================
        # ADX (20)
        # ==========================

        if last["ADX"] >= 25:
            score += 20

        score = max(0, min(score, 100))

        logger.info(f"Trade Score: {score}")

        return score


score_service = ScoreService()
