import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

CAPTIONS_PATH = os.path.join(BASE_DIR, "captions.txt")
FONT_PATH = os.path.join(BASE_DIR, "Lobster-Regular.ttf")
IMAGES_DIR = os.path.join(BASE_DIR, "images")