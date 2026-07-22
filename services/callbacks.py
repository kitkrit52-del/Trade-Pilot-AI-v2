"""
Trade Pilot AI v2.1
Callbacks
"""

from telegram import Update
from telegram.ext import (
    CallbackQueryHandler,
    ContextTypes,
)

from handlers.symbols import symbols_menu
from handlers.timeframes import timeframe_menu

from services.market_engine import market_engine
from services.report_service import report_service


async def menu_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    data = query.data

    # ==========================
    # Main Menu
    # ==========================

    if data == "analysis":
        await symbols_menu(update, context)
        return

    if data == "scanner":

        await query.edit_message_text(
            "📈 Scanner\n\n"
            "Скоро буде доступний."
        )
        return

    if data == "ai":

        await query.edit_message_text(
            "🤖 AI Engine\n\n"
            "Скоро буде доступний."
        )
        return

    if data == "settings":

        await query.edit_message_text(
            "⚙️ Налаштування\n\n"
            "Скоро буде доступно."
        )
        return

    if data == "help":

        await query.edit_message_text(
            "❓ Допомога\n\n"
            "Використовуйте меню для аналізу."
        )
        return

    # ==========================
    # Symbol
    # ==========================

    symbols = [
        "BTCUSDT",
        "ETHUSDT",
        "BNBUSDT",
        "SOLUSDT",
        "XRPUSDT",
        "DOGEUSDT",
        "TONUSDT",
        "LINKUSDT",
        "SUIUSDT",
        "AVAXUSDT",
    ]

    if data in symbols:
        await timeframe_menu(update, context)
        return

    # ==========================
    # Analysis
    # ==========================

    if "|" in data:

        symbol, timeframe = data.split("|")

        try:

            result = market_engine.analyze(
                symbol=symbol,
                timeframe=timeframe,
            )

            message = report_service.build_report(result)

            await query.edit_message_text(
                message,
                parse_mode="HTML",
            )

        except Exception as e:

            await query.edit_message_text(
                f"❌ {e}"
            )

        return


callback_handler = CallbackQueryHandler(
    menu_callback
)
