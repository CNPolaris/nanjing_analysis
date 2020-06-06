# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 14:30
# @FileName: url_manager.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com
"""
本模块主要是对链家网站的url进行管理，目的是实现能够自动爬取数据
通过两个set()存放已经使用和尚未使用过的url地址
"""


class UrlManager():
    def __init__(self):
        self.old_urls = set()  # 在这个集合里存放已经下载过的url
        self.new_urls = set()  # 在这个集合里存放还没有下载的url

    def add_new_url(self, url):
        """向new_urls中添加一个新的url"""
        if url is None:
            """如果url是空的就直接结束跳过"""
            return
        if url not in self.old_urls and url not in self.new_urls:
            """如果url不在已经检索过的集合中，且不重复，那么就进行添加"""
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """批量添加新的urls"""
        if len(urls) == 0 or urls is None:
            """如果urls中没有数据那么就直接跳过"""
            return
        else:
            """如果url中有可使用的url,就进行循环调用add_new_url,根据实际情况进行添加"""
            for url in urls:
                self.add_new_url(url)

    def get_new_url(self):
        """从new_urls集合中取出一个url"""
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)  # 将取出的url放在old_urls中，表示已经使用过了
        return new_url

    def isEmpty_new_urls(self):
        """判断new_urls中是否还有没有使用过的url"""
        return len(self.new_urls) != 0
