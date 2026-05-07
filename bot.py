from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

import os

TOKEN = os.getenv("8767113824:AAEXUVp71qNvNAytocfQlaUZY8hj5E0CrP0")

# 💰 LINKS (EDIT ONLY HERE)
CPA_LINK = "https://your-cpa-link.com"
ADSTERRA_LINK = "https://your-adsterra-link.com"

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
app.run_polling()