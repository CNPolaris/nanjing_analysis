# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 9:02
# @FileName: clean.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com

import re
import csv
import pandas as pd
filename = "E:\GitHub\\nanjing_analysis\\data\\deal\\secondhome.csv"
with open(filename, encoding='GBK') as f:
    reader = csv.reader(f)
    context = [line for line in reader]

with open("E:\GitHub\\nanjing_analysis\\data\\deal\\secondhome_clean.csv", "w", encoding='GBK', newline="") as f:
    writer = csv.writer(f)
    for line in context:
        line = [x.strip() for x in line]  # 去除每个数据项的空白符和换行符
        if line[0] == "id":
            writer.writerow(line)
            continue
        line[3]=line[3].split()[0]

        writer.writerow(line)