#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
from bs4 import BeautifulSoup


class Rule:
    def __init__(self, rf):
        self.rule_file = rf

    def get_rule(self):
        with open(self.rule_file) as rf:
            return BeautifulSoup(rf.read(), features="lxml-xml")


class AllRules:
    def __init__(self, rpath):
        self.path = rpath

    def rules_list(self):
        for r, ds, fs in os.walk(self.path):
            rs = []
            for xr in fs:
                if xr.endswith(".xml"):
                    rs.append(self.path + xr)
            return rs
