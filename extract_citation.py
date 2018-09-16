# -*- coding:utf-8 -*-

import csv
import time
import json
import requests
from lxml import etree
from bs4 import BeautifulSoup
from utils import *
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def extract_citation(filename):
    temp_dict = {}
    with open(filename, 'r') as fp:
        page = fp.read()
        html = etree.HTML(page)
    fp.close()
    try:
        title = html.xpath("//div[@class='gs_in_txtw gs_in_txtb gs_in_acw']/input")[0].get('value')
    except:
        return ' ', -2
    try:
        citation_tag = html.xpath("//div[@class='gs_r gs_or gs_scl']/div[@class='gs_ri']/div[@class='gs_fl']")[0]
        citation = citation_tag.xpath('.//a')
        if len(citation) < 3:
            return title, -1
        else:
            text = citation[2].text
            if not text:
                return title, -1
            elif text.startswith('被引用次数'):
                return title, text.split('：')[1]
            else:
                return title, -1
    except:
        return title, -2


if __name__ == '__main__':
    files = os.listdir('./google_result')
    citation_dict = {}
    for file in files:
        year = file[0: 4]
        conf = file[5: file.find('?')]
        title, citation = extract_citation('./google_result/' + file)
        if citation == -2:
            print conf, year, title, file
        if conf not in citation_dict:
            citation_dict[conf] = {}
        if year not in citation_dict[conf]:
            citation_dict[conf][year] = {}
        citation_dict[conf][year][title] = citation
    with open('citation_dict.json', 'w') as f:
        f.write(json.dumps(citation_dict))
    f.close()
