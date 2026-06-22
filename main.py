from bot.handlers import build_application
from utils.logger import setup_logger
from config import TELEGRAM_BOT_TOKEN
import sys

setup_logger()

def main():
    if not TELEGRAM_BOT_TOKEN:
        print("❌ Missing TELEGRAM_BOT_TOKEN")
        sys.exit(1)

    app = build_application()
    print("🚀 Vizaris is LIVE...")
    app.run_polling()

if __name__ == "__main__":
    main()
