# Shohanshohning botida foydali mahsulotlarni Telegram orqali yuboruvchi modul

import telegram
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def send_to_telegram(products):
    """
    Foydali mahsulotlar roвЂyxatini Telegramga yuboradi.
    :param products: tahlildan oвЂtgan mahsulotlar roвЂyxati
    """
    bot = telegram.Bot(token=TELEGRAM_TOKEN)

    if not products:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="Foydali mahsulot topilmadi.")
        return

    for product in products[:10]:  # faqat 10 tasi yuboriladi
        message = message = f"📦 {product['title']}\n💰 Narx: ¥{product['price']}\n🔥 Sotilgan: {product['sold']}\n🔗 Link: {product['link']}"
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
