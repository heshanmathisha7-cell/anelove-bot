import os
import telegram
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        json_update = request.get_json(force=True)
        update = telegram.Update.de_json(json_update, bot)
        
        if update.message:
            chat_id = update.message.chat.id
            text = update.message.text
            if text == "/start":
                bot.send_message(chat_id=chat_id, text="Vanakkam! Nan Vercel-il irunthu iyankuren.")
                
        return "OK", 200
    return "Telegram Bot is running smoothly on Vercel!", 200

if __name__ == "__main__":
    app.run()

