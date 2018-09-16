import json
import os
import numpy as np
import operator

def author_analysis():
    with open('./author_dict.json', 'r') as fp:
        author_dict = json.loads(fp.read())
    fp.close()
    for conf in author_dict.keys():
        author_num = []
        author_sum = {}
        # for year in author_dict[conf].keys():
        for year_n in range(2014, 2018):
            year = str(year_n)
            author_list = []
            for title in author_dict[conf][year].keys():
                for author in author_dict[conf][year][title]:
                    if author not in author_list:
                        author_list.append(author)
                    if author not in author_sum:
                        author_sum[author] = 1
                    else:
                        author_sum[author] += 1
            author_num.append(len(author_list))
            # print conf, year, len(author_list)
        author_dict['author_aver'] = np.array(author_num).mean()
        author_dict['author_sum'] = len(author_sum.keys())

        author_sum = sorted(author_sum.items(), key=operator.itemgetter(1), reverse = True)
        # print conf
        # print author_sum[0:10]

        print conf, author_dict['author_aver'], author_dict['author_sum']

def citation_analysis():
    with open('./citation_dict.json', 'r') as fp:
        citation_dict = json.loads(fp.read())
    fp.close()
    for conf in citation_dict.keys():
        for year in citation_dict[conf].keys():
            citation_list = []
            for title in citation_dict[conf][year].keys():
                citation_list.append(citation_dict[conf][year][title])
            print conf, year, np.array(citation_list).mean()


def get_paper_num():
    with open('title.json', 'r') as fp:
        title_dict = json.loads(fp.read())
    fp.close()
    for conf in title_dict.keys():
        for year in title_dict[conf].keys():
            print conf, year
            print len(title_dict[conf][year])

if __name__ == '__main__':
    # get_paper_num()
    author_analysis()