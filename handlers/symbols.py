"""
Trade Pilot AI v2.1
Symbol Menu
"""

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)

from telegram.ext import ContextTypes


async def symbols_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        [
            InlineKeyboardButton("₿ BTC", callback_data="BTCUSDT"),
            InlineKeyboardButton("♦ ETH", callback_data="ETHUSDT"),
        ],

        [
            InlineKeyboardButton("◎ SOL", callback_data="SOLUSDT"),
            InlineKeyboardButton("✕ XRP", callback_data="XRPUSDT"),
        ],

        [
            InlineKeyboardButton("🟡 BNB", callback_data="BNBUSDT"),
            InlineKeyboardButton("🐶 DOGE", callback_data="DOGEUSDT"),
        ],

        [
            InlineKeyboardButton("🌊 SUI", callback_data="SUIUSDT"),
            InlineKeyboardButton("💎 TON", callback_data="TONUSDT"),
        ],

        [
            InlineKeyboardButton("🔗 LINK", callback_data="LINKUSDT"),
            InlineKeyboardButton("🅰️ AVAX", callback_data="AVAXUSDT"),
        ],

        [
            InlineKeyboardButton("⬅️ Назад", callback_data="main_menu"),
        ]

    ]

    await update.callback_query.edit_message_text(
        "📊 Оберіть торгову пару:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
