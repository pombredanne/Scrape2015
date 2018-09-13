import csv
import time
import json
import requests
from lxml import etree
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def initial(proxy=None):
    chrome_options = Options()
    # chrome_options.add_argument('--proxy-server=http://http-dyn.abuyun.com:9020')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver

def download(driver, url, filepath):
	driver.get(url)
	with open(filepath, "w") as fp:
		fp.write(driver.page_source)
