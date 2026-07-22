"""
Trade Pilot AI v2.1
Timeframe Menu
"""

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)

from telegram.ext import ContextTypes


async def timeframe_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    symbol = query.data

    keyboard = [

        [
            InlineKeyboardButton("1M", callback_data=f"{symbol}|1m"),
            InlineKeyboardButton("5M", callback_data=f"{symbol}|5m"),
            InlineKeyboardButton("15M", callback_data=f"{symbol}|15m"),
        ],

        [
            InlineKeyboardButton("30M", callback_data=f"{symbol}|30m"),
            InlineKeyboardButton("1H", callback_data=f"{symbol}|1h"),
            InlineKeyboardButton("4H", callback_data=f"{symbol}|4h"),
        ],

        [
            InlineKeyboardButton("1D", callback_data=f"{symbol}|1d"),
        ],

        [
            InlineKeyboardButton("⬅️ Монети", callback_data="analysis"),
        ]

    ]

    await query.edit_message_text(
        f"📊 {symbol}\n\nОберіть таймфрейм:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
