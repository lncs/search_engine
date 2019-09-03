# Author :  lncs
# Time:     2019/9/3 23:07
# File :    SearchEngineBase.py
# Software: PyCharm

"""
一个搜索引擎由搜索器、索引器、检索器和用户接口四个部分组成。
搜索器，通俗来讲就是我们常提到的爬虫（scrawler），它能在互联网上大量爬取各类网站的内容，送给索引器
索引器拿到网页和内容后，会对内容进行处理，形成索引（index），存储于内部的数据库等待检索
用户接口很好理解，是指网页和 App 前端界面，例如百度和谷歌的搜索页面。用户通过用户接口，向搜索引擎发出询问（query），询问解析后送达检索器；
检索器高效检索后，再将结果返回给用户。
"""

import re


class SearchEngineBase(object):
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented.')

    def search(self, query):
        raise Exception('search not implemented.')


def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)

