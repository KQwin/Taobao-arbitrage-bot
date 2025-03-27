
# telegram_bot.py
# Shohanshoh botidan foydali mahsulotlarni Telegramga yuboruvchi modul

from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
import telegram

def send_to_telegram(products):
    if not products:
        message = "Foydali mahsulot topilmadi."
    else:
        message = "[+] Foydali mahsulotlar:\n\n"
        for p in products:
            message += (
                f"📦 {p['title']}\n"
                f"💰 Narxi: ¥{p['price']}\n"
                f"🛒 Sotilgan: {p['sold']}\n"
                f"🔗 Havola: {p['link']}\n\n"
            )

    try:
        bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        print("[+] Telegramga yuborildi.")
    except Exception as e:
        print(f"[!] Telegramga yuborishda xatolik: {e}")
