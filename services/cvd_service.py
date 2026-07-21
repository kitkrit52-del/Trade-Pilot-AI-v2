"""
Trade Pilot AI v2
CVD Service
"""

import logging

logger = logging.getLogger(__name__)


class CVDService:

    def calculate(self, df):
        """
        Approximate CVD using candle direction.
        """

        try:

            cvd = 0

            for _, row in df.iterrows():

                if row["close"] > row["open"]:
                    cvd += row["volume"]

                elif row["close"] < row["open"]:
                    cvd -= row["volume"]

            if cvd > 0:
                direction = "BUYERS"

            elif cvd < 0:
                direction = "SELLERS"

            else:
                direction = "NEUTRAL"

            return {
                "cvd": round(cvd, 2),
                "direction": direction
            }

        except Exception as e:

            logger.exception("CVD Error")

            raise Exception(f"CVD error: {e}")


cvd_service = CVDService()
