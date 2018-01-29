# ADCode
python实现的代码审计学习笔记，代码审计的辅助工具。

## requirement
pyperclip 访问剪贴板的库

bs4 处理xml的库
## 说明
安装完需要的库，git clone下来就能用了

## 插件说明
### 插件类型
#### vulnfunc 类型，使用有缺陷的函数，只要使用了该函数就有隐患。
#### regmatchall 类型，指定几个正则表达式，只有全部匹配才存在隐患。
#### regmatchonce 类型，指定几个正则表达式，只要匹配一个就有隐患。
