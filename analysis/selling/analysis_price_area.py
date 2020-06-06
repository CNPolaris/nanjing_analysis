# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 10:04
# @FileName: analysis_price_area.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
该模块统一进行数据可视化分析
"""


# 使用一个类统一管理
class data_visualization():
    # 构造函数
    def __init__(self):
        # 数据集位置
        self.filename = "/data/secondhome_clean.csv"
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

    # 生成总房价与建筑面积散点图
    def scatter_plot(self):
        fig = plt.figure(figsize=(12, 7))
        ax = fig.add_subplot(111)
        ax.set_title("南京二手房房价与建筑面积", fontsize=18)
        self.file_text.plot(x="jzmj", y="total", kind="scatter", grid=True, fontsize=12, ax=ax, alpha=0.4,
                            xticks=[0, 50, 100, 150, 200, 250, 300, 400, 500, 600, 700], xlim=[0, 800])
        ax.set_xlabel("建筑面积(㎡)", fontsize=14)
        ax.set_ylabel("总价(元)", fontsize=14)
        plt.savefig("E:\GitHub\\nanjing_analysis\\data_picture\\南京二手房房价与建筑面积散点图.png")
        plt.show()

    # 生成单位房价与居住面积散点图
    def scatter_plot2(self):
        fig = plt.figure(figsize=(12, 7))
        ax = fig.add_subplot(111)
        ax.set_title("南京二手房单位房价与居住面积", fontsize=18)
        self.file_text.plot(x="jzmj", y="unitPriceValue", kind="scatter", grid=True, fontsize=12, ax=ax, alpha=0.4,
                            xticks=[0, 50, 100, 150, 200, 250, 300, 400, 500, 600, 700], xlim=[0, 800])
        ax.set_xlabel("建筑面积(㎡)", fontsize=14)
        ax.set_ylabel("单价(元/平米)", fontsize=14)
        plt.savefig("E:\GitHub\\nanjing_analysis\\data_picture\\南京二手房单位房价与建筑面积散点图.png")
        plt.show()

    # 生成单位房价与地区箱线图
    def box_plot(self):
        box_area=self.file_text["unitPriceValue"].groupby(self.file_text["areaName"])
        flag=True
        box_data=pd.DataFrame(list(range(21000)),columns=["start"])
        for name, group in box_area:
            box_data[name] = group
        del box_data["start"]

        fig=plt.figure(figsize=(12,7))
        ax=fig.add_subplot(111)
        ax.set_ylabel("单价(元/m2)", fontsize=14)
        ax.set_title("南京各区域二手房单价箱线图", fontsize=18)
        box_data.plot(kind="box", fontsize=12, sym='r+', grid=True, ax=ax, yticks=[20000, 30000, 40000, 50000,60000,70000,80000,90000,100000])
        plt.savefig("E:\GitHub\\nanjing_analysis\\data_picture\\南京各区域二手房单价箱线图.png")
        plt.show()
    # 南京市各区二手房房源数量直方图
    def second_count(self):
        # 按照区域进行分组
        group_area = self.file_text["id"].groupby(self.file_text["areaName"])
        secondhome_count = group_area.count()

        fig = plt.figure(figsize=(12, 7))
        ax = fig.add_subplot(111)
        secondhome_count.plot(kind='bar', rot=0,color=['#0000FF','#666699','#00FF00','#993366','#FF6600','#339966','#FF8080','#0066CC','#993366','#FFCC99','#99CC00'])
        ax.set_title("南京市各区二手房房源数量", fontsize=18)
        ax.set_ylabel('房源数量(套)', fontsize=14)
        ax.set_xlabel('地区', fontsize=14)


        plt.savefig("E:\GitHub\\nanjing_analysis\\data_picture\南京市各区二手房房源数量直方图.png")

    # 南京市各区二手房房源数量折线图
    def second_count2(self):
        # 按照区域进行分组
        group_area = self.file_text["id"].groupby(self.file_text["areaName"])
        secondhome_count = group_area.count()
        fig = plt.figure(figsize=(12, 7))
        ax = fig.add_subplot(111)

        ax.set_title("南京市各区二手房房源数量", fontsize=18)
        ax.set_ylabel('房源数量(套)', fontsize=14)
        ax.set_xlabel('地区', fontsize=14)
        plt.plot(secondhome_count)
        plt.grid(True, linestyle='--', alpha=0.5, marker="o")

        area = ['六合', '建邺', '栖霞', '江宁', '浦口', '溧水', '玄武', '秦淮', '雨花台', '高淳', '鼓楼']
        count = secondhome_count.values
        for a, b in zip(area, count):
            plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

        plt.savefig("E:\GitHub\\nanjing_analysis\\data_picture\南京市各区二手房房源数量折线图.png")
        # print(secondhome_count.keys,secondhome_count.values)

    # 南京市各区二手房房源总面积直方图
    def second_sum_area(self):
        group_area = self.file_text["jzmj"].groupby(self.file_text["areaName"])
        secondhome_sum_area = group_area.sum()
        # print(secondhome_sum_area)
        fig = plt.figure(figsize=(12, 7))
        ax = fig.add_subplot(111)

        secondhome_sum_area.plot(kind='bar', rot=0,color=['#0000FF','#666699','#00FF00','#993366','#FF6600','#339966','#FF8080','#0066CC','#993366','#FFCC99','#99CC00'])
        ax.set_title("南京市各区二手房房源总面积", fontsize=18)
        ax.set_ylabel('房源数量(套)', fontsize=14)
        ax.set_xlabel('地区', fontsize=14, )
        plt.savefig("E:\GitHub\\nanjing_analysis\\data_picture\南南京市各区二手房房源总面积直方图.png")

    # 南京市各区二手房房源平均面积与平均房价
    def second_aver_area(self):
        group_area = self.file_text["jzmj"].groupby(self.file_text["areaName"])
        second_aver_area = group_area.mean()
        group_unitPriceValue = self.file_text["unitPriceValue"].groupby(self.file_text["areaName"])
        second_aver_value = group_unitPriceValue.mean()
        # print(second_aver_area,second_aver_value)
        fig = plt.figure()
        ax1 = fig.add_subplot(2, 1, 1)
        ax1.set_title("南京市各区二手房房源平均面积", fontsize=14)
        ax1.set_ylabel('平均面积(m2)', fontsize=10)


        ax2 = fig.add_subplot(2, 1, 2)
        ax2.set_title("南京市各区二手房房源单位平均房价", fontsize=14)
        ax2.set_ylabel('单位平均房价(元)', fontsize=10)
        plt.subplots_adjust(hspace=0.6)
        second_aver_area.plot(kind='bar', ax=ax1,fontsize=10,rot=0,color=['#0000FF','#666699','#00FF00','#993366','#FF6600','#339966','#FF8080','#0066CC','#993366','#FFCC99','#99CC00'])
        second_aver_value.plot(kind='bar',ax=ax2,fontsize=10,rot=0,color=['#0000FF','#666699','#00FF00','#993366','#FF6600','#339966','#FF8080','#0066CC','#993366','#FFCC99','#99CC00'])
        ax1.set_xlabel('地区', fontsize=10)
        ax2.set_xlabel('地区', fontsize=10)

        plt.savefig("E:\GitHub\\nanjing_analysis\\data_picture\南京市各区二手房房源平均面积与单位平均房价.png")

    # 南京市二手房房源中单价前20的房源
    def top_value_20(self):
        value_top = self.file_text.sort_values(by="unitPriceValue", ascending=False)[:20]
        value_top = value_top.sort_values(by="unitPriceValue")
        value_top.set_index(value_top["communityName"], inplace=True)

        fig = plt.figure(figsize=(12, 7))
        ax = fig.add_subplot(111)
        ax.set_ylabel("单价(元/平米)", fontsize=14)
        ax.set_title("南京二手房单价最高Top20", fontsize=18)

        value_top["unitPriceValue"].plot(kind="barh", fontsize=12)
        plt.savefig("E:\GitHub\\nanjing_analysis\\data_picture\南京市二手房房源中单价前20的房源.png")

    # 南京市房源数量前20小区
    def home_count_top(self):
        group_area=self.file_text["id"].groupby(self.file_text["communityName"])
        top_count=group_area.count().sort_values(ascending=False)[:20]

        fig=plt.figure(figsize=(12,7))
        ax=fig.add_subplot(111)
        ax.set_title("南京市房源数量前20小区",fontsize=18)
        ax.set_xlabel("房源数量(套)",fontsize=14)
        ax.set_ylabel("小区",fontsize=14)

        top_count.plot(kind="barh",fontsize=12)
        plt.savefig("E:\GitHub\\nanjing_analysis\\data_picture\南京市房源数量前20小区.png")
if __name__ == '__main__':
    visualization = data_visualization()
    # visualization.scatter_plot()
    # visualization.scatter_plot2()
    # visualization.second_count()
    # visualization.second_count2()
    # visualization.second_sum_area()
    # visualization.second_aver_area()
    # visualization.top_value_20()
    # visualization.home_count_top()
    visualization.box_plot()
