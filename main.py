# main.py

from scraper_requests import search_taobao
from analyzer import analyze_products
from telegram_bot import send_to_telegram

def main():
    keywords = ["LED灯", "手表", "耳机", "玩具", "书包"]  # Kalit so‘zlar ro‘yxati

    for keyword in keywords:
        print(f"\n[+] Kalit so‘z: {keyword}")
        print("[+] Mahsulotlar qidirilmoqda...")
        products = search_taobao(keyword, pages=1)

        print(f"[+] Topilgan mahsulotlar soni: {len(products)}")
        print("[+] Tahlil qilinmoqda...")
        best = analyze_products(products)

        print(f"[+] Foydali mahsulotlar: {len(best)}")
        print("[+] Telegramga yuborilmoqda...")
        send_to_telegram(best)

if __name__ == "__main__":
    main()
