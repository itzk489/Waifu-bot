import os
from threading import Thread
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌸 Waifu Hunter Bot is alive!\n\n"
        "Waifu drops coming soon..."
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Waifu Hunter Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host="0.0.0.0", port=port)

Thread(target=run_web, daemon=True).start()

print("Bot is starting...")
app.run_polling()
