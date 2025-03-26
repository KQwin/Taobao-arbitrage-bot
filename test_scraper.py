
from playwright.sync_api import sync_playwright

def test_scrape_titles():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        keyword = "LED灯"
        url = f"https://s.taobao.com/search?q={keyword}"
        page.goto(url, timeout=60000)
        page.wait_for_timeout(5000)

        items = page.query_selector_all("div.items .item")
        print(f"Topilgan itemlar soni: {len(items)}")

        for i, item in enumerate(items[:10]):
            try:
                title = item.query_selector("div.title").inner_text()
                print(f"{i+1}. {title}")
            except:
                continue

        browser.close()

if __name__ == "__main__":
    test_scrape_titles()
