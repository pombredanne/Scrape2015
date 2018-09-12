from selenium import webdriver
import time

if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://scholar.google.com/")
    title = 'TrackMeOrNot: Enabling Flexible Control on Web Tracking'
    driver.find_element_by_id("gs_hdr_tsi").clear()
    driver.find_element_by_id("gs_hdr_tsi").send_keys(title)
    driver.find_element_by_id("gs_hdr_tsb").click()
    cite = driver.find_element_by_xpath("//div[@class='gs_ri']/div[@class='gs_fl']/a[3]").get_attribute('href')
    driver.get(cite)
    results = driver.find_elements_by_xpath("//div[@class='gs_r gs_or gs_scl']/div[@class='gs_ri']/div[@class='gs_a']")
    for result in results:
        print result.text