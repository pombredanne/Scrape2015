import csv
import time
import json
import requests
from lxml import etree
from bs4 import BeautifulSoup
from utils import *
import os

def extract_author(filename):
    temp_dict = {}
    with open(filename, 'r') as fp:
        html = etree.HTML(fp.read())
    tags = html.xpath("//li[@class='entry inproceedings']/div[@class='data']")
    for tag in tags:
        author_list = []
        authors = tag.xpath(".//span[@itemprop='author']/a/span[@itemprop='name']")
        for author in authors:
            author_list.append(author)
        title = tag.xpath(".//br/span[@class='title']")[0].text()
        temp_dict['title'] = author_list
    print temp_dict


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
        conf = file[5: file.find("?")]

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
	# extract_all("dblp_result")
    extract_author('./dblp_result/2014_cvpr?-3822629069221609197')
