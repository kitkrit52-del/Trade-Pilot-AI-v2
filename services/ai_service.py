"""
Trade Pilot AI v2
AI Service
"""

import logging

logger = logging.getLogger(__name__)


class AIService:

    def analyze(
        self,
        market,
        open_interest=None,
        cvd=None,
        liquidation=None
    ):
        """
        AI Recommendation Engine
        """

        score = market["score"]

        reasons = []

        # ==========================
        # EMA Analysis
        # ==========================

        if market["ema20"] > market["ema50"] > market["ema200"]:
            reasons.append("EMA підтверджує висхідний тренд")

        elif market["ema20"] < market["ema50"] < market["ema200"]:
            reasons.append("EMA підтверджує низхідний тренд")

        # ==========================
        # RSI Analysis
        # ==========================

        if market["rsi"] > 55:
            reasons.append("RSI підтримує покупців")

        elif market["rsi"] < 45:
            reasons.append("RSI підтримує продавців")

        # ==========================
        # ADX Analysis
        # ==========================

        if market["adx"] >= 25:
            reasons.append("Сильний тренд (ADX ≥ 25)")

        # ==========================
        # MACD Analysis
        # ==========================

        if market["macd"] > market["macd_signal"]:
            reasons.append("MACD Bullish")

        else:
            reasons.append("MACD Bearish")

        # ==========================
        # Open Interest
        # ==========================

        if (
            open_interest
            and isinstance(open_interest, dict)
            and "open_interest" in open_interest
        ):
            reasons.append(
                f"Open Interest: {open_interest['open_interest']:.2f}"
            )

        # ==========================
        # CVD
        # ==========================

        if (
            cvd
            and isinstance(cvd, dict)
            and "direction" in cvd
        ):
            reasons.append(
                f"CVD: {cvd['direction']}"
            )

        # ==========================
        # Long / Short Ratio
        # ==========================

        if liquidation and isinstance(liquidation, dict):

            ratio = liquidation.get("long_short_ratio", 1)

            if ratio > 1:
                reasons.append("Перевага LONG-позицій")

            elif ratio < 1:
                reasons.append("Перевага SHORT-позицій")

            else:
                reasons.append("LONG / SHORT баланс")

        # ==========================
        # Recommendation
        # ==========================

        if score >= 80:
            signal = "🟢 STRONG LONG"

        elif score >= 60:
            signal = "🟢 LONG"

        elif score >= 40:
            signal = "🟡 WAIT"

        else:
            signal = "🔴 SHORT"

        confidence = min(score + 10, 99)

        logger.info(
            f"AI Signal: {signal} | Score: {score} | Confidence: {confidence}%"
        )

        return {
            "signal": signal,
            "score": score,
            "confidence": confidence,
            "reasons": reasons
        }


ai_service = AIService()
