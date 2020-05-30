# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 14:53
# @FileName: url_downloader.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com

"""
该模块用来进行根据url地址爬取html
"""
from requests import *
from random import *
from log import MyLog


class UrlDownloader():
    def __init__(self):
        # 使用日志记录
        self.log = MyLog("url_downloader", "logs")
        # 用来伪装成浏览器的头部 防止触发网站的反爬虫机制
        self.user_agent = ["Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
                           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; 360SE) ",
                           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0) ",
                           "Mozilla/5.0 (Windows NT 5.1; zh-CN; rv:1.9.1.3) Gecko/20100101 Firefox/8.0",
                           "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
                           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
                           "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
                           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; TencentTraveler 4.0; .NET CLR 2.0.50727)",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
                           ]

    # 根据url网址下载html
    def downloader(self, url):
        if url is None:
            # 如果传入的url地址是空的,向log中写入
            self.log.logger.error("heml下载: url为空,无法下载!")
            return None
        else:  # 不为空执行下载
            # 随机生成头部,避免同样的头部访问过多触发反爬虫
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Connection": "keep-alive",
                "Cache-Control": "max-age=0",
                "Host": "nj.lianjia.com",
                "User-Agent": random.choice(self.user_agent)
            }
            spider = get(url, headers=headers)
            if spider.status_code != 200:
                # 成功连接的话是200 其他值说明连接失败 向日志写入
                self.log.logger.error("html下载: 响应错误! %d" % spider.status_code)
                return None
            else:
                # 向日志中写入信息
                self.log.logger.info("html下载: 下载成功!")
                # 在控制台中打印下载成功的信息
                print("html下载: 成功")
                # 返回获取到的html
                return spider.text
