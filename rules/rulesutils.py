#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
from bs4 import BeautifulSoup

#解析插件的类
class Rule:
    #创建对象时传入插件的路径
    def __init__(self, rf):
        self.rule_file = rf

    #返回一个ＢｅａｕｔｉｆｕｌＳｏｕｐ对象
    def get_rule(self):
        with open(self.rule_file) as rf:
            return BeautifulSoup(rf.read(), features="lxml-xml")

#获取插件列表的类
class AllRules:
    #创建对象时传入插件的路径
    def __init__(self, rpath):
        self.path = rpath

    #遍历文件夹，取到所有以．ｘｍｌ结尾的文件，也就是取到所有插件的文件名，返回一个插件列表
    def rules_list(self):
        for r, ds, fs in os.walk(self.path):
            rs = []
            for xr in fs:
                if xr.endswith(".xml"):
                    rs.append(self.path + xr)
            return rs
