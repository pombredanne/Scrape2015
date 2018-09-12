import selenium
from selenium import webdriver
import json
import time
import re

# conf_list = ['WWW', 'INFOCOM', 'SIGCOMM', 'MOBICOM', 'NSDI', 'SIGMOD', 'KDD', 'CVPR']
conf_list = ['www', 'infocom', 'sigcomm', 'mobicom', 'nsdi', 'sigmod', 'kdd', 'cvpr']

if __name__ == '__main__':
    conf_dict = {}
    driver = webdriver.Chrome('./chromedriver')
    for conf in conf_list:
        link = 'https://dblp.org/db/conf/' + conf
        conf_dict[conf] = []
        for i in range(2014, 2018):
            conf_dict[conf].append(link + '/' + conf + str(i))
            # driver.get(link + '/' + conf + str(i))
            # time.sleep(1)
    with open('./output.json', 'w') as f:
        f.write(json.dumps(conf_dict))
    f.close()