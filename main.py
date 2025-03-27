
# main.py
# Shohanshohning Taobao Arbitrage botining markaziy boshqaruv fayli

from scraper_playwright import search_taobao
from analyzer import analyze_products
from telegram_bot import send_to_telegram

def main():
    keywords = ["衣服", "女装", "鞋", "T恤", "短裤", "裙子", "裤子", "袜子"]

    print("[+] Mahsulotlar qidirilmoqda...")
    products = search_taobao(keywords, pages=1)
    print(f"[+] Umumiy topilgan mahsulotlar soni: {len(products)}")

    print("[+] Foydali mahsulotlar tahlil qilinmoqda...")
    best = analyze_products(products)
    print(f"[+] Foydali mahsulotlar soni: {len(best)}")

    print("[+] Telegramga yuborilmoqda...")
    send_to_telegram(best)

if __name__ == "__main__":
    main()
