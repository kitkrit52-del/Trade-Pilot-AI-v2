"""
Trade Pilot AI v2.1
Market Scanner
"""

from services.market_engine import market_engine


class ScannerService:

    SYMBOLS = [
        "BTCUSDT",
        "ETHUSDT",
        "BNBUSDT",
        "SOLUSDT",
        "XRPUSDT",
        "DOGEUSDT",
        "TONUSDT",
        "LINKUSDT",
        "AVAXUSDT",
        "SUIUSDT",
    ]

    def scan(self, timeframe="1h"):

        results = []

        for symbol in self.SYMBOLS:

            try:

                result = market_engine.analyze(
                    symbol=symbol,
                    timeframe=timeframe
                )

                ai = result["ai"]

                results.append({
                    "symbol": symbol,
                    "score": ai["score"],
                    "signal": ai["signal"],
                    "confidence": ai["confidence"]
                })

            except Exception:
                continue

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return results


scanner_service = ScannerService()
