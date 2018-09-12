import csv
import time
import json
import requests
from lxml import etree
from bs4 import BeautifulSoup
from utils import *
import os


def extract_information(filename):
    ret = {}
    with open(filename, 'r') as fp:
        target = etree.HTML(fp.read())
    titles = target.cssselect(".title")
    def is_paper(element):
        if element is None or element.text is None:
            return False
        if element.text.find("Proceedings") == -1:
           return True
        return False

    trim_titles = map(lambda item: item.text, filter(is_paper, titles))
    # print (list(trim_titles))

    return list(trim_titles)

def extract_all(dire):
    file_list = os.listdir(dire)
    title_dic = {}

    for file in file_list:
        lis = extract_information(os.path.join(dire, file))
        year = file[0: 4]
        conf = file[4: -1]
        for title in lis:
            if title_dic.get(conf) is None:
                title_dic[conf] = {}
            if title_dic[conf].get(year) is None:
                title_dic[conf][year] = []
            title_dic[conf][year].append(title)
            # print (title_dic[conf][year])

    with open("title.json", "w") as fp:
        fp.write(json.dumps(title_dic))

if __name__ == '__main__':
	# download("https://dblp.org/db/conf/sigmod/sigmod2013", "./result/dblp.html")
	extract_all("dblp_result")

