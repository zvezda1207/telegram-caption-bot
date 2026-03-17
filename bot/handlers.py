import os
import random
from datetime import datetime

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from image_service import add_caption
from config import CHANNEL_ID, CAPTIONS_PATH

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    photo = update.message.photo[-1]
    file = await photo.get_file()

    user_id = update.message.from_user.id

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M")

    filename = f"{timestamp}_{user_id}.jpg"
    path = os.path.join("images", filename)

    await file.download_to_drive(path)

    with open(CAPTIONS_PATH, "r", encoding="utf-8") as f:
        captions = f.readlines()

    if not captions:
        caption = "Нет подписи 😅"
    else:
        caption = random.choice(captions).strip()

    result_path = add_caption(path, caption)

    keyboard = [
        [InlineKeyboardButton("Поделиться", callback_data=result_path)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    with open(result_path, "rb") as photo_file:
        await update.message.reply_photo(
            photo=photo_file,
            reply_markup=reply_markup
        )

    await update.message.reply_text("Готово! 🎉")


async def share(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    path = query.data

    with open(path, "rb") as photo_file:
        await context.bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=photo_file
        )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 👋\n\n"
        "Отправь мне фото, и я сделаю из него мем 😄"
    )