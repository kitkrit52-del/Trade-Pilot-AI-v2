"""
Trade Pilot AI v2.1
Scanner Command
"""

from telegram import Update
from telegram.ext import (
    CommandHandler,
    ContextTypes,
)

from services.scanner_service import scanner_service


async def scanner(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🔍 Сканую ринок..."
    )

    try:

        results = scanner_service.scan()

        if not results:

            await update.message.reply_text(
                "❌ Не вдалося отримати дані."
            )
            return

        message = "📈 <b>Market Scanner</b>\n\n"

        medals = ["🥇", "🥈", "🥉"]

        for i, item in enumerate(results):

            medal = medals[i] if i < 3 else "📊"

            message += (
                f"{medal} <b>{item['symbol']}</b>\n"
                f"⭐ {item['score']}/100\n"
                f"🚦 {item['signal']}\n"
                f"🎯 Confidence: {item['confidence']}%\n\n"
            )

        await update.message.reply_html(message)

    except Exception as e:

        await update.message.reply_text(
            f"❌ {e}"
        )


scanner_handler = CommandHandler(
    "scanner",
    scanner
)
