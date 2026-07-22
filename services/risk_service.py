"""
Trade Pilot AI v2.2
Risk Service
"""

import logging

logger = logging.getLogger(__name__)


class RiskService:

    def calculate(self, market, trend, signal=None):

        price = market["price"]
        atr = market["atr"]

        # якщо сигнал не передали — беремо тренд
        if signal:
            direction = signal
        else:
            direction = trend["trend"]


        # LONG
        if "LONG" in direction or direction == "BULLISH":

            entry = price

            stop_loss = price - (atr * 1.5)

            tp1 = price + (atr * 2)

            tp2 = price + (atr * 4)

            tp3 = price + (atr * 6)


        # SHORT
        elif "SHORT" in direction or direction == "BEARISH":

            entry = price

            stop_loss = price + (atr * 1.5)

            tp1 = price - (atr * 2)

            tp2 = price - (atr * 4)

            tp3 = price - (atr * 6)


        # WAIT
        else:

            return {

                "entry": round(price, 2),
                "stop_loss": 0,
                "tp1": 0,
                "tp2": 0,
                "tp3": 0,
                "risk_reward": 0
            }


        risk = abs(entry - stop_loss)

        reward = abs(tp2 - entry)

        rr = round(
            reward / risk,
            2
        ) if risk > 0 else 0


        return {

            "entry": round(entry, 2),

            "stop_loss": round(stop_loss, 2),

            "tp1": round(tp1, 2),

            "tp2": round(tp2, 2),

            "tp3": round(tp3, 2),

            "risk_reward": rr

        }


risk_service = RiskService()
