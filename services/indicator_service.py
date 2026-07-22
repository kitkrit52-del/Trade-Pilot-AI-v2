"""
Trade Pilot AI v2.2
Indicator Service
"""

import ta


class IndicatorService:

    def calculate(self, df):
        """
        Додає всі основні індикатори до DataFrame.
        """

        # EMA
        df["EMA20"] = ta.trend.ema_indicator(
            df["close"], window=20
        )

        df["EMA50"] = ta.trend.ema_indicator(
            df["close"], window=50
        )

        df["EMA200"] = ta.trend.ema_indicator(
            df["close"], window=200
        )

        # RSI
        df["RSI"] = ta.momentum.rsi(
            df["close"], window=14
        )

        # MACD
        macd = ta.trend.MACD(df["close"])

        df["MACD"] = macd.macd()
        df["MACD_SIGNAL"] = macd.macd_signal()
        df["MACD_HIST"] = macd.macd_diff()

        # ATR
        atr = ta.volatility.AverageTrueRange(
            high=df["high"],
            low=df["low"],
            close=df["close"],
            window=14
        )

        df["ATR"] = atr.average_true_range()

        # ADX
        adx = ta.trend.ADXIndicator(
            high=df["high"],
            low=df["low"],
            close=df["close"],
            window=14
        )

        df["ADX"] = adx.adx()

        # Bollinger Bands
        bb = ta.volatility.BollingerBands(
            close=df["close"],
            window=20,
            window_dev=2
        )

        df["BB_UPPER"] = bb.bollinger_hband()
        df["BB_MIDDLE"] = bb.bollinger_mavg()
        df["BB_LOWER"] = bb.bollinger_lband()


        return df


    def analyze(self, df):
        """
        Trade Pilot AI v2.2
        Генерація сигналу + пояснення
        """

        last = df.iloc[-1]

        price = float(last["close"])
        ema20 = float(last["EMA20"])
        ema50 = float(last["EMA50"])
        rsi = float(last["RSI"])
        atr = float(last["ATR"])

        # Volume
        avg_volume = df["volume"].tail(20).mean()
        current_volume = float(last["volume"])

        volume_state = (
            "HIGH 🔥"
            if current_volume > avg_volume * 1.5
            else "NORMAL"
        )


        score = 0
        reasons = []


        # Trend
        if ema20 > ema50:
            score += 25
            trend = "🟢 Bullish"
            reasons.append(
                "✅ EMA20 вище EMA50"
            )
        else:
            trend = "🔴 Bearish"
            reasons.append(
                "❌ EMA20 нижче EMA50"
            )


        # RSI
        if rsi > 55:
            score += 25
            reasons.append(
                "✅ RSI підтверджує імпульс"
            )

        elif rsi < 45:
            score += 25
            reasons.append(
                "✅ RSI підтверджує падіння"
            )


        # Volume
        if current_volume > avg_volume * 1.5:
            score += 25
            reasons.append(
                "🔥 Високий обʼєм"
            )


        # Price position
        support = float(
            df["low"].tail(20).min()
        )

        resistance = float(
            df["high"].tail(20).max()
        )


        if price > support:
            score += 25


        # Signal

        if ema20 > ema50 and rsi > 55:
            signal = "🟢 LONG"

            stop_loss = price - atr * 1.5
            tp1 = price + atr * 2
            tp2 = price + atr * 4


        elif ema20 < ema50 and rsi < 45:
            signal = "🔴 SHORT"

            stop_loss = price + atr * 1.5
            tp1 = price - atr * 2
            tp2 = price - atr * 4


        else:
            signal = "⚪ SKIP"

            stop_loss = 0
            tp1 = 0
            tp2 = 0


        risk = abs(price - stop_loss)

        reward = abs(tp1 - price)

        rr = (
            round(reward / risk, 2)
            if risk > 0
            else 0
        )


        confidence = min(score + 10, 95)


        return {

            "price": round(price, 2),
            "trend": trend,
            "rsi": round(rsi, 2),
            "atr": round(atr, 2),

            "volume": volume_state,

            "score": score,
            "confidence": confidence,

            "signal": signal,

            "support": round(support, 2),
            "resistance": round(resistance, 2),

            "stop_loss": round(stop_loss, 2),
            "tp1": round(tp1, 2),
            "tp2": round(tp2, 2),

            "rr": rr,

            "reasons": reasons
        }


indicator_service = IndicatorService()
