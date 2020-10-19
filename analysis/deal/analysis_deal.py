# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 8:41
# @FileName: analysis_deal.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class data_visualization():
    # 构造函数
    def __init__(self):
        # 数据集位置
        self.filename = "..\\..\\data\\deal\\secondhome_clean.csv"
        self.names = [
            "id", "communityName", "areaName", "time", "total", "unitPriceValue",
            "fwhx", "szlc", "jzmj", "hxjg", "tnmj",
            "jzlx", "fwcx", "jcnd", "zxqk", "jzjg",
            "gnfs", "thbl", "pbdt", "ljbh", "jyqs",
            "gpsj", "fwyt", "fwnx", "fqss"
        ]
        self.miss_value = ["null", "暂无数据"]
        self.file_text = pd.read_csv(self.filename, skiprows=[0], names=self.names, na_values=self.miss_value,
                                     encoding='GBK')
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

    # 时间和平均成交价格折线图
    def scatter_plot(self):
        fig = plt.figure(figsize=(12, 7))
        ax = fig.add_subplot(111)
        ax.set_title("2020年南京市二手房成交价格走势", fontsize=18)
        data = self.file_text["total"].groupby(pd.to_datetime(self.file_text["time"]))
        data = data.mean()
        data2012 = data['2020-01-01':'2021-01-01']
        # print(data)
        plt.plot(data2012)
        plt.grid(True, linestyle='--', alpha=0.5, marker="o")
        ax.set_ylabel("总价(元)", fontsize=14)
        plt.savefig("..\\..\\data_picture\\deal\\2020年南京市二手房成交价格走势.png")
        plt.show()

    # 2012-2020年间南京市二手房平均成交价与平均单位房价
    def year_aver_total(self):
        data = self.file_text["id"].groupby(pd.to_datetime(self.file_text["time"]))
        data = data.count()['2016-01-01':'2016-12-31']
        """
        2012 296    2013     2014 547    2015 1619    2016 4078 2017 3959 2018 4442  2019 12032 2020 6013
        147         175         194           187          188      207         224     239         246
                                                                                         30438      31209
        """
        x_list = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
        count_list = [296, 742, 547, 1619, 4078, 3959, 4442, 12032, 6013]
        total_list = [147, 175, 194, 187, 188, 207, 224, 239, 246]
        unit_list = [18273, 22502, 23896, 22615, 22693, 27149, 28618, 30438, 31209]
        # print(data.sum())
        fig = plt.figure(figsize=(12, 7))
        ax1 = fig.add_subplot(2, 2, 1)
        ax1.set_title("2012-2020年间南京市二手房成交量统计", fontsize=18)
        ax1.plot(x_list, count_list, color='red')
        ax1.bar(x_list, count_list,
                color=['#0000FF', '#666699', '#00FF00', '#993366', '#FF6600', '#339966', '#FF8080', '#0066CC',
                       '#993366'])
        ax1.set_ylabel("成交量(套)", fontsize=12)
        for a, b in zip(x_list, count_list):
            ax1.text(a, b, b, ha='center', va='bottom', fontsize=10)

        plt.subplots_adjust(hspace=0.6)

        ax2 = fig.add_subplot(2, 2, 2)
        ax2.set_title("2012-2020年间南京市二手房成交平均房价统计", fontsize=18)
        ax2.plot(x_list, unit_list, color='red', label="平均房价")
        for a, b in zip(x_list, unit_list):
            ax2.text(a, b, b, ha='center', va='bottom', fontsize=10)

        ax3 = fig.add_subplot(2, 2, 3)
        ax3.set_title("2012-2020年间南京市二手房成交平均总价统计")
        ax3.bar(x_list, total_list, label="成交总价",
                color=['#0000FF', '#666699', '#00FF00', '#993366', '#FF6600', '#339966', '#FF8080', '#0066CC',
                       '#993366'])
        plt.xticks = (['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'])
        ax3.set_ylabel("金额(元)", fontsize=12)
        for a, b in zip(x_list, total_list):
            ax3.text(a, b, b, ha='center', va='bottom', fontsize=10)
        plt.savefig("..\\..\\data_picture\\deal\\2012-2020年南京市二手房成交数据分析.png")
        plt.show()


if __name__ == '__main__':
    visualization = data_visualization()
    # visualization.scatter_plot()
    visualization.year_aver_total()
