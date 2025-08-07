from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.decathlon.pl/')
    page.get_by_role("button", name="Zaakceptuj wszystko").click()
    page.get_by_role("button", name="Otwórz boczną nawigację strony").click()
    page.get_by_role("button", name="Wszystkie sporty").click()
    page.locator("#highlight-0").click()
    page.locator("#cat-30").click()
    page.click('text=Rowery górskie');
    page.click('text=Pokazuj tylko produkty dostępne w Twoim sklepie');
    page.pause();
