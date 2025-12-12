import os
from playwright.sync_api import sync_playwright

def download_generic(url, instance=None):
    output_directory = os.path.join(os.path.expanduser("~"), "Downloads")
    os.makedirs(output_directory, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        page = browser.new_page()
        page.goto(url)

        with page.expect_download() as event:
            page.click("text=Download")

        download = event.value
        path = os.path.join(output_directory, download.suggested_filename)
        download.save_as(path)

        browser.close()
        return path