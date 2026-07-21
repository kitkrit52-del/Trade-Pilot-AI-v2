"""
Trade Pilot AI v2
Volume Service
"""

import logging

logger = logging.getLogger(__name__)


class VolumeService:

    def analyze(self, df):
        """
        Аналіз торгового об'єму
        """

        try:

            current_volume = float(df.iloc[-1]["volume"])
            avg_volume = float(df["volume"].tail(20).mean())

            ratio = current_volume / avg_volume if avg_volume else 0

            if ratio >= 2.0:
                strength = "VERY HIGH"

            elif ratio >= 1.5:
                strength = "HIGH"

            elif ratio >= 1.0:
                strength = "NORMAL"

            else:
                strength = "LOW"

            return {
                "current_volume": round(current_volume, 2),
                "average_volume": round(avg_volume, 2),
                "ratio": round(ratio, 2),
                "strength": strength
            }

        except Exception as e:

            logger.exception("Volume Service Error")

            raise Exception(f"Volume error: {e}")


volume_service = VolumeService()
