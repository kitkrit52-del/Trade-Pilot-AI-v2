from flask import Flask

from config import (
    HOST,
    PORT,
    APP_NAME,
    VERSION
)

app = Flask(__name__)


@app.route("/")
def home():

    return {
        "application": APP_NAME,
        "version": VERSION,
        "status": "running"
    }


@app.route("/health")
def health():

    return {
        "status": "ok"
    }


def run_health_server():

    app.run(
        host=HOST,
        port=PORT
    )
