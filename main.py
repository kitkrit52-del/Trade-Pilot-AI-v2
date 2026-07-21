"""
Trade Pilot AI v2
Main Application
"""

import logging
import threading

from telegram.ext import (
    Application,
    CommandHandler,
)

from config import BOT_TOKEN
from web.health import run_health_server

from handlers.start import start_handler
from handlers.help import help_handler
from handlers.signal import signal


# ======================================
# Logging
# ======================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# ======================================
# Register Handlers
# ======================================

def register_handlers(app):

    app.add_handler(start_handler)
    app.add_handler(help_handler)

    app.add_handler(
        CommandHandler(
            "signal",
            signal
        )
    )

    logger.info("Handlers registered.")


# ======================================
# Main
# ======================================

def main():

    logger.info("Starting Trade Pilot AI v2")

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    register_handlers(app)

    threading.Thread(
        target=run_health_server,
        daemon=True
    ).start()

    logger.info("Health server started.")

    app.run_polling(
        drop_pending_updates=True
    )


if __name__ == "__main__":
    main()
