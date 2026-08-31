"""
Trade Pilot AI v2
Telegram Alert Service (Fixed Version)
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
        """Гнучка перевірка таймфрейму (дозволено ≥ 15m)."""
        try:
            tf = str(timeframe).lower().strip()
            if tf.isdigit():
                return int(tf) >= 15
            if 'm' in tf and 'h' not in tf and 'd' not in tf:
                minutes = int(re.findall(r'\d+', tf)[0])
                return minutes >= 15
            return True
        except Exception as e:
            logger.error(f"Помилка визначення таймфрейму {timeframe}: {e}")
            return True

    def send_personal_alert(self, data: dict):
        """Форматує та надсилає сигнал в особистий бот із захистом від відсутніх ключів."""
        try:
            market = data.get("market", {})
            trend = data.get("trend", {})
            # Оскільки ціни стопу і тейків розраховує risk_service, беремо їх з об'єкта risk
            risk = data.get("risk", {}) 
            
            tf = market.get("timeframe", "1h")
            if not self.is_timeframe_allowed(tf):
                logger.info(f"⏳ Сигнал з таймфрейму {tf.upper()} пропущено фільтром.")
                return

            # Безпечно витягуємо змінні з використанням значень за замовчуванням
            symbol = market.get("symbol", "UNKNOWN")
            price = market.get("price", "0.0")
            score = market.get("score", "0")
            
            # Витягуємо параметри ризику (якщо їх немає в risk, спробуємо взяти з market на всякий випадок)
            signal_raw = risk.get("signal", market.get("signal", "READY LONG"))
            stop_loss = risk.get("stop_loss", market.get("stop_loss", "Не визначено"))
            tp1 = risk.get("tp1", market.get("tp1", "Не визначено"))
            tp2 = risk.get("tp2", market.get("tp2", "Не визначено"))
            
            signal_emoji = "🟢" if "LONG" in str(signal_raw).upper() else "🔴"

            # Формуємо повідомлення
            formatted_text = (
                f"🚨 *НОВИЙ СИГНАЛ ({str(tf).upper()})*\n\n"
                f"🪙 Пара: #{symbol}\n"
                f"📈 Сигнал: {signal_emoji} *{signal_raw}*\n\n"
                f"💵 Вхід: `{price}`\n"
                f"🛑 Стоп: `{stop_loss}`\n"
                f"🎯 Тейк 1: `{tp1}`\n"
                f"🎯 Тейк 2: `{tp2}`\n\n"
                f"📊 Тренд: *{trend.get('direction', 'BULLISH')}*\n"
                f"⭐ Score: `{score}/100`"
            )

            self._execute_send(formatted_text)

        except Exception as e:
            error_msg = f"❌ Помилка обробки сигналу в AlertService: {e}"
            logger.error(error_msg)
            # Якщо сталася помилка парсингу, бот все одно надішле вам структуру помилки, щоб ви бачили, що зв'язок є
            self._execute_send(f"⚠️ *Помилка в коді бота:* {str(e)}")

    def _execute_send(self, text: str):
        """Пряма відправка запиту в Telegram."""
        payload = {"chat_id": self.user_id, "text": text, "parse_mode": "Markdown"}
        try:
            res = requests.post(self.base_url, json=payload, timeout=10)
            if res.status_code != 200:
                logger.warning(f"⚠️ Telegram вернув помилку: {res.text}")
        except Exception as e:
            logger.error(f"❌ Помилка запиту: {e}")

# Ініціалізація (Вкажіть ваші точні дані!)
telegram_alert_service = TelegramAlertService(
    bot_token="СЮДИ_ВАШ_ТОКЕН_З_BOTFATHER",
    user_id=515860664
)
