"""
Trade Pilot AI v2
Telegram Alert Service
"""

import re
import requests
import logging

logger = logging.getLogger(__name__)

class TelegramAlertService:
    def __init__(self, bot_token: str, user_id: int):
        self.bot_token = bot_token
        self.user_id = user_id
        self.base_url = f"https://telegram.org{self.bot_token}/sendMessage"

        def is_timeframe_allowed(self, timeframe) -> bool:
        """Покращена перевірка таймфрейму."""
        try:
            # Перетворюємо на рядок та нижній регістр (на випадок, якщо прийшло число або об'єкт)
            tf = str(timeframe).lower().strip()
            
            # Якщо передано просто число 5 або 15 (без 'm')
            if tf.isdigit():
                return int(tf) >= 15

            # Якщо це хвилинний таймфрейм (наприклад, "5m", "15m")
            if 'm' in tf and 'h' not in tf and 'd' not in tf:
                minutes = int(re.findall(r'\d+', tf)[0])
                return minutes >= 15

            # Усі інші (1h, 4h, 1d) — дозволені
            return True
        except Exception as e:
            logger.error(f"Помилка визначення таймфрейму {timeframe}: {e}")
            return True # У разі невідомого формату краще пропустити сигнал, ніж загубити


    def send_personal_alert(self, data: dict):
        """Форматує та надсилає сигнал в особистий бот."""
        try:
            market = data.get("market", {})
            trend = data.get("trend", {})
            risk = data.get("risk", {})
            
            # Фільтруємо таймфрейм
            tf = market.get("timeframe", "1h")
            if not self.is_timeframe_allowed(tf):
                logger.info(f"⏳ Сигнал з таймфрейму {tf.upper()} пропущено фільтром.")
                return

            # Визначаємо емодзі для сигналу
            signal_raw = risk.get("signal", "READY LONG")
            signal_emoji = "🟢" if "LONG" in signal_raw.upper() else "🔴"

            # Формуємо компактний текст для копіювання в один тап
            formatted_text = (
                f"🚨 *НОВИЙ СИГНАЛ ({tf.upper()})*\n\n"
                f"🪙 Пара: #{market.get('symbol')}\n"
                f"📈 Сигнал: {signal_emoji} *{signal_raw}*\n\n"
                f"💵 Вхід: `{market.get('price')}`\n"
                f"🛑 Стоп: `{risk.get('stop_loss')}`\n"
                f"🎯 Тейк 1: `{risk.get('tp1')}`\n"
                f"🎯 Тейк 2: `{risk.get('tp2')}`\n\n"
                f"📊 Напрямок тренду: *{trend.get('direction', 'BULLISH')}*\n"
                f"⭐ Score: `{market.get('score')}/100`"
            )

            payload = {
                "chat_id": self.user_id,
                "text": formatted_text,
                "parse_mode": "Markdown"
            }
            
            response = requests.post(self.base_url, json=payload, timeout=10)
            if response.status_code == 200:
                logger.info("✅ Сповіщення успішно надіслано в особистий бот.")
            else:
                logger.warning(f"⚠️ Telegram API повернув помилку: {response.text}")

        except Exception as e:
            logger.error(f"❌ Помилка відправки особистого сповіщення: {e}")

# Ініціалізуємо екземпляр сервісу (замініть на власні дані)
# Токен від @BotFather та ваш ID від @userinfobot
telegram_alert_service = TelegramAlertService(
    bot_token="ТУТ_ВАШ_ТОКЕН_БОТА",
    user_id=515860664
)

