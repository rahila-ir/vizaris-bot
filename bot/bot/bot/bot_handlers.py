from telegram.ext import ApplicationBuilder, CommandHandler
from bot.ui import main_menu

async def start(update, context):
    await update.message.reply_text(
        "👑 Welcome to Vizaris\nChoose an option:",
        reply_markup=main_menu()
    )

def build_application():
    app = ApplicationBuilder().token("YOUR_TOKEN").build()

    app.add_handler(CommandHandler("start", start))

    return app
