# Shohanshohning Taobao avtomatik tahlilchi botining Playwright asosidagi scraper moduli

from playwright.sync_api import sync_playwright

def search_taobao(keyword, pages=1):
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        for page_number in range(1, pages + 1):
            offset = (page_number - 1) * 44
            url = f"https://s.taobao.com/search?q={keyword}&s={offset}"
            print(f"[+] Ochilmoqda: {url}")
            page.goto(url, timeout=60000)
            page.wait_for_timeout(5000)  # sahifa toвЂliq yuklanishi uchun kutish

            items = page.query_selector_all("div.items .item")
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
