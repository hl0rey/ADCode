#!/usr/bin/python
# -*- coding:utf-8 -*-
import re
import rules.rulesutils

#实现审计功能的核心类
class ADCode:
    #传入代码的内容
    def __init__(self, content):
        self.content = content

    #载入规则
    def load(self, rule):
        self.rule = rules.rulesutils.Rule(rule).get_rule()

    #判断插件的类型
    def detect_type(self):
        type = self.rule.type.text
        # print(type)
        if type == "vulnfunc":
            return 1

        if type == "regmatchall":
            return 2

        if type == "keywords":
            return 3

        if type == "regmatchonce":
            return 4

        return False

    #vulnfunc 类型的审计
    def vulnfunc(self):
        # print("vulnfunc")
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

    # regmatchall 类型的审计
    def regmatchall(self):
        # print("reg")
        regs = self.rule.regs.stripped_strings
        for ms in regs:
            if not re.search(ms, self.content):
                return

        output.good("发现可能有问题的代码！\n")
        output.printrule(self.rule)
        print("\n")
        return

    # keywords 类型的审计
    def keywords(self):
        # print("keywords")
        key = self.rule.keywords.text
        if "," in key:
            keys = key.split(",")
            for k in keys:
                if k in self.content:
                    print("发现关键词：" + k + "\n")
                    output.printrule(self.rule)
                    print("\n")
        else:
            if key in self.content:
                print("发现关键词：" + key + "\n")
                output.printrule(self.rule)
                print("\n")

        return

    # regmatchonce 类型的审计
    def regmatchonce(self):
        regs = self.rule.regs.stripped_strings
        for ms in regs:
            if re.search(ms, self.content):
                output.good("发现可能有问题的代码！\n")
                output.printrule(self.rule)
                print("\n")

        return

    #根据不同的类型，调用不同的类方法
    def check(self):
        # print("do check!\n")
        t = self.detect_type()
        # print(t)
        if t == 1:
            self.vulnfunc()
        if t == 2:
            self.regmatchall()
        if t == 3:
            self.keywords()
        if t == 4:
            self.regmatchonce()


#为了让输出好看一点而存在的类
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

    def printrule(r):
        print("--------")
        print("----bug_name:" + r.bug_name.text)
        print("----id:" + r.id.text)
        print("----author:" + r.author.text)
        print("----tips:" + r.tips.text)
        if not r.note_id.text == "-1":
            print("----note_id:" + r.note_id.text)
        print("--------")
