
# analyzer.py
# Shohanshoh botidagi mahsulotlarni foydaliligi bo‘yicha tahlil moduli

def analyze_products(products):
    useful = []
    for product in products:
        try:
            price = float(product["price"])
            sold_str = product["sold"].replace("人付款", "").replace("+", "").strip()
            sold = int(sold_str) if sold_str.isdigit() else 0

            # Mezoni: narxi > 1 va sotilgan > 50 dona bo‘lsa
            if price > 1 and sold > 50:
                useful.append(product)
        except Exception:
            continue
    return useful
