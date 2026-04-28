import os
from PIL import Image, ImageDraw, ImageFont
from config import FONT_PATH


def add_caption(path, caption):

    image = Image.open(path)
    image = image.convert("RGB")

    draw = ImageDraw.Draw(image)

    FONT_PATH = os.path.join(os.path.dirname(__file__), "..", "Lobster-Regular.ttf")

    font = ImageFont.truetype(FONT_PATH, 60)

    width, height = image.size

    text_width, text_height = draw.textbbox((0, 0), caption, font=font)[2:]

    x = (width - text_width) // 2
    y = height - text_height - 40

    # обводка
    for dx in [-2, -1, 0, 1, 2]:
        for dy in [-2, -1, 0, 1, 2]:
            draw.text((x + dx, y + dy), caption, font=font, fill="black")

    draw.text((x, y), caption, font=font, fill="white")

    image.save(path)

    return path


