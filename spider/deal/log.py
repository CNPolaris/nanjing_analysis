# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 14:51
# @FileName: log.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com
"""
日志记录
"""
import logging
import datetime


class MyLog():
    """程序调试日志输出"""

    def __init__(self, name, filepath):
        """初始化属性"""
        # 初始化日志器
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # 每天生成一个新的文件
        filepath = (filepath + "\\" + str(datetime.date.today()) + " log.txt")
        self.fh = logging.FileHandler(filepath)
        self.fh.setLevel(logging.DEBUG)

        # 初始化格式器
        self.formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)

    def getMyLogger(self):
        """获得自定义的日志器"""
        return self.logger
