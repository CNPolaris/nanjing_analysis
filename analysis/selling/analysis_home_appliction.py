# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 19:22
# @FileName: analysis_home_appliction.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


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

    # 南京市二手房房源建筑类型饼图
    def appliction_pie(self):
        df = self.file_text.groupby("jzlx").size()
        df.plot(kind='pie', subplots=True, figsize=(8, 8), cmap=plt.cm.rainbow, autopct="%3.1f%%", fontsize=12)
        plt.title("南京市二手房房源建筑类型", fontsize=18)
        plt.legend()
        plt.ylabel("")
        plt.savefig("..\\..\\data_picture\\南京市二手房房源建筑类型饼图.png")
        plt.show()

    # 南京市二手房房源房屋朝向饼图
    def home_forward_pie(self):
        group_forward = self.file_text["fwcx"].value_counts()[:5]
        forward_other = pd.Series({"其他": self.file_text['fwcx'].value_counts()[5:].count()})
        group_forward = group_forward.append(forward_other)
        fig = plt.figure(figsize=(12, 7))
        ax = fig.add_subplot(111)
        group_forward.plot(kind='pie', subplots=True, figsize=(8, 8), cmap=plt.cm.rainbow, autopct="%3.1f%%",
                           fontsize=12)

        # df = self.file_text.groupby("fwcx").size()
        # df.plot(kind='pie', subplots=True, figsize=(8, 8), cmap=plt.cm.rainbow, autopct="%3.1f%%", fontsize=12)
        plt.title("南京市二手房房源房屋朝向", fontsize=18)
        plt.legend()
        plt.ylabel("")
        plt.savefig("..\\..\\data_picture\\南京市二手房房源房屋朝向饼图.png")
        plt.show()

    # 南京市二手房房源房屋户型结构饼形图
    def home_structure_pie(self):
        home_structure = self.file_text["fwhx"].value_counts()[:10]
        home_structure_other = pd.Series({"其他": self.file_text['fwhx'].value_counts()[10:].count()})
        home_structure = home_structure.append(home_structure_other)
        home_structure.plot(kind='pie', subplots=True, figsize=(8, 8), cmap=plt.cm.rainbow, autopct="%3.1f%%",
                            fontsize=12)
        # structure_count.plot(kind='bar',rot=0,color=['#0000FF','#666699','#00FF00','#993366','#FF6600','#339966','#FF8080','#0066CC','#993366','#FFCC99','#99CC00'])
        plt.title("南京市二手房房源房屋户型结构", fontsize=18)
        # plt.legend()
        plt.ylabel("")
        plt.savefig("..\\..\\data_picture\\南京市二手房房源房屋户型结构饼形图.png")
        plt.show()

    # 相关图
    def correllogram(self):
        plt.figure(figsize=(12, 7))

        """ 
        sns.heatmap(self.file_text.corr(),xticklabels=self.file_text.corr().columns,yticklabels=self.file_text.corr().columns,
                    cmap='RdYlGn',center=0,annot=True)
        """
        data = pd.read_csv(self.filename, usecols=[2, 3, 4, 5, 6, 7, 8, 9], na_values=self.miss_value,
                           encoding='GBK')
        sns.heatmap(data.corr(), xticklabels=data.corr().columns,
                    yticklabels=data.corr().columns,
                    cmap='RdYlGn', center=0, annot=True)
        # print(data)
        plt.yticks(fontsize=12)
        plt.xticks(fontsize=12)
        plt.title("南京市二手房信息相关图", fontsize=18)
        plt.savefig("..\\..\\data_picture\\南京市二手房信息相关图.png")

        plt.show()


if __name__ == '__main__':
    visualization = data_visualization()
    # visualization.appliction_pie()
    # visualization.home_forward_pie()
    # visualization.home_structure_pie()
    # visualization.correllogram()
