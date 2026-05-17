from flask import Flask
from threading import Thread

app_flask = Flask('')

@app_flask.route('/')
def home():
    return "Bot is alive!"

def run():
    app_flask.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

import os

TOKEN = os.getenv("BOT_TOKEN")

CPA_LINK = os.getenv("CPA_LINK")
ADSTERRA_LINK = os.getenv("ADSTERRA_LINK")

# ---------------- START COMMAND ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚡ Free Tools", callback_data="tools")],
        [InlineKeyboardButton("🤖 AI Assistant", callback_data="ai")],
        [InlineKeyboardButton("💰 Earn Money", callback_data="earn")]
    ]

    await update.message.reply_text(
        "🌍 Welcome to Global Tools Bot\n\nChoose an option:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ---------------- BUTTON HANDLER ----------------
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "tools":
        await query.message.reply_text("⚡ Tools section coming soon...")

    elif data == "ai":
        await query.message.reply_text("🤖 AI feature coming soon...")

    elif data == "earn":
        await query.message.reply_text(
            "💰 Earn Online Section\n\n"
            f"🔥 CPA Offer:\n👉 {CPA_LINK}\n\n"
            f"⚡ Adsterra Offer:\n👉 {ADSTERRA_LINK}\n\n"
            "🚀 More offers coming soon..."
        )

# ---------------- OPTIONAL COMMAND ----------------
async def earn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 Earn Section\n\n"
        f"CPA: {CPA_LINK}\n"
        f"Ads: {ADSTERRA_LINK}"
    )

# ---------------- MAIN APP ----------------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("earn", earn))
app.add_handler(CallbackQueryHandler(button_handler))

print("Bot is running...")
keep_alive()
app.run_polling()
