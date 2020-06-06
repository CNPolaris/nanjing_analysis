# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 15:29
# @FileName: html_output.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com

from log import MyLog
import csv

"""
将采集到的数据集，进行写出
"""


class HtmlOutPut():
    def __init__(self):
        self.log = MyLog("html_output", "logs")
        # 数据集写入的位置和格式
        filename = "dataout/secondhome.csv"
        with open(filename, "w", newline="")as file:
            # 链家二手房信息表格中的数据内容
            data = ["id", "小区名称", "所在区域","成交时间", "总价", "单价",
                    "房屋户型", "所在楼层", "建筑面积", "户型结构",
                    "套内面积", "建筑类型", "房屋朝向", "建成年代",
                    "装修情况", "建筑结构", "供暖方式", "梯户比例",
                    "配备电梯", "链家编号", "交易权属", "挂牌时间",
                    "房屋用途", "房屋年限", "房权所属"]
            # 位置、格式
            writer = csv.writer(file, dialect='excel')
            writer.writerow(data)

    # 数据写入
    def write_data(self, data):
        if data is None:
            # 写入日志
            self.log.logger.error("html数据集写入: 传入的数据为空!")
            # 控制台输出
            print("html数据集写入: 传入的数据为空!")
            return
        else:
            # 传入数据不为空
            filename = "dataout/secondhome.csv"
            with open(filename, "a", newline="") as file:
                writer = csv.writer(file, dialect='excel')
                writer.writerow(data)
            # 写入日志
            self.log.logger.info("html数据集写入: 传入数据写出成功!")
            # 控制台输出
            print("html数据集写入: 传入数据写出成功!")
