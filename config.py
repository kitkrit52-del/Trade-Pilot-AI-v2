"""
Trade Pilot AI v2
Configuration
"""

import os

# ==========================
# Telegram
# ==========================

BOT_TOKEN = os.getenv("BOT_TOKEN")

# ==========================
# Server
# ==========================

HOST = "0.0.0.0"
PORT = int(os.getenv("PORT", 8080))

# ==========================
# Application
# ==========================

APP_NAME = "Trade Pilot AI"
VERSION = "2.0.0"

# ==========================
# Default Trading
# ==========================

DEFAULT_SYMBOL = "BTCUSDT"
DEFAULT_TIMEFRAME = "1h"

# ==========================
# Supported Symbols
# ==========================

SYMBOLS = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "XRPUSDT",
]

# ==========================
# Supported Timeframes
# ==========================

TIMEFRAMES = [
    "15m",
    "1h",
    "4h",
    "1d",
]

# ==========================
# Binance
# ==========================

BINANCE_DEFAULT_TYPE = "future"
