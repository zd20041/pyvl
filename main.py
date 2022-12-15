"""
# 安装python的各版本
# 自动更改名称
# 自动添加环境变量
"""
import bs4
import re
import requests
import json
import os				# 导入os模块


OLPYTHOBLIST = [] # 线上可安装的python版本列表
LOPYTHONLIST = [] # 本地已安装的python版本列表

# 获取可安装python版本列表(剔除本地已经安装的版本)
def getpython():
  with open('./python_vList/list.json','r',encoding='utf8')as fp:
    json_data = json.load(fp) #读取json文件
    return json_data

# 下载python版本
def dowpython():
  ...

# 删除本地python版本
def delpython():
  ...

# 获取本地已经安装的python列表
def localpython():
  ...

if __name__ == '__main__':
  os.system('cls')
  print("""✎～～～～～～～～～～～✐\n   [1] 添加python版本\n   [2] 删除python版本\n   [3] 查看本地python列表\n   [4] 退出\n✎～～～～～～～～～～～✐""")
  cmd = input("\n( ´_ゝ`)✎  ")
  os.system('cls')
  if cmd == "1":
    pythonlist = getpython() # 线上 python list
    print('可安装Python版本列表|･ω･｀)\n')
    for i, val in enumerate(pythonlist):
      print(f"┏ (^ω^)=☞  [{i+1}] {val['name']}")
    python_name = input("\n选择版本 (      。＿ 。） ✎ ＿  ")
    # 根据python_name 查找python进行下载
  elif cmd == "2":
    ...
  elif cmd == "3":
    ...
  else:
    print("输入错误")