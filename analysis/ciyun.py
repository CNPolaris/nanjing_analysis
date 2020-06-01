# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 21:18
# @FileName: ciyun.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com

import csv
import jieba
from wordcloud import WordCloud

# 数据集文件位置
filename="E:\GitHub\\nanjing_analysis\data\secondhome_clean.csv"
# 生成词云图片的保存位置和格式
savePicture="E:\GitHub\\nanjing_analysis\data_picture\南京市二手房数据词云.png"
# 过滤一些无效词汇
stop_words=["null","暂无","数据","上传","照片","房本"]
# 字体格式
fontpath="simhei.ttf"
# 1.读入数据集
file_text=open(filename,encoding="GBK").read()
# 2.设置词云的背景颜色、字体、字号
cloud=WordCloud(
# 字体格式
font_path = fontpath,
# 背景色
background_color="black",
# 允许最大词汇
max_words = 2000,
# 最大号字体
max_font_size = 60
)
# 3.jieba分词 把无效字剔除
secondhome_words1 = jieba.cut(file_text)
secondhome_words2 = [word for word in secondhome_words1 if word not in stop_words]
last_text=" ".join(secondhome_words2)
# 4.开始生成词云
word_cloud=cloud.generate(last_text)
# 5.保存词云
word_cloud.to_file(savePicture)
#image=word_cloud.to_image()
#image.show()



