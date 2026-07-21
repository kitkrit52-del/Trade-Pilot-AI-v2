"""
Trade Pilot AI v2
Start Command
"""

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from config import APP_NAME, VERSION


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = f"""
🚀 <b>{APP_NAME}</b>

Version: <b>{VERSION}</b>

Ласкаво просимо!

Доступні команди:

/start
/help
/signal BTCUSDT 1h

Trade Pilot AI готовий до роботи.
"""

    await update.message.reply_html(text)


start_handler = CommandHandler("start", start)
