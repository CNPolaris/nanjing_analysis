# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 15:26
# @FileName: html_parser.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com


from bs4 import BeautifulSoup
from log import MyLog

"""
解析html网页，获得所需要的数据，并调用输出模块，将数据输出存储
"""

class HtmlParser:
    def __init__(self):
        # 写入日志，标明是解析html
        self.log = MyLog("html_parser", "logs")


    def get_secondhandhome_data(self, html_cont, id):
        # 获取二手房页面详细数据
        if html_cont is None:
            self.log.logger.error("页面解析(detail)：传入页面为空！")
            print("页面解析(detail)：传入页面为空！")
            return

        # 二手房list
        secondhandhouse = []
        # 社区名
        communityName = "null"
        # 地区名
        areaName = "null"
        # 建筑面积
        total = "null"
        # 单位房价
        unitPriceValue = "null"
        # 存放html,utf-8格式
        bsObj = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")

        tag_com = bsObj.find("div", {"class": "communityName"}).find("a")
        if tag_com is not None:
            communityName = tag_com.get_text()
        else:
            self.log.logger.error("页面解析(detail)：找不到communityName标签！")

        tag_area = bsObj.find("div", {"class": "areaName"}).find("span", {"class": "info"}).find("a")
        if tag_area is not None:
            areaName = tag_area.get_text()
        else:
            self.log.logger.error("页面解析(detail)：找不到areaName标签！")

        tag_total = bsObj.find("span", {"class": "total"})
        if tag_total is not None:
            total = tag_total.get_text()
        else:
            self.log.logger.error("页面解析(detail)：找不到total标签！")

        tag_unit = bsObj.find("span", {"class": "unitPriceValue"})
        if tag_unit is not None:
            unitPriceValue = tag_unit.get_text()
        else:
            self.log.logger.error("页面解析(detail)：找不到total标签！")
        # 把检索到的数据 放在list中
        secondhandhouse.append(id)
        secondhandhouse.append(communityName)
        secondhandhouse.append(areaName)
        secondhandhouse.append(total)
        secondhandhouse.append(unitPriceValue)

        counta = 12
        for a_child in bsObj.find("div", {"class": "introContent"}).find("div", {"class": "base"}).find("div", {
        "class": "content"}).ul.findAll("li"):
            # print(child1)
            [s.extract() for s in a_child("span")]
            secondhandhouse.append(a_child.get_text())
            counta = counta - 1

        while counta > 0:
            secondhandhouse.append("null")
            counta = counta - 1

        countb = 8
        for b_child in bsObj.find("div", {"class": "introContent"}).find("div", {"class": "transaction"}).find("div", {
        "class": "content"}).ul.findAll("li"):
            information = b_child.span.next_sibling.next_sibling.get_text()
            secondhandhouse.append(information)
            countb = countb - 1

        while countb > 0:
            secondhandhouse.append("null")
            countb = countb - 1

        self.log.logger.info("页面解析(detail)：页面解析成功！")
        print("页面解析(detail)：页面解析成功！")
        return secondhandhouse


    def get_secondhandhome_urls(self, html_cont):
        """获取二手房页面的链接"""
        if html_cont is None:
            self.log.logger.error("页面解析(page)：pg页面为空！")
            print("页面解析(page)：pg页面为空！")
            return

        ershoufang_urls = set()
        bsObj = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")

        sellListContent = bsObj.find("ul", {"class": "sellListContent"})

        if sellListContent is not None:
            for child in sellListContent.children:
                if child["class"][0] == "clear":
                    ershoufang_urls.add(child.a["href"])
                    self.log.logger.info(child.a["href"])
                    # print(child.find("a",{"class":"img"})["href"])
        else:
            self.log.logger.error("页面解析(page)：找不到sellListContent标签！")

        self.log.logger.info("页面解析：页面解析成功！")
        print("页面解析：页面解析成功！")
        return ershoufang_urls
