import os

from telegram.ext import ApplicationBuilder, MessageHandler, CallbackQueryHandler, filters, CommandHandler

from config import TOKEN, IMAGES_DIR
from handlers import handle_photo, share, start

os.makedirs(IMAGES_DIR, exist_ok=True)


async def error_handler(update, context):
    print(f"Ошибка: {context.error}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(CallbackQueryHandler(share))
    app.add_handler(CommandHandler("start", start))

    app.add_error_handler(error_handler)

    app.run_polling()


if __name__ == "__main__":
    main()