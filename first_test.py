from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.decathlon.pl/')
    
    expect(page.locator("#didomi-notice-agree-button")).to_be_visible()
    page.locator("#didomi-notice-agree-button").click()

    page.get_by_role("button", name="Otwórz boczną nawigację strony").click()
    page.get_by_role("button", name="Wszystkie sporty").click()
    page.locator("#highlight-0").click()
    page.locator("#cat-30").click()
    test = page.locator(".sublevel a span").filter(has_text="Rowery górskie")
    test.click()

    expect(page.locator("#list-sort-select")).to_be_visible()
    page.locator("#list-sort-select").click()

    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")

    page.wait_for_timeout(1500)

    expect(page.locator("a.filter-element--checkbox span").filter(has_text="Decathlon")).to_be_visible()
    page.locator("a.filter-element--checkbox span").filter(has_text="Decathlon").click()

    page.wait_for_timeout(1500)


    product_links = page.locator("a.dpb-product-link")
    rows = []

    for i in range(product_links.count()):
        link = product_links.nth(i)

        brand = link.locator("strong").inner_text().strip()
        model = link.locator("span").inner_text().strip()

        price_locator = link.locator("css=+ div.price-wrapper span.vtmn-mr-1").first
        price = price_locator.inner_text().replace('\xa0', ' ').strip()

        rows.append({
            "marka": brand,
            "model": model,
            "cena": price
        })

    print(rows)

