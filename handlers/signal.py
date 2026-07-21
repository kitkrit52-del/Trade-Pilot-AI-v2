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
        volume = result["volume"]
        trend = result["trend"]
        risk = result["risk"]
        ai = result["ai"]

        message = (
            f"📊 <b>Trade Pilot AI v2</b>\n\n"

            f"💰 <b>{market['symbol']}</b>\n"
            f"⏰ TF: <b>{market['timeframe']}</b>\n\n"

            f"💵 <b>Price:</b> {market['price']}\n\n"

            f"📈 EMA20 : {market['ema20']}\n"
            f"📈 EMA50 : {market['ema50']}\n"
            f"📈 EMA200: {market['ema200']}\n\n"

            f"📊 RSI : {market['rsi']}\n"
            f"📊 ADX : {market['adx']}\n"
            f"📊 ATR : {market['atr']}\n"
            f"📊 MACD : {market['macd']}\n"
            f"📊 Signal : {market['macd_signal']}\n\n"

            f"📦 <b>Volume</b>\n"
            f"Strength : {volume['strength']}\n"
            f"Ratio : {volume['ratio']}\n\n"

            f"📈 <b>Trend</b>\n"
            f"Direction : {trend['trend']}\n"
            f"Strength : {trend['strength']}\n"
            f"Rating : {trend['rating']}\n"
        )

        if trend["warning"]:
            message += f"⚠️ {trend['warning']}\n"

        message += "\n"

        if result["open_interest"]:

            oi = result["open_interest"]

            try:
                message += (
                    f"📈 Open Interest : "
                    f"{oi['open_interest']:,.0f}\n"
                )
            except Exception:
                pass

        if result["cvd"]:

            cvd = result["cvd"]

            try:
                message += (
                    f"📊 CVD : "
                    f"{cvd['direction']}\n"
                )
            except Exception:
                pass

        if result["liquidation"]:

            ls = result["liquidation"]

            try:
                message += (
                    f"⚖️ Long / Short : "
                    f"{ls['long_short_ratio']:.2f}\n"
                )
            except Exception:
                pass

        message += (

            f"\n⭐ <b>Trade Score:</b> {ai['score']}/100\n"
            f"🎯 <b>Confidence:</b> {ai['confidence']}%\n"
            f"🚦 <b>Signal:</b> {ai['signal']}\n\n"

            f"💰 <b>Entry:</b> {risk['entry']}\n"
            f"🛑 <b>Stop Loss:</b> {risk['stop_loss']}\n"
            f"🎯 <b>TP1:</b> {risk['tp1']}\n"
            f"🎯 <b>TP2:</b> {risk['tp2']}\n"
            f"🎯 <b>TP3:</b> {risk['tp3']}\n"
            f"⚖️ <b>Risk / Reward:</b> {risk['risk_reward']}\n\n"

            f"🧠 <b>AI Analysis</b>\n"
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
