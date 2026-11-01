import os
import json
import urllib.request
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is missing")


def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": text
    }

    payload = json.dumps(data).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/json"
        },
        method="POST"
    )

    with urllib.request.urlopen(req, timeout=10) as response:
        return response.read().decode("utf-8")


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return "Anelove Bot is running!", 200

    try:
        update = request.get_json(silent=True) or {}

        message = update.get("message")

        if not message:
            return "OK", 200

        chat_id = message["chat"]["id"]

        text = message.get("text", "").strip()

        if text == "/start":

            send_message(
                chat_id,
                "👋 Vanakkam!\n\n"
                "Welcome to Anelove Anime Bot!\n\n"
                "Bot is running on Vercel."
            )

        elif text == "/help":

            send_message(
                chat_id,
                "Available commands:\n\n"
                "/start - Start bot\n"
                "/help - Help"
            )

        return "OK", 200

    except Exception as e:

        print("Webhook Error:", str(e))

        return "Internal Server Error", 500
