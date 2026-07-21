"""
Trade Pilot AI v2
Liquidation Service
"""

import logging
import requests

logger = logging.getLogger(__name__)


class LiquidationService:

    BASE_URL = "https://fapi.binance.com"

    def get_long_short_ratio(self, symbol="BTCUSDT", period="5m"):
        """
        Long / Short Ratio Binance Futures
        """

        try:

            url = (
                f"{self.BASE_URL}/futures/data/"
                "globalLongShortAccountRatio"
            )

            response = requests.get(
                url,
                params={
                    "symbol": symbol,
                    "period": period,
                    "limit": 1
                },
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

            if not data:
                return None

            last = data[-1]

            return {
                "long_short_ratio": float(last["longShortRatio"]),
                "long_account": float(last["longAccount"]),
                "short_account": float(last["shortAccount"])
            }

        except Exception as e:

            logger.exception("Liquidation Service Error")

            return None


liquidation_service = LiquidationService()
