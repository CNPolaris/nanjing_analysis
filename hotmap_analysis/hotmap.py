# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 10:55
# @FileName: hotmap.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com
import json
import quote
import requests
from urllib.request import quote
from bs4 import BeautifulSoup
import time
import random
import matplotlib.pyplot as plt
import pandas as pd
import csv


def hotmap_data():
    map_file_path = "E:\GitHub\\nanjing_analysis\data\map_point.js"
    map_file = open(map_file_path, 'w')
    with open(r"E:\GitHub\\nanjing_analysis\data\latlng.csv", 'r', encoding='utf-8', errors='ignore') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            # 忽略第一行的变量名称
            if reader.line_num == 1:
                continue
            # line是个list，取得所有需要的值
            id == line[0].strip()  # 第一列是id
            lat = line[2]  # 第三列是纬度
            lng = line[3]  # 第四列是经度
            str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(id) + '},'
            map_file.write(str_temp)  # 写入文档
    map_file.close()


class hot_map():
    def __init__(self):
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

        # 数据集位置
        self.filename = "E:\GitHub\\nanjing_analysis\data\secondhome_clean.csv"
        self.names = [
            "id", "communityName", "areaName", "total", "unitPriceValue",
            "fwhx", "szlc", "jzmj", "hxjg", "tnmj",
            "jzlx", "fwcx", "jzjg", "zxqk", "thbl",
            "pbdt", "cqnx", "gpsj", "jyqs", "scjy",
            "fwyt", "fwnx", "cqss", "dyxx", "fbbj",
        ]
        self.miss_value = ["null", "暂无数据"]
        self.file_text = pd.read_csv(self.filename, skiprows=[0], names=self.names, na_values=self.miss_value,
                                     encoding='GBK')
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

    # 根据地址通过百度地图api查询地理坐标
    def getlnglat(self, address):
        """
        获取一个中文地址的经纬度(lat:纬度值,lng:经度值)
        """
        url_base = "http://api.map.baidu.com/geocoding/v3/"
        output = "json"
        ak = "98edo3vSG3UhY6lLnN9vr3l3wZPDK1Cj"  # 浏览器端密钥
        address = quote(address)  # 为防止乱码，先用quote进行编码
        url = url_base + '?' + 'address=' + address + '&output=' + output + '&ak=' + ak
        lat = 0.0
        lng = 0.0
        # 随机生成头部,避免同样的头部访问过多触发反爬虫
        headers = {
            "User-Agent": random.choice(self.user_agent)
        }
        try:
            res = requests.get(url, timeout=500, headers=headers)
            temp = json.loads(res.text)
            if temp['status'] == 0:
                lat = temp['result']['location']['lat']
                lng = temp['result']['location']['lng']
                time.sleep(0.3)
        except Exception as e:
            print(repr(e))
            time.sleep(60)
        return lat, lng

    # 查询地址
    def get_lng_lat(self):
        # 存放id
        idint = []
        # 存放名字
        names = []
        # 存放纬度
        lats = []
        # 存放经度
        lngs = []
        # 格式头
        lat_lng_data = {"id": idint, "communityName": names, "lat": lats, "lng": lngs}
        for id, name in zip(list(self.file_text["id"]), list(self.file_text["communityName"])):
            name = str(name)
            lat, lng = self.getlnglat("南京市" + name)
            if lat != 0 and lng != 0:
                idint.append(id)
                names.append(name)
                lats.append(lat)
                lngs.append(lng)
                print(id)
        frame_test = pd.DataFrame(lat_lng_data)
        frame_test.to_csv("E:\GitHub\\nanjing_analysis\data\latlng.csv")

    # 将坐标位置转换成js格式

    # 数据整理
    def data_Integration(self):
        # 合并数据
        df_latlng = pd.read_csv("E:\GitHub\\nanjing_analysis\data\latlng.csv", skiprows=[0],
                                names=["idi", "id", "communityName", "lat", "lng"])
        del df_latlng["idi"]
        del df_latlng["communityName"]

        df_merge = pd.merge(self.file_text, df_latlng, on="id")

        # 小于200万
        xiaoyu = df_merge[df_merge["total"] < 201]
        xiaoyu2 = df_merge.loc[df_merge["total"] < 201]
        xiaoyu2 = xiaoyu2.loc[xiaoyu2["jzmj"] < 50]

        out_map = "E:\GitHub\\nanjing_analysis\data\start.txt"
        with open(out_map, "w") as file_out:
            for lng, lat in zip(list(df_merge["lng"]), list(df_merge["lat"])):
                out = str(lng) + "," + str(lat)
                file_out.write(out)
                file_out.write("\n")

    # 将坐标位置与二手房总价生成一个js文件
    def data_convert_total(self):
        # 合并数据
        df_latlng = pd.read_csv("E:\GitHub\\nanjing_analysis\data\latlng.csv", skiprows=[0],
                                names=["idi", "id", "communityName", "lat", "lng"])
        del df_latlng["idi"]
        del df_latlng["communityName"]

        df_merge = pd.merge(self.file_text, df_latlng, on="id")
        out_total = "E:\GitHub\\nanjing_analysis\hotmap_analysis\\total.js"
        """
        生成文件之后手动修改一下文件的格式，形成高德地图api的要求,和html放在一起
        var heatmapData= []
        """
        with open(out_total, "w") as file_out:
            for lng, lat, price in zip(list(df_merge["lng"]), list(df_merge["lat"]), list(df_merge["total"])):
                str_temp = '{"lng":' + str(lng) + ',"lat":' + str(lat) + ',"count":' + str(price) + '},'
                file_out.write(str_temp)
                file_out.write("\n")

    # 将坐标位置与二手房单价生成一个js文件
    def data_convert_unitPrice(self):
        # 合并数据
        df_latlng = pd.read_csv("E:\GitHub\\nanjing_analysis\data\latlng.csv", skiprows=[0],
                                names=["idi", "id", "communityName", "lat", "lng"])
        del df_latlng["idi"]
        del df_latlng["communityName"]

        df_merge = pd.merge(self.file_text, df_latlng, on="id")
        out_total = "E:\GitHub\\nanjing_analysis\hotmap_analysis\\unitlPrice.js"
        with open(out_total, "w") as file_out:
            for lng, lat, price in zip(list(df_merge["lng"]), list(df_merge["lat"]), list(df_merge["unitPriceValue"])):
                str_temp = '{"lng":' + str(lng) + ',"lat":' + str(lat) + ',"count":' + str(price) + '},'
                file_out.write(str_temp)
                file_out.write("\n")

    def data_convert_total200(self):
        # 合并数据
        df_latlng = pd.read_csv("E:\GitHub\\nanjing_analysis\data\latlng.csv", skiprows=[0],
                                names=["idi", "id", "communityName", "lat", "lng"])
        del df_latlng["idi"]
        del df_latlng["communityName"]

        df_merge = pd.merge(self.file_text, df_latlng, on="id")
        xiaoyu = df_merge[df_merge["total"] < 201]
        out_total = "E:\GitHub\\nanjing_analysis\hotmap_analysis\\total200.js"
        with open(out_total, "w") as file_out:
            for lng, lat, price in zip(list(xiaoyu["lng"]), list(xiaoyu["lat"]), list(xiaoyu["total"])):
                str_temp = '{"lng":' + str(lng) + ',"lat":' + str(lat) + ',"count":' + str(price) + '},'
                file_out.write(str_temp)
                file_out.write("\n")


if __name__ == '__main__':
    map = hot_map()
    # map.get_lng_lat()
    # map.hotmap_data()
    # map.data_Integration()
    # map.data_convert_total()
    # map.data_convert_unitPrice()
    map.data_convert_total200()
