# analyzer.py

def analyze_products(products):
    result = []
    for product in products:
        try:
            price = float(product["price"].replace("¥", "").strip())
            sold = int(product["sold"].replace("人付款", "").replace("+", "").strip())
            
            # Engil mezonlar: narx < 50 ¥ va sotilgan > 20 dona bo‘lsa kifoya
            if price < 50 and sold > 20:
                result.append(product)
        except:
            continue
    return result
