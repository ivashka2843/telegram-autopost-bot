import requests
import schedule
import time
import random
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = '8171106941:AAHdIrcrWYluUpcCwzrtKt90RfgNp43e_8w'
CHANNEL_ID = 'ТЕХНОБУМ!!!'

bot = Bot(token=TOKEN)

# Пример: категории и ключевые слова для фильтрации
CATEGORIES_KEYWORDS = {
    "tech": ["смартфон", "ноутбук", "планшет", "камера", "телевизор"],
    "accessories": ["чехол", "зарядка", "наушники", "кабель", "мышь", "клавиатура"],
    "home": ["лампа", "ковер", "полотенце", "мусорное ведро", "органайзер"]
}

def parse_aliexpress():
    # Пример: простейший парсинг товаров с AliExpress (запрос с фильтрами)
    url = 'https://www.aliexpress.com/wholesale?SearchText=техника'
    # Для демонстрации — просто подставим фиксированные товары (парсить AliExpress без API сложно)
    # Лучше использовать API или готовые парсеры, это пример
    return [
        {
            'title': 'Беспроводные наушники AliExpress',
            'description': 'Качественный звук и комфорт',
            'price': '1500 ₽',
            'image_url': 'https://ae01.alicdn.com/kf/Hbca43f8f19884e6fb4e0b7f45a6a5285Y.jpg',
            'product_url': 'https://aliexpress.com/item/123456.html'
        },
    ]

def parse_wildberries():
    # Для Wildberries: можно парсить с категории техника или аксессуары
    url = 'https://www.wildberries.ru/catalog/elektronika'
    # Для простоты, возвращаем статичный пример
    return [
        {
            'title': 'Умная лампа Wildberries',
            'description': 'Управление через приложение',
            'price': '1200 ₽',
            'image_url': 'https://images.wbstatic.net/c246x328/new/12345678.jpg',
            'product_url': 'https://wildberries.ru/catalog/12345678/detail.aspx'
        },
    ]

def get_products():
    products = []
    products.extend(parse_aliexpress())
    products.extend(parse_wildberries())
    return products

def post_product():
    products = get_products()
    product = random.choice(products)
    message = f"🛍️ {product['title']}\n\n{product['description']}\nЦена: {product['price']}"
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Купить 🔗", url=product['product_url'])]])
    bot.send_photo(chat_id=CHANNEL_ID, photo=product['image_url'], caption=message, reply_markup=keyboard)
    print(f"Опубликован товар: {product['title']}")

# Расписание - 5 раз в день
schedule.every().day.at("03:40").do(post_product)
schedule.every().day.at("06:00").do(post_product)
schedule.every().day.at("15:00").do(post_product)
schedule.every().day.at("18:00").do(post_product)
schedule.every().day.at("21:00").do(post_product)

print("🤖 Бот с парсингом запущен и готов к публикации.")

while True:
    schedule.run_pending()
    time.sleep(60)