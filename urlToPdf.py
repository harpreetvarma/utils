import base64
import threading
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# import FileReader
import GetUrl


def svg_to_pdf_chromium():
    """Convert a svg on disk to a pdf using Selenium and Chromedriver"""
    service = Service()
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument('--kiosk-printing')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=2000x2000")
    chrome_options.add_argument('--disable-dev-shm-usage')

    webdriver_chrome = webdriver.Chrome(
        service=service, options=chrome_options)

    # for line in FileReader.listOfFileContents('C:\\Users\\Harpreet\\Downloads\\Documents\\et\\db\\format.txt'):
    #     google_url = GetUrl.getUrlLink(line)
    #     saveAsPdf(webdriver_chrome, google_url, line)

    for i in range(13,50):
        line = 'Exam AWS Certified Developer - Associate DVA-C02 topic 1 question "' + str(i) + '" discussion'
        time.sleep(10)
        google_url = GetUrl.getUrlLink(line)
        print(google_url)
        saveAsPdf(webdriver_chrome, google_url, line)

    webdriver_chrome.close()

def saveAsPdf(webdriver_chrome, google_url, file_name):
    webdriver_chrome.get(google_url)
    pdf = webdriver_chrome.execute_cdp_cmd(
        "Page.printToPDF", {
            "printBackground": True,
            "landscape": True,
            "displayHeaderFooter": False,
            "scale": 0.75,
        })
    with open(f'aws/' + file_name + '.pdf', "wb") as f:
        f.write(base64.b64decode(pdf['data']))


svg_to_pdf_chromium()
