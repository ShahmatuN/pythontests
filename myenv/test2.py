import pytest
from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_add_product_to_cart():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://www.vseinstrumenti.ru/")
        await page.click('[data-qa="cart"]', timeout=10000)
        await page.wait_for_selector('[data-qa="checkout-total"]', timeout=10000)
        await browser.close()
