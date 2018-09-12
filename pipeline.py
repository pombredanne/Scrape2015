from utils import *
import time
import json
from dblp import *

def conversion():
	yearly_result = {}

	with open("json_result/output.json", "r") as fp:
		dic = json.loads(fp.read())
		for (name, contents) in dic.items():
			yearly_result[name] = {}
			for item in contents:
				year = parse_year(item)
				yearly_result[name][year] = item
	with open("json_result/conference_yearly.json", "w") as fp:
		fp.write(json.dumps(yearly_result))


def parse_year(year_str):
	import re
	match = re.search(r'[12][0-9]{3}', year_str)
	if match is None:
		return "-1000"

	return match.group(0)

def generate_file_name(conf, year, hash_value):

	return year + "_" + conf + "_" + hash_value
		

def scrape_all_dblp(filepath):
	driver = initial()
	with open(filepath, 'r') as fp:
		dic = json.loads(fp.read())
		for (conf, item) in dic.items(): 
			for (year, url) in item.items():
				download(driver, url, "./dblp_result/" + generate_file_name(conf, year, str(hash(url))))
				time.sleep(1)
				count += 1

if __name__ == '__main__':
	## conversion()
	conversion()
	scrape_all_dblp("json_result/conference_yearly.json")
	extract_all("dblp_result")




	