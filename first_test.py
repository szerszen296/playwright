from playwright.sync_api import sync_playwright, expect
import time

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

    
    page.wait_for_load_state('load')
    decathlonSeler = page.locator("css=.filter-element--checkbox").filter(has=page.locator("css=#DecathlonPartner"))
    decathlonSeler.click()
    expect(decathlonSeler.locator("css=#DecathlonPartner")).to_be_checked()
    page.wait_for_load_state('load')

    time.sleep(2)

    expect(page.locator("#list-sort-select")).to_be_visible()
    page.locator("#list-sort-select").select_option(value = '2')
    page.wait_for_load_state('load')
    
    time.sleep(2)
    

    product_links = page.locator("a.dpb-product-link")
    rows = []

    for i in range(product_links.count()):
        link = product_links.nth(i)

        brand = link.locator("strong").inner_text().strip()
        model = link.locator("span").inner_text().strip()
        price_locator = link.locator("css=+ div.price-wrapper span.vtmn-mr-1").first
        price = price_locator.inner_text().replace('\xa0', ' ').strip()

        link.click()

        try:
            weight = page.locator("h3:has-text('Waga') >> xpath=following-sibling::p").nth(0).inner_text()
            weight = " ".join(weight.split())
        except:
            weight = "N/A"

        page.go_back()
        
        rows.append({
            "marka": brand,
            "model": model,
            "cena": price,
            "waga": weight
        })

    print(rows)
    page.pause()
