"""
Trade Pilot AI v2.1
Menu Callbacks
"""

from telegram import Update
from telegram.ext import ContextTypes

from handlers.symbols import symbols_menu


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    data = query.data

    # ==========================
    # Main Menu
    # ==========================

    if data == "analysis":

        await symbols_menu(update, context)

    elif data == "ai":

        await query.edit_message_text(
            "🤖 AI ANALYSIS\n\n"
            "Модуль AI знаходиться у розробці."
        )

    elif data == "scanner":

        await query.edit_message_text(
            "📈 MARKET SCANNER\n\n"
            "Сканер буде доданий у версії 2.1."
        )

    elif data == "settings":

        await query.edit_message_text(
            "⚙️ НАЛАШТУВАННЯ\n\n"
            "Налаштування будуть доступні незабаром."
        )

    elif data == "help":

        await query.edit_message_text(
            "❓ ДОПОМОГА\n\n"
            "Trade Pilot AI v2.1\n\n"
            "Використовуйте меню для аналізу ринку."
        )

    # ==========================
    # Back
    # ==========================

    elif data == "main_menu":

        from handlers.menu import menu

        await menu(update, context)

    # ==========================
    # Unknown
    # ==========================

    else:

        await query.edit_message_text(
            "⚠️ Команда поки не реалізована."
        )
