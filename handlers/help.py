"""
Trade Pilot AI v2
Help Command
"""

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📚 Довідка

Доступні команди:

/start
/help
/signal BTCUSDT 1h

Найближчим часом:

✅ AI Score
✅ Open Interest
✅ CVD
✅ Liquidations
✅ Multi-Timeframe Analysis
"""

    await update.message.reply_html(text)


help_handler = CommandHandler("help", help_command)
