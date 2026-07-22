"""
Trade Pilot AI v2.1
Start Command
"""

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    CommandHandler,
    ContextTypes,
)

from config import APP_NAME, VERSION


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        [
            InlineKeyboardButton("📊 Аналіз", callback_data="analysis"),
            InlineKeyboardButton("🤖 AI", callback_data="ai"),
        ],

        [
            InlineKeyboardButton("📈 Scanner", callback_data="scanner"),
            InlineKeyboardButton("⚙️ Налаштування", callback_data="settings"),
        ],

        [
            InlineKeyboardButton("❓ Допомога", callback_data="help"),
        ]

    ]

    text = (
        f"🚀 <b>{APP_NAME}</b>\n\n"
        f"Version: <b>{VERSION}</b>\n\n"
        "Ласкаво просимо до Trade Pilot AI.\n\n"
        "Оберіть потрібний розділ:"
    )

    await update.message.reply_html(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


start_handler = CommandHandler(
    "start",
    start
)
