#!/usr/bin/python
# -*- coding:utf-8 -*-
# 类型 vulnfunc regmatchonce regmatchall

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


def findtarget():
    try:
        code = open(sys.argv[1]).read()
        ADC.ADCode.output.good("读取待审计代码成功。")
        return code
    except:
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
    if targetcode == False:
        print("""
        使用方法：
            1、直接在脚本后跟待审计的文件，运行脚本。
            2、将待审计的内容复制到剪贴板，运行脚本。
        """)
    if isinstance(targetcode, str):
        adclass = ADC.ADCode.ADCode(targetcode)
        for r in rules_list:
            adclass.load(r)
            adclass.check()


if __name__ == '__main__':
    main()
