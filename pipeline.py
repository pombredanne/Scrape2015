from utils import *
import time
import json
from dblp import *
from google_scholar import search_google_scholar
def conversion(filepath):
	yearly_result = {}

	with open(filepath, "r") as fp:
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

	return year + "_" + conf + "?" + hash_value
		

def scrape_all_dblp(filepath):
	driver = initial()
	count = 0
	with open(filepath, 'r') as fp:
		dic = json.loads(fp.read())
		for (conf, item) in dic.items(): 
			for (year, url) in item.items():
				download(driver, url, "./dblp_result/" + generate_file_name(conf, year, str(hash(url))))
				time.sleep(0.5)
				count += 1
				print(count)


def scrape_all_paper(filepath):
	origin =  int(open("log", "r").read())
	driver = initial()
	try:
		with open(filepath, 'r') as fp:
			dic = json.loads(fp.read())
			count = 0
			for (conf, dicts) in dic.items():
				for (year, titles) in dicts.items():
					for title in titles:
						count += 1
						if origin >	 count:
							continue
						search_google_scholar(driver, title, os.path.join("google_result", generate_file_name(conf, year, str(hash(title)))))
						print (count)
						time.sleep(2)

	except Exception as inst:
		print (inst)
		with open("log", "w") as fp:
			fp.write(str(count))
		return 						

if __name__ == '__main__':
	# conversion()
	# conversion("output.json")
	# scrape_all_dblp("json_result/conference_yearly.json")
	# extract_all("dblp_result")
	
	scrape_all_paper("title.json")



	