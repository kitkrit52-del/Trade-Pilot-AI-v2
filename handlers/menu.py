"""
Trade Pilot AI v2.1
Main Menu
"""

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)

from telegram.ext import ContextTypes


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

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

    await update.message.reply_text(

        "🚀 Trade Pilot AI v2.1\n\n"
        "Оберіть потрібний розділ.",

        reply_markup=InlineKeyboardMarkup(keyboard)

    )
