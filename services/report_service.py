"""
Trade Pilot AI v2.1
Report Service
"""


class ReportService:

    def build_report(self, result):

        market = result["market"]
        volume = result["volume"]
        trend = result["trend"]
        risk = result["risk"]
        ai = result["ai"]

        message = (
            f"📊 <b>Trade Pilot AI v2.1</b>\n\n"

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

        if result.get("open_interest"):

            oi = result["open_interest"]

            try:
                message += (
                    f"\n📈 Open Interest : "
                    f"{oi['open_interest']:,.0f}\n"
                )
            except Exception:
                pass

        if result.get("cvd"):

            cvd = result["cvd"]

            try:
                message += (
                    f"📊 CVD : "
                    f"{cvd['direction']}\n"
                )
            except Exception:
                pass

        if result.get("liquidation"):

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

        return message


report_service = ReportService()
