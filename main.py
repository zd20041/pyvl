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
import shutil


# 获取可安装python版本列表(剔除本地已经安装的版本)
def getpython():
  with open('./python_vList/list.json','r',encoding='utf8')as fp:
    json_data = json.load(fp) #读取json文件
    return json_data

# 下载python版本
def dowpython(name,list):
  for i in list:
    if i['name'] == name:
      pyname = i['name'] # 名
      pydowurl = i['dow_url'] # 下载地址
      print(f'\n开始从 {pydowurl} 下载 {pyname}')
      print('进度: ')
      # 下载
      input('安装成功 按任意键继续..')

# 删除本地python版本
def delpython(localpythonlist, python_index):
  python_name = localpythonlist[int(python_index) - 1]
  print(f'\n你确定要删除 {python_name} 吗?  Σ( ° △ °|||)︴')
  reok = input('\nY/N: ')
  if reok == 'Y' or reok == 'y':
    # 删除本地文件夹
    shutil.rmtree("X:\\pylv\\python_vList\\Python\\" + python_name)
    print('删除成功')
  elif reok == 'N' or reok == 'n':
    print('下次别在手滑了哦~')
  else:
    print('取消')

# 获取本地已经安装的python列表
def localpython():
  list = os.listdir('X:\pylv\python_vList\Python')
  return list

if __name__ == '__main__':
  while 1:
    os.system('cls')
    print("""✎～～～～～～～～～～～✐\n   [1] 添加python版本\n   [2] 查看本地python列表\n   [3] 退出\n✎～～～～～～～～～～～✐""")
    cmd = input("\n( ´_ゝ`)✎  ")
    os.system('cls')
    if cmd == "1":
      pythonlist = getpython() # 线上 python list
      print('可安装Python版本列表|･ω･｀)\n')
      for i, val in enumerate(pythonlist):
        print(f"┏ (^ω^)=☞  [{i+1}] {val['name']}")
      python_index = input("\n选择 (      。＿ 。） ✎ ＿  ")
      python_name = pythonlist[int(python_index) - 1]['name']
      # 根据python_name 查找python进行下载
      dowpython(python_name, pythonlist)
      print('bb')
    elif cmd == "2":
      # 列出本地的版本列表
      print('本地Python版本列表|･ω･｀) 删除: del <序号>\n')
      localpythonlist = localpython()
      if len(localpythonlist) == 0:
        print('┑(￣Д ￣)┍ 空的')
        input("\n按任意键继续...")
        continue
      for i, val in enumerate(localpythonlist):
        print(f"┏ (^ω^)=☞  [{i+1}] {val}")
      python_index = input("\n选择 (      。＿ 。） ✎ ＿  ")
      if python_index.startswith('del'):
        try:
          python_index = python_index.split(' ')[1]
        except:
          print('输入有误')
          break
        delpython(localpythonlist, python_index)
    elif cmd == "3":
      print('( ﾟдﾟ)つBye~')
      exit()
    else:
      print("输入错误")