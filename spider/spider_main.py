# -*- coding: utf-8 -*-
# @Time    : 2020/5/29 9:23
# @FileName: spider_main.py.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com


from url_manager import UrlManager
from log import MyLog
from url_downloader import UrlDownloader
from html_output import HtmlOutPut
from html_parser import HtmlParser
import time
import random
"""
爬虫程序的主模块

"""
class spider_main():
    def __init__(self):
        self.urls=UrlManager()
        self.parser=HtmlParser()
        self.downloader=UrlDownloader()
        self.log=MyLog("spider","logs")
        self.output=HtmlOutPut()

    # 主模块中开始爬虫
    def Crawling(self,root_url):
        # 用字典存放地区名和网页数
        areas={
            "gulou":100,"jianye":100,"qinhuai":100,"xuanwu":100,"yuhuatai":100,"qixia":100,
            "baijiahu":91,"jiangningqita11":19,"chalukou1":71,"dongshanzhen":98,"jiangningdaxuecheng":74,
            "jiulonghu":49,"jiangjundadao11":51,"kexueyuan":28,"pukou":100,"liuhe":100,"lishui":100,"gaochun11":2,
            "jiangning":100,"qilinzhen":100,"tangshanzhen":19,"fenghuangxijie1":40,"xianlin":72,"yaohuamen":32,"maigaoqiao1":50,
            "maqun1":44,"qixiaqita1":19,"qixiaqita1":19,"xiaozhuang":18,"yanziji":8,"yueyuan":18,"wanshou1":15,"hongshan1":25,
            "caochangmendajie":10,"dinghuaimendajie":17,"fujianlu":12,"hanzhongmendajie":10,"huxijie":11,"jiangdong2":3,
            "jiangxinzhou":6,"nanhu4":21,"nanyuan2":17,"shuiximen1":7,"wandaguangchang1":28,"xiaoxing":10,"yuhuaxincun":16,
            "jiangningbinjiang":16,"lukou":70,"dingshanjiedao":22,"gaoxinqu2":44,"jiangpujiedao":100,"pukouqita11":36,"qiaobei":100,
            "taishanjiedao":32,"dachang12":69,"liuheqita1":14,"longchi":26,"luhezhucheng":21,"nanmenxincheng":26,"wutangguangchang":17
        }
        # 通过拼接形成所有的url地址,将所有的url连接保存
        for area,num in areas.items():
            for n in range(1,num+1):
                # 拼接url: https://nj.lianjia.com/ershoufang/
                splice_url=root_url+area+"/pg"+str(n)+"/"
                # 将拼接url写入日志
                self.log.logger.info("url地址拼接"+splice_url)
                # 控制台打印
                print("url地址拼接"+splice_url)
                # 拼接完成后开始进行网页下载
                try:
                    html_down=self.downloader.download(splice_url)
                except Exception as e:
                    # 将错误信息写入日志
                    self.log.logger.error("html下载出现错误"+repr(e))
                    # 挂起进程
                    time.sleep(60*30)
                else:
                    # 如果下载页面不出现错误，进行网页解析
                    try:
                        secondhome_urls=self.parser.get_secondhandhome_urls(html_down)
                    except Exception as e:
                        # 将错误信息写入日志
                        self.log.logger.error("html页面解析错误"+repr(e))
                    else:
                        # 页面解析正常
                        self.urls.add_new_urls(secondhome_urls)
                        time.sleep(random.randint(0,3))
        time.sleep(60*10)
        # 具体解析html 获取需要的数据集
        id=1 # 起始
        stop=1
        while self.urls.isEmpty_new_urls():
            # 取出url
            try:
                temp_url=self.urls.get_new_url()
                # 控制台打印
                print("html页面地址"+temp_url)
                # 日志写入
                self.log.logger.info("html页面地址"+temp_url)
            except Exception as e:
                # 错误信息写入日志
                # 控制台打印
                print("html页面地址获取失败" + temp_url)
                self.log.logger.error("获取url错误"+repr(e))

            # url获取正常进行下载
            try:
                temp_data=self.downloader.download(temp_url)
            except Exception as e:
                # 控制台打印
                print("页面下载失败"+temp_url)
                # 错误写入日志
                self.log.logger.error("页面下载失败"+repr(e))
                self.urls.add_new_url(temp_url)
                time.sleep(60)
            else:    # 正常下载后 进行页面解析
                try:
                    temp_parser=self.parser.get_secondhandhome_data(temp_data,id)
                except Exception as e:
                    self.log.logger.error("html页面解析错误"+repr(e))
                    print("html页面解析错误"+repr(e))
                else:
                    # 页面解析正常 进行写出
                    try:
                        self.output.write_data(temp_parser)
                    except Exception as e:
                        self.log.logger.error("数据集写出错误"+repr(e))
                        print("数据集写出错误"+repr(e))
                    else:
                        print(id)
                        id=id+1
                        stop=stop+1
                        time.sleep(1)
                        if stop==2500:
                            stop=1;
                            time.sleep(60)

if __name__=='__main__':
    # 设定爬虫入口URL
    root_url = "https://nj.lianjia.com/ershoufang/"
    # 初始化爬虫对象
    obj_spider = spider_main()
    # 启动爬虫
    obj_spider.Crawling(root_url)