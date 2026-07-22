"""
Trade Pilot AI v2.1
Menu Callbacks
"""

from telegram import Update
from telegram.ext import ContextTypes


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    data = query.data

    if data == "analysis":

        await query.edit_message_text(
            "📊 Оберіть монету.\n\n"
            "Наступним кроком ми додамо кнопки BTC, ETH, SOL..."
        )

    elif data == "ai":

        await query.edit_message_text(
            "🤖 AI Analysis\n\n"
            "Модуль знаходиться у розробці."
        )

    elif data == "scanner":

        await query.edit_message_text(
            "📈 Scanner\n\n"
            "Сканер буде доданий у v2.1."
        )

    elif data == "settings":

        await query.edit_message_text(
            "⚙️ Налаштування\n\n"
            "Незабаром."
        )

    elif data == "help":

        await query.edit_message_text(
            "❓ Допомога\n\n"
            "Trade Pilot AI v2.1"
        )
