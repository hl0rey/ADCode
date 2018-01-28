#!/usr/bin/python
# -*- coding:utf-8 -*-
import re
import rules.rulesutils


class ADCode:
    def __init__(self, content):
        self.content = content

    def load(self, rule):
        self.rule = rules.rulesutils.Rule(rule).get_rule()

    def detect_type(self):
        type = self.rule.type.text
        #print(type)
        if type == "vulnfunc":
            return 1

        if type == "regmatchall":
            return 2

        if type == "keywords":
            return 3

        if type=="regmatchonce":
            return 4

        return False

    def vulnfunc(self):
        #print("vulnfunc")
        funcname = self.rule.funcname.text
        if "," in funcname:
            names = funcname.split(",")
            for n in names:
                ms = n + "\(.*\)"
                if (re.search(ms, self.content)):
                    output.good("发现脆弱函数！\n")
                    output.printrule(self.rule)
                    print("\n")
        else:
            ms = funcname + "(.*)"
            if (re.search(ms, self.content)):
                output.good("发现脆弱函数！\n")
                output.printrule(self.rule)
                print("\n")
        return


    def regmatchall(self):
        #print("reg")
        regs = self.rule.regs.stripped_strings
        for ms in regs:
            if not re.search(ms, self.content):
                return

        output.good("发现可能有问题的代码！\n")
        output.printrule(self.rule)
        print("\n")
        return

    def keywords(self):
        #print("keywords")
        key = self.rule.keywords.text
        if "," in key:
            keys=key.split(",")
            for k in keys:
                if self.content.find(k):
                    print("发现关键词："+k+"\n")
                    output.printrule(self.rule)
                    print("\n")
        else:
            if self.content.find(key):
                print("发现关键词：" + key + "\n")
                output.printrule(self.rule)
                print("\n")

        return

    def regmatchonce(self):
        regs = self.rule.regs.stripped_strings
        for ms in regs:
            if re.search(ms, self.content):
                output.good("发现可能有问题的代码！\n")
                output.printrule(self.rule)
                print("\n")

        return


    def check(self):
        #print("do check!\n")
        t = self.detect_type()
        #print(t)
        if t == 1:
            self.vulnfunc()
        if t == 2:
            self.regmatchall()
        if t == 3:
            self.keywords()
        if t==4:
            self.regmatchonce()

class output:
    def good(content):
        print("\n")
        print("[!!!] " + content)

    def bad(content):
        print("\n")
        print("[X] " + content)

    def warn(content):
        print("\n")
        print("[*] " + content)

    def printrule(content):
        print("--------")
        print("----bug_name:" + content.bug_name.text)
        print("----id:" + content.id.text)
        print("----author:" + content.author.text)
        print("----tips:" + content.tips.text)
        if not content.note_id.text=="-1":
            print("----note_id:"+content.note_id.text)
        print("--------")
