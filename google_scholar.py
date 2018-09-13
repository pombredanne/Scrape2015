from utils import *
import json
import time

def search_google_scholar(driver, title, filepath):
    driver.get("https://scholar.google.com/") 
    driver.find_element_by_id("gs_hdr_tsi").clear()
    time.sleep(2)
    driver.find_element_by_id("gs_hdr_tsi").send_keys(title)
    time.sleep(2)
    driver.find_element_by_id("gs_hdr_tsb").click()

    with open(filepath, "w") as fp:
        fp.write(driver.page_source)

def extract_google_scholar(filepath):
    with open(filepath, 'r') as fp:
        target = etree.HTML(fp.read())
    first_item = target.cssselect(".gs_ri")[0].cssselect(".gs_fl")[0].cssselect("a")[2].text
    print(first_item)
     


if __name__ == '__main__':
    filepath = "./result/test.html"
    driver = initial()
    with open("title.json", 'r') as fp:
        dic = json.loads(fp.read())
    for (conf, item) in dic.items():
        for (year, title) in item.items():
            search_google_scholar(driver, title, "google_result/")
            time.sleep(10)


