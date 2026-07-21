"""
Trade Pilot AI v2
Signal Command
"""

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from services.market_engine import market_engine


async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    symbol = "BTCUSDT"
    timeframe = "1h"

    if len(context.args) >= 1:
        symbol = context.args[0].upper()

    if len(context.args) >= 2:
        timeframe = context.args[1]

    try:

        result = market_engine.analyze(
            symbol=symbol,
            timeframe=timeframe
        )

        market = result["market"]
        ai = result["ai"]
        volume = result["volume"]
        oi = result["open_interest"]
        cvd = result["cvd"]
        liquidation = result["liquidation"]

        message = (
            f"📊 <b>Trade Pilot AI v2</b>\n\n"

            f"💰 <b>{market['symbol']}</b>\n"
            f"⏰ {market['timeframe']}\n\n"

            f"💵 Price: <b>{market['price']}</b>\n\n"

            f"📈 EMA20 : {market['ema20']}\n"
            f"📈 EMA50 : {market['ema50']}\n"
            f"📈 EMA200: {market['ema200']}\n\n"

            f"⚡ RSI : {market['rsi']}\n"
            f"📊 ADX : {market['adx']}\n"
            f"📉 MACD : {market['macd']}\n"
            f"📉 Signal : {market['macd_signal']}\n"
            f"📏 ATR : {market['atr']}\n\n"

            f"📦 Volume : {volume['strength']}\n"
            f"📊 Volume Ratio : {volume['ratio']}\n\n"
        )

        if oi:
            message += (
                f"📈 Open Interest : "
                f"{oi['open_interest']:,.0f}\n"
            )

        if cvd:
            message += (
                f"📊 CVD : "
                f"{cvd['direction']}\n"
            )

        if liquidation:
            message += (
                f"⚖️ Long/Short : "
                f"{liquidation['long_short_ratio']:.2f}\n"
            )

        message += (
            f"\n⭐ <b>Trade Score :</b> "
            f"{ai['score']}/100\n"

            f"🎯 <b>Confidence :</b> "
            f"{ai['confidence']}%\n\n"

            f"<b>{ai['signal']}</b>\n\n"

            f"🧠 <b>AI Analysis:</b>\n"
        )

        for reason in ai["reasons"]:
            message += f"✅ {reason}\n"

        await update.message.reply_html(message)

    except Exception as e:

        await update.message.reply_text(
            f"❌ {e}"
        )


signal_handler = CommandHandler(
    "signal",
    signal
)
