import os
from flask import Flask, request
import telegram

app = Flask(__name__)

# Environment variable-il irunthu BOT_TOKEN-ai eduthukollum
TOKEN = os.getenv("BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    # Telegram-ilirunthu varum update-ai peruthal
    json_update = request.get_json(force=True)
    update = telegram.Update.de_json(json_update, bot)
    
    # Ingu unga bot-in command/message logic-ai ezhutha vendum
    # Utharanathukku:
    if update.message:
        chat_id = update.message.chat.id
        text = update.message.text
        if text == "/start":
            bot.send_message(chat_id=chat_id, text="Vanakkam! Nan Vercel-il irunthu iyankuren.")
            
    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "Telegram Bot is running smoothly on Vercel!", 200

if __name__ == "__main__":
    app.run()

