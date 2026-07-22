"""
Trade Pilot AI v3
AI Analyst Service
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

        score = market["score"]

        strengths = []
        weaknesses = []

        readiness = 0

        # ==========================
        # EMA
        # ==========================

        bullish = (
            market["ema20"] >
            market["ema50"] >
            market["ema200"]
        )

        bearish = (
            market["ema20"] <
            market["ema50"] <
            market["ema200"]
        )

        if bullish:
            strengths.append("EMA підтверджує висхідний тренд")
            readiness += 25

        elif bearish:
            strengths.append("EMA підтверджує низхідний тренд")
            readiness += 25

        else:
            weaknesses.append("EMA без чіткої структури")

        # ==========================
        # RSI
        # ==========================

        rsi = market["rsi"]

        if 55 <= rsi <= 70:
            strengths.append("RSI підтримує покупців")
            readiness += 10

        elif 30 <= rsi <= 45:
            strengths.append("RSI підтримує продавців")
            readiness += 10

        else:
            weaknesses.append("RSI нейтральний")

        # ==========================
        # ADX
        # ==========================

        if market["adx"] >= 25:
            strengths.append("Сильний тренд")
            readiness += 15

        else:
            weaknesses.append("Слабкий тренд (ADX)")

        # ==========================
        # MACD
        # ==========================

        if market["macd"] > market["macd_signal"]:
            strengths.append("MACD Bullish")
            readiness += 15

        else:
            weaknesses.append("MACD Bearish")

        # ==========================
        # CVD
        # ==========================

        if cvd:

            if cvd.get("direction") == "BUYERS":
                strengths.append("Покупці домінують (CVD)")
                readiness += 10

            elif cvd.get("direction") == "SELLERS":
                weaknesses.append("Продавці домінують (CVD)")

        # ==========================
        # Open Interest
        # ==========================

        if open_interest:

            strengths.append("Open Interest активний")
            readiness += 10

        # ==========================
        # Long / Short
        # ==========================

        if liquidation:

            ratio = liquidation.get(
                "long_short_ratio",
                1
            )

            if ratio > 1:
                strengths.append("LONG переважає")
                readiness += 5

            elif ratio < 1:
                weaknesses.append("SHORT переважає")

        # ==========================
        # Readiness
        # ==========================

        readiness = min(readiness, 100)

        # ==========================
        # Market Bias
        # ==========================

        if bullish:
            bias = "🟢 BULLISH"

        elif bearish:
            bias = "🔴 BEARISH"

        else:
            bias = "🟡 SIDEWAYS"

        # ==========================
        # Trading Scenario
        # ==========================

        if readiness >= 80:

            signal = "🟢 READY LONG"

            risk = "LOW"

        elif readiness >= 60:

            signal = "🟡 WAIT CONFIRMATION"

            risk = "MEDIUM"

        else:

            signal = "⚪ NO TRADE"

            risk = "HIGH"

        # ==========================
        # Summary
        # ==========================

        summary = (
            f"Ринок має {bias.lower()} сценарій. "
            f"Готовність до входу {readiness}%."
        )

        logger.info(
            f"{signal} | Readiness={readiness}"
        )

        return {

            "signal": signal,

            "score": score,

            "confidence": readiness,

            "market_bias": bias,

            "risk": risk,

            "strengths": strengths,

            "weaknesses": weaknesses,

            "summary": summary,

            "reasons": strengths

        }


ai_service = AIService()
