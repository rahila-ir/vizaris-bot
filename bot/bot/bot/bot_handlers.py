from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚡ Pro - $9.99", callback_data="pro")],
        [InlineKeyboardButton("💎 Premium - $29.99", callback_data="premium")],
        [InlineKeyboardButton("🤖 Chat AI", callback_data="chat")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👑 Welcome to Vizaris Bot\nChoose your plan:",
        reply_markup=reply_markup
    )


# BUTTON HANDLER
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "pro":
        await query.edit_message_text("⚡ Pro plan selected - Payment coming soon...")
    elif query.data == "premium":
        await query.edit_message_text("💎 Premium plan selected - Payment coming soon...")
    else:
        await query.edit_message_text("🤖 AI mode activated...")


# APP
def build_application():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    return app
