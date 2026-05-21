from flask import Flask
from threading import Thread

app_flask = Flask(__name__)

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

CPA_LINKS = [
    os.getenv("CPA_LINK_1"),
    os.getenv("CPA_LINK_2"),
    os.getenv("CPA_LINK_3"),
    os.getenv("CPA_LINK_4"),
    os.getenv("CPA_LINK_5"),
]

CPA_LINKS = [link for link in CPA_LINKS if link]

ADSTERRA_LINKS = [
    os.getenv("ADSTERRA_LINK_1"),
    os.getenv("ADSTERRA_LINK_2"),
    os.getenv("ADSTERRA_LINK_3"),
    os.getenv("ADSTERRA_LINK_4"),
    os.getenv("ADSTERRA_LINK_5"),
]

ADSTERRA_LINKS = [link for link in ADSTERRA_LINKS if link]

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

    cpa_text = "\n".join(CPA_LINKS)
    adsterra_text = "\n".join(ADSTERRA_LINKS)

    await query.message.reply_text(
        f"💰 Earn Online Section\n\n"
        f"🔥 CPA Offers:\n{cpa_text}\n\n"
        f"⚡ Adsterra Offers:\n{adsterra_text}"
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
print("KEEP ALIVE STARTED")
app.run_polling()
