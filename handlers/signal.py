from telegram import Update
from telegram.ext import ContextTypes

from services.market_engine import market_engine


async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    symbol = "BTCUSDT"
    timeframe = "1h"

    if len(context.args) >= 1:
        symbol = context.args[0].upper()

    if len(context.args) >= 2:
        timeframe = context.args[1]

    try:

        data = market_engine.analyze(
            symbol=symbol,
            timeframe=timeframe
        )

        message = (
            f"📊 Trade Pilot AI v2\n\n"
            f"💰 {data['symbol']}\n"
            f"⏰ {data['timeframe']}\n\n"
            f"Price: {data['price']}\n"
            f"EMA20: {data['ema20']}\n"
            f"EMA50: {data['ema50']}\n"
            f"EMA200: {data['ema200']}\n"
            f"RSI: {data['rsi']}\n"
            f"MACD: {data['macd']}\n"
            f"ATR: {data['atr']}\n"
            f"ADX: {data['adx']}\n\n"
            f"⭐ Trade Score: {data['score']}/100"
        )

        await update.message.reply_text(message)

    except Exception as e:
        await update.message.reply_text(
            f"❌ {str(e)}"
        )
