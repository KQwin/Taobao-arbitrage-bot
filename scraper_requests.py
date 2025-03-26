# scraper_requests.py
# Shohanshoh uchun yengil, Render va Termuxda 100% ishlaydigan scraper

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
        items = soup.select(".items .item")

        for item in items:
            try:
                title = item.select_one(".title").get_text(strip=True)
                price = item.select_one(".price strong").get_text(strip=True)
                link = item.select_one(".title a")["href"]
                results.append({
                    "title": title,
                    "price": price,
                    "sold": "0",  # Requests orqali ko‘rinmaydi
                    "link": "https:" + link if link.startswith("//") else link
                })
            except:
                continue

    return results
