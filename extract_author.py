import csv
import time
import json
import requests
from lxml import etree
from bs4 import BeautifulSoup
# from utils import *
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
            author_list.append(author.text)
        # print author_list
        title = tag.xpath(".//span[@class='title']")[0].text
        temp_dict[title] = author_list
    return temp_dict


if __name__ == '__main__':
    files = os.listdir('./dblp_result')
    author_dict = {}
    for file in files:
        year = file[0: 4]
        conf = file[5: file.find('?')]
        temp_dict = extract_author('./dblp_result/' + file)
        if conf not in author_dict:
            author_dict[conf] = {}
        author_dict[conf][year] = temp_dict
    with open('author_dict.json', 'w') as f:
        f.write(json.dumps(author_dict))
    f.close()
