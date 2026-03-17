# Telegram Caption Bot 🤖

Небольшой Telegram-бот, который принимает изображение от пользователя, добавляет случайную подпись и отправляет результат обратно.
Пользователь может поделиться изображением в канал.

---

## 🚀 Функциональность

* Принимает изображения от пользователя
* Сохраняет изображения локально
* Генерирует случайную подпись из файла `captions.txt`
* Добавляет текст на изображение (шрифт Lobster)
* Отправляет обработанное изображение обратно
* Позволяет опубликовать изображение в Telegram-канал

---

## ⚙️ Настройка

Создайте файл `.env` в корне проекта:

```
BOT_TOKEN=your_telegram_bot_token
CHANNEL_ID=-100xxxxxxxxxx
```

---

## ▶️ Запуск локально

Установите зависимости:

```
pip install -r requirements.txt
```

Запустите бота:

```
python bot/bot.py
```

---

## 🐳 Запуск через Docker

Сборка образа:

```
docker build -t caption-bot .
```

Запуск контейнера:

```
docker run --env-file .env caption-bot
```

---

## 📁 Структура проекта

```
telegram-bot/
│
├── bot/
│   ├── bot.py
│   ├── handlers.py
│   ├── image_service.py
│   └── config.py
│
├── captions.txt
├── Lobster-Regular.ttf
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

---

## 🛠 Используемые технологии

* Python
* python-telegram-bot
* Pillow
* Docker

---

## 💡 Примечания

* Бот работает через polling
* Изображения сохраняются в папку `images/`
* Имя файла формируется как:
  `YYYY-MM-DD_HH-MM_userid.jpg`

---

## 📌 Требования

* Python 3.10+
* Telegram Bot Token
* Docker (опционально)
