# Shohanshoh botining markaziy boshqaruv fayli

from scraper_playwright import search_taobao
from analyzer import analyze_products
from telegram_bot import send_to_telegram

def main():
    keyword = "LED chiroq"  # Kalit soвЂz вЂ” oвЂzgartirish mumkin
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
