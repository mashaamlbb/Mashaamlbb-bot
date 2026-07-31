from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

import os

from flask import Flask
from threading import Thread

TOKEN = os.getenv("TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📥 TikTok Video", "🎵 TikTok MP3"],
        ["▶️ YouTube Video", "🎧 YouTube Music"],
        ["🍎 Blox Fruits Stock"],
        ["🔔 Subscribe Stock Alert"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "🌌 Mashaamlbb assistant\n\nPilih fungsi:",
        reply_markup=reply_markup
    )


async def stock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    import requests

    try:
        url = "https://www.gamersberg.com/blox-fruits/stock"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        if response.status_code == 200
            await update.message.reply_text(
        "✅ Gamersberg berjaya diakses!\n\n"
        + response.text[:500]
    )
    
        else:
            await update.message.reply_text(
                "❌ Gagal mengambil data Gamersberg."
            )

    except Exception as e:
        await update.message.reply_text(
            "❌ Error sambungan:\n" + str(e)
        )


async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔔 Stock Alert Aktif!\n\n"
        "Anda akan menerima notifikasi bila buah rare muncul."
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(
        filters.Regex("🍎 Blox Fruits Stock"),
        stock
    )
)

app.add_handler(
    MessageHandler(
        filters.Regex("🔔 Subscribe Stock Alert"),
        subscribe
    )
)

print("Bot sedang berjalan...")
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot is running!"

def run_web():
    flask_app.run(host="0.0.0.0", port=10000)

Thread(target=run_web).start()

app.run_polling()
