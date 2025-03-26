# scraper_requests.py
# Yangilangan versiya: foydali topilmasa ham, barcha mahsulotlarni chiqaradi

import requests
from bs4 import BeautifulSoup

def search_taobao(keyword, pages=1):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.taobao.com"
    }
    results = []

    for page in range(pages):
        s = page * 44
        url = f"https://s.taobao.com/search?q={keyword}&s={s}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        # Yangi strukturaga moslashish
        scripts = soup.find_all("script")
        for script in scripts:
            if 'g_page_config' in script.text:
                if 'rawData' in script.text:
                    continue  # Murakkab, JS kod, o‘tkazamiz

        items = soup.select(".item.J_MouserOnverReq")

        for item in items:
            try:
                title = item.select_one(".title").get_text(strip=True)
                price = item.select_one(".price strong").get_text(strip=True)
                link = item.select_one(".title a")["href"]
                results.append({
                    "title": title,
                    "price": price,
                    "sold": "-",
                    "link": "https:" + link if link.startswith("//") else link
                })
            except:
                continue

    return results
