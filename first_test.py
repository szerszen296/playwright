from math import e
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.decathlon.pl/')
    expect(page.get_by_role("button", name="Zaakceptuj wszystko")).to_be_visible()
    page.get_by_role("button", name="Zaakceptuj wszystko").click()
    expect(page.get_by_role("button", name="Otwórz boczną nawigację strony")).to_be_visible()
    page.get_by_role("button", name="Otwórz boczną nawigację strony").click()
    expect(page.get_by_role("button", name="Wszystkie sporty")).to_be_visible()
    page.get_by_role("button", name="Wszystkie sporty").click()
    expect(page.locator("#highlight-0")).to_be_visible()
    page.locator("#highlight-0").click()
    expect(page.locator("#cat-30")).to_be_visible()
    page.locator("#cat-30").click()
    expect(page.locator('text=Rowery górskie')).to_be_visible()
    page.click('text=Rowery górskie');
    page.pause();
