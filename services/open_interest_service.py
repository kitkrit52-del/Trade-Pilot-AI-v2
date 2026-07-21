"""
Trade Pilot AI v2
Open Interest Service
"""

import logging
import requests

logger = logging.getLogger(__name__)


class OpenInterestService:

    BASE_URL = "https://fapi.binance.com"

    def get_open_interest(self, symbol="BTCUSDT"):
        """
        Отримання Open Interest з Binance Futures
        """

        try:

            url = f"{self.BASE_URL}/fapi/v1/openInterest"

            response = requests.get(
                url,
                params={
                    "symbol": symbol
                },
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

            return {
                "symbol": data["symbol"],
                "open_interest": float(data["openInterest"])
            }

        except Exception as e:

            logger.exception("Open Interest Error")

            raise Exception(f"Open Interest error: {e}")


open_interest_service = OpenInterestService()
