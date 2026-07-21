"""
Trade Pilot AI v2
Risk Service
"""

import logging

logger = logging.getLogger(__name__)


class RiskService:

    def calculate(self, market, trend):

        price = market["price"]
        atr = market["atr"]

        signal = trend["trend"]

        # LONG
        if signal == "BULLISH":

            entry = price

            stop_loss = price - (atr * 1.5)

            tp1 = price + (atr * 2)

            tp2 = price + (atr * 4)

            tp3 = price + (atr * 6)

        # SHORT
        elif signal == "BEARISH":

            entry = price

            stop_loss = price + (atr * 1.5)

            tp1 = price - (atr * 2)

            tp2 = price - (atr * 4)

            tp3 = price - (atr * 6)

        # SIDEWAYS
        else:

            entry = price

            stop_loss = price

            tp1 = price

            tp2 = price

            tp3 = price

        risk = abs(entry - stop_loss)
        reward = abs(tp2 - entry)

        rr = round(reward / risk, 2) if risk > 0 else 0

        return {

            "entry": round(entry, 2),

            "stop_loss": round(stop_loss, 2),

            "tp1": round(tp1, 2),

            "tp2": round(tp2, 2),

            "tp3": round(tp3, 2),

            "risk_reward": rr

        }


risk_service = RiskService()
