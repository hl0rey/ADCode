#!/usr/bin/python
# -*- coding:utf-8 -*-
# 类型 vulnfunc regmatchonce regmatchall　keywords

import os
import rules.rulesutils
import ADC.ADCode
import pyperclip
import sys

# banner
banner = """
    _         ____  _ _      ____          _      
   / \  _   _|  _ \(_) |_   / ___|___   __| | ___ 
  / _ \| | | | | | | | __| | |   / _ \ / _` |/ _ \
 / ___ \ |_| | |_| | | |_  | |__| (_) | (_| |  __/
/_/   \_\__,_|____/|_|\__|  \____\___/ \__,_|\___|
                                                  

                                                  
                                        --hl0rey
"""

# 获取绝对路径
abs_path = os.path.abspath(".")
# 载入所有的规则
rules_path = abs_path + "/rules/"
rules_list = rules.rulesutils.AllRules(rules_path).rules_list()

#读取待审计的代码
def findtarget():
    try:
        #检测是否在脚本后跟了待审计的文件名
        code = open(sys.argv[1]).read()
        ADC.ADCode.output.good("读取待审计代码成功。")
        return code
    except:
        #如果抛出异常，也就是没有跟文件名，则从剪贴板读取内容
        if pyperclip.paste() == "":
            ADC.ADCode.output.bad("剪贴板没有内容。请复制待审计的代码到剪贴板！")
            return False
        else:
            ADC.ADCode.output.good("准备对剪贴板内容进行审计。\n")
            return pyperclip.paste()


def main():
    print(banner)
    targetcode = findtarget()
    print("以下是剪贴板的内容：\n")
    print(targetcode)
    print("\n")
    #如果没有跟文件名，剪贴板也没有内容就返回Ｆａｌｓｅ，并且打印出帮助信息
    if targetcode == False:
        print("""
        使用方法：
            1、直接在脚本后跟待审计的文件，运行脚本。
            2、将待审计的内容复制到剪贴板，运行脚本。
        """)
    #开始审计代码
    if isinstance(targetcode, str):
        #创建代码审计对象
        adclass = ADC.ADCode.ADCode(targetcode)
        #遍历所有插件规则，挨个检测
        for r in rules_list:
            adclass.load(r)
            adclass.check()


if __name__ == '__main__':
    main()
