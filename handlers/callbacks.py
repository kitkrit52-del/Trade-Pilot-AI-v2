"""
Trade Pilot AI v2.1
Menu Callbacks
"""

from telegram import Update
from telegram.ext import ContextTypes

from handlers.symbols import symbols_menu
from handlers.timeframes import timeframe_menu
from services.market_engine import market_engine


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    data = query.data

    # ==========================
    # MAIN MENU
    # ==========================

    if data == "analysis":
        await symbols_menu(update, context)
        return

    if data == "ai":
        await query.edit_message_text(
            "🤖 AI Analysis\n\n"
            "AI Engine v2.1"
        )
        return

    if data == "scanner":
        await query.edit_message_text(
            "📈 Market Scanner\n\n"
            "Скоро..."
        )
        return

    if data == "settings":
        await query.edit_message_text(
            "⚙️ Settings\n\n"
            "Скоро..."
        )
        return

    if data == "help":
        await query.edit_message_text(
            "❓ Trade Pilot AI v2.1"
        )
        return

    # ==========================
    # SYMBOL
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
        "AVAXUSDT"
    ]

    if data in symbols:
        await timeframe_menu(update, context)
        return

    # ==========================
    # ANALYZE
    # ==========================

    if "|" in data:

        symbol, timeframe = data.split("|")

        try:

            result = market_engine.analyze(
                symbol=symbol,
                timeframe=timeframe
            )

            market = result["market"]
            ai = result["ai"]

            text = (
                "🚀 <b>Trade Pilot AI v2.1</b>\n\n"

                f"💰 <b>{market['symbol']}</b>\n"
                f"⏰ {timeframe}\n\n"

                f"💵 Price: {market['price']}\n"
                f"⭐ Score: {ai['score']}/100\n"
                f"🎯 Confidence: {ai['confidence']}%\n\n"

                f"🚦 <b>{ai['signal']}</b>"
            )

            await query.edit_message_text(
                text,
                parse_mode="HTML"
            )

        except Exception as e:

            await query.edit_message_text(
                f"❌ {e}"
            )

        return

    # ==========================
    # BACK
    # ==========================

    if data == "main_menu":

        from handlers.menu import menu

        await menu(update, context)
