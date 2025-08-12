from playwright.sync_api import sync_playwright
from requests import head

def download_file():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("http://localhost:8000/")

        response = page.request.get("http://localhost:8000/test.py")

        with open("test.py", "wb") as f:
            f.write(response.body())

        browser.close()

download_file()
