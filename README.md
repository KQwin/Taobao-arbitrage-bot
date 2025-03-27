
# Taobao Arbitrage Bot

Bu loyiha Shohanshoh tomonidan yaratilgan. Botning asosiy vazifasi:
- Taobao’dan mahsulotlarni avtomatik qidirish (Playwright orqali)
- Narx va sotuv miqdoriga qarab tahlil qilish
- Foydali deb topilgan mahsulotlarni Telegramga yuborish

## Foydalanish

### 1. GitHub’ga joylang
- Barcha fayllarni GitHub repositoryga yuklang.

### 2. Render’da loyiha oching
- `type: worker` bo‘yicha yangi Python servis oching
- `render.yaml` faylni tanlang

### 3. TOKEN va CHAT_ID
- `config.py` fayliga o‘z Telegram bot token va chat ID’ingizni yozing.

### 4. Ishga tushiring
- Render’da "Manual Deploy" bosing
- Telegramda natijani kuting

## Kalit so‘zlar

Quyidagi so‘zlar bo‘yicha mahsulotlar qidiriladi:
```
衣服, 女装, 鞋, T恤, 短裤, 裙子, 裤子, 袜子
```

## Loyiha fayllari

- `main.py`
- `scraper_playwright.py`
- `analyzer.py`
- `telegram_bot.py`
- `config.py`
- `requirements.txt`
- `render.yaml`

Barchasi Shohanshoh sifati va strategiyasi asosida yozilgan.
