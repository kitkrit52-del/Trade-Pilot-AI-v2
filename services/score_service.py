"""
Trade Pilot AI v2
Score Service
"""


class ScoreService:

    def calculate(self, df):
        """
        Розрахунок рейтингу торгового сигналу (0-100)
        """

        last = df.iloc[-1]

        score = 0

        # EMA
        if last["EMA20"] > last["EMA50"]:
            score += 20

        if last["EMA50"] > last["EMA200"]:
            score += 20

        # RSI
        if 50 <= last["RSI"] <= 70:
            score += 20

        # MACD
        if last["MACD"] > last["MACD_SIGNAL"]:
            score += 20

        # ADX
        if last["ADX"] > 25:
            score += 20

        return score


score_service = ScoreService()
