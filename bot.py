import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.taobao.com")
        await page.screenshot(path="screenshot.png")
        print("Sahifa screenshot olindi!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
