import os

from telegram.ext import ApplicationBuilder, MessageHandler, CallbackQueryHandler, filters

from config import TOKEN, IMAGES_DIR
from handlers import handle_photo, share

os.makedirs(IMAGES_DIR, exist_ok=True)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(CallbackQueryHandler(share))

    app.run_polling()


if __name__ == "__main__":
    main()