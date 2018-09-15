import os
import time
import json

def generate_file_name(conf, year, hash_value):
	return year + "_" + conf + "?" + hash_value

if __name__ == "__main__":
    s = 0
    file_crawled = os.listdir('./google_result')
    filepath = 'title.json'
    with open(filepath, 'r') as fp:
        dic = json.loads(fp.read())
        count = 0
        for (conf, dicts) in dic.items():
            for (year, titles) in dicts.items():
                for title in titles:
                    count += 1
                    result = generate_file_name(conf, year, str(hash(title)))
                    if count < 300: continue
                    if count  > 800 and count < 3500: continue
                    if (result not in file_crawled) and ((result + '.html') not in file_crawled):
                        print count
                        print title
                        print result
                        s += 1
    print s