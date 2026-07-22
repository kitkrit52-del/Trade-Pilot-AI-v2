"""
Trade Pilot AI v2.1
Signal Command
"""

from telegram import Update
from telegram.ext import (
    ContextTypes,
    CommandHandler,
)

from services.market_engine import market_engine
from services.report_service import report_service


async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    symbol = "BTCUSDT"
    timeframe = "1h"

    if len(context.args) >= 1:
        symbol = context.args[0].upper()

    if len(context.args) >= 2:
        timeframe = context.args[1]

    try:

        result = market_engine.analyze(
            symbol=symbol,
            timeframe=timeframe
        )

        message = report_service.build_report(result)

        await update.message.reply_html(message)

    except Exception as e:

        await update.message.reply_text(
            f"❌ {e}"
        )


signal_handler = CommandHandler(
    "signal",
    signal
)
