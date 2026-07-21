"""
Trade Pilot AI v2
Position Service
"""

import logging

logger = logging.getLogger(__name__)


class PositionService:

    def calculate(
        self,
        deposit,
        risk_percent,
        entry,
        stop_loss,
        leverage=1
    ):
        """
        Position Size Calculator
        """

        try:

            max_loss = deposit * (risk_percent / 100)

            stop_distance = abs(entry - stop_loss)

            if stop_distance <= 0:
                raise ValueError("Invalid Stop Loss")

            position_size = max_loss / (stop_distance / entry)

            margin = position_size / leverage

            potential_loss = (
                stop_distance / entry
            ) * position_size

            return {

                "deposit": round(deposit, 2),

                "risk_percent": round(risk_percent, 2),

                "max_loss": round(max_loss, 2),

                "entry": round(entry, 2),

                "stop_loss": round(stop_loss, 2),

                "position_size": round(position_size, 2),

                "margin": round(margin, 2),

                "leverage": leverage,

                "potential_loss": round(
                    potential_loss,
                    2
                )

            }

        except Exception as e:

            logger.exception("Position Service Error")

            raise Exception(f"Position Service: {e}")


position_service = PositionService()
