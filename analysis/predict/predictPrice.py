# -*- coding: utf-8 -*-
# @Time    : 2020/10/19 19:22
# @FileName: predictPrice.py
# @Author  : CNPolaris

import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier

"""
小区名称	所在区域	总价 单价 房屋户型 所在楼层 建筑面积 户型结构 套内面积 建筑类型 房屋朝向 建筑结构 装修情况 梯户比例 配备电梯 产权年限 挂牌时间 交易权属	上次交易	房屋用途	房屋年限	产权所属	抵押信息	房本备件	
"""


class Predict:
    def __init__(self):
        # 载入数据
        self.filename = "../../data/selling/secondhome_clean.csv"  # 原式数据
        self.names = [
            "id", "communityName", "areaName", "total", "unitPriceValue",
            "fwhx", "szlc", "jzmj", "hxjg", "tnmj",
            "jzlx", "fwcx", "jzjg", "zxqk", "thbl",
            "pbdt", "cqnx", "gpsj", "jyqs", "scjy",
            "fwyt", "fwnx", "cqss", "dyxx", "fbbj",
        ]
        self.miss_value = ["null", "暂无数据"]
        self.file_data = pd.read_csv(self.filename, skiprows=[0], names=self.names, na_values=self.miss_value,
                                     encoding='GBK')
        # 查看数据集缺失情况
        # print(self.file_data.isnull().sum())

    # 数据清洗
    def filling(self):
        """
        填充缺失信息
        :return:
        """
        # 使用众数填充房屋户型
        self.file_data['fwhx'].fillna(self.file_data['fwhx'].mode()[0], inplace=True)
        # 使用平均数填充建筑面积
        self.file_data['jzmj'].fillna(self.file_data['jzmj'].mean(), inplace=True)
        # 使用众数填充户型结构
        self.file_data['hxjg'].fillna(self.file_data['hxjg'].mode()[0], inplace=True)
        # 使用众数填充建筑类型
        self.file_data['jzlx'].fillna(self.file_data['jzlx'].mode()[0], inplace=True)
        # 使用众数填充房屋朝向
        self.file_data['fwcx'].fillna(self.file_data['fwcx'].mode()[0], inplace=True)
        # 使用众数填充建筑结构
        self.file_data['jzjg'].fillna(self.file_data['jzjg'].mode()[0], inplace=True)
        # 使用众数填充装修情况
        self.file_data['zxqk'].fillna(self.file_data['zxqk'].mode()[0], inplace=True)
        # 使用众数填充梯户比例和配备电梯
        self.file_data['thbl'].fillna(self.file_data['thbl'].mode()[0], inplace=True)
        self.file_data['pbdt'].fillna(self.file_data['pbdt'].mode()[0], inplace=True)
        # 使用众数填充房屋用途、产权所属、抵押信息
        self.file_data['fwyt'].fillna(self.file_data['fwyt'].mode()[0], inplace=True)
        self.file_data['cqss'].fillna(self.file_data['cqss'].mode()[0], inplace=True)
        self.file_data['dyxx'].fillna(self.file_data['dyxx'].mode()[0], inplace=True)
        # print(self.file_data.isnull().sum())

        """
        保存数据
        """
        save = pd.DataFrame(self.file_data, columns=[
            "id", "communityName", "areaName", "total", "unitPriceValue",
            "fwhx", "szlc", "jzmj", "hxjg", "tnmj",
            "jzlx", "fwcx", "jzjg", "zxqk", "thbl",
            "pbdt", "cqnx", "gpsj", "jyqs", "scjy",
            "fwyt", "fwnx", "cqss", "dyxx", "fbbj",
        ])
        save.to_csv('trainData.csv')

    # 预测训练
    def perdictTrain(self):
        # 载入数据
        train_data = pd.read_csv('trainData.csv')
        # print(train_data.isnull().sum())
        """
        构建模型
        """
        # 选择特征
        features = ["fwhx", "jzmj", "hxjg",
                    "jzlx", "fwcx", "jzjg", "zxqk", "thbl",
                    "pbdt", "jyqs", "fwyt", "cqss", "dyxx"
                    ]
        train_features = train_data[features]
        train_labels = train_data['total']
        test_features = train_data[features]
        dvec = DictVectorizer(sparse=False)
        train_features = dvec.fit_transform(train_features.to_dict(orient='record'))
        # 构造 ID3 决策树
        clf = DecisionTreeClassifier(criterion='entropy')
        """
        模型训练
        """
        # 决策树训练
        clf.fit(train_features, train_labels)
        test_features = dvec.transform(test_features.to_dict(orient='record'))
        # 预测
        pred_labels = clf.predict(test_features)
        print(pred_labels)


if __name__ == '__main__':
    predict = Predict()
    # predict.filling()
    predict.perdictTrain()
