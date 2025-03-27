
# scraper_playwright.py
# Shohanshohning Playwright asosidagi Taobao scraper moduli

from playwright.sync_api import sync_playwright

def search_taobao(keywords, pages=1):
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        for keyword in keywords:
            print(f"[+] Qidirilmoqda: {keyword}")
            for page_number in range(1, pages + 1):
                offset = (page_number - 1) * 44
                url = f"https://s.taobao.com/search?q={keyword}&s={offset}"
                page.goto(url, timeout=60000)
                page.wait_for_timeout(6000)

                items = page.query_selector_all("div.items .item")
                print(f"[+] Sahifada topilgan mahsulotlar: {len(items)}")

                for item in items:
                    try:
                        title = item.query_selector("div.title").inner_text()
                        price = item.query_selector("div.price strong").inner_text()
                        deal = item.query_selector("div.deal-cnt").inner_text()
                        link = item.query_selector("div.title a").get_attribute("href")
                        results.append({
                            "title": title,
                            "price": price,
                            "sold": deal,
                            "link": "https:" + link if link.startswith("//") else link
                        })
                    except:
                        continue

        browser.close()
    return results
