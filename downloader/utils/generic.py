import os
from playwright.sync_api import sync_playwright
from downloader.models import Archive

def download_generic(url, instance=Archive):
    output_directory = os.path.join(os.path.expanduser("~"), "Downloads")
    os.makedirs(output_directory, exist_ok=True)
    instance.status = instance.StatusChoice.PENDENTE
    try:
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
            instance.status = instance.StatusChoice.CONCLUIDO
            return path
    except Exception as e:
        instance.status = instance.StatusChoice.FALHA
        print("Download sem sucesso: ", e)