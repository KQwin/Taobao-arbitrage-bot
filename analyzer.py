# Shohanshohning botida mahsulotlarni foydalilik asosida tahlil qiluvchi modul

def analyze_products(products, max_price=20.0, min_sold=1000):
    """
    Kiruvchi mahsulotlar roвЂyxatini narx va sotuvga qarab filtrlab beradi.
    :param products: scraper_playwright.py dan kelgan mahsulotlar roвЂyxati
    :param max_price: maksimal narx (ВҐ) вЂ” shundan yuqori boвЂlsa oвЂtkazilmaydi
    :param min_sold: minimal sotuv soni вЂ” shundan kam boвЂlsa oвЂtkazilmaydi
    :return: foydali mahsulotlar roвЂyxati
    """
    filtered = []

    for product in products:
        try:
            price = float(product['price'])
            sold_text = product['sold'].replace("дєєд»ж¬ѕ", "").replace("+", "").strip()
            sold = int(sold_text)

            if price <= max_price and sold >= min_sold:
                filtered.append(product)
        except:
            continue

    return filtered
