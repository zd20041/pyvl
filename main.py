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
from tqdm import tqdm
import zipfile

# 获取可安装python版本列表(剔除本地已经安装的版本)
def getpython():
  with open('c:\\pylv\\list.json','r',encoding='utf8')as fp:
    json_data = json.load(fp) #读取json文件
    return json_data

# 下载python版本 并安装
def dowpython(name,list):
  for i in list:
    if i['name'] == name:
      pyname = i['name'] # 名
      pydowurl = i['dow_url'] # 下载地址
      print(f'\n开始从 {pydowurl} 下载 {pyname}')
      #下载文件，并传入文件名
      download(pydowurl, f"c:\\pylv\\python_tmp\\{pyname}.zip")
      # 解压到 Python文件夹内
      zip_file(f"{tmp_path}\\{pyname}.zip", f'{python_path}\\{pyname}')
      # 复制一份python.exe 重命名为 此版本的名
      
      input('安装完成 按任意键继续...')


# 解压函数 我又抬手一套 直接复制粘贴
def zip_file(zip_path,save_path):
  file = zipfile.ZipFile(zip_path)
  file.extractall(save_path)
  # 关闭文件流
  file.close()

# 带进度条的下载函数 我抬手就是一套 直接复制粘贴 大法
def download(url: str, fname: str):
    # 用流stream的方式获取url的数据
    resp = requests.get(url, stream=True)
    # 拿到文件的长度，并把total初始化为0
    total = int(resp.headers.get('content-length', 0))
    # 打开当前目录的fname文件(名字你来传入)
    # 初始化tqdm，传入总数，文件名等数据，接着就是写入，更新等操作了
    with open(fname, 'wb') as file, tqdm(
        desc=fname,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)


# 删除本地python版本
def delpython(localpythonlist, python_index):
  python_name = localpythonlist[int(python_index) - 1]
  print(f'\n你确定要删除 {python_name} 吗?  Σ( ° △ °|||)︴')
  reok = input('\nY/N: ')
  if reok == 'Y' or reok == 'y':
    # 删除本地文件夹
    shutil.rmtree(f"{python_path}\\{python_name}")
    input('删除成功 按任意键继续...')
  elif reok == 'N' or reok == 'n':
    print('下次别在手滑了哦~')
  else:
    print('取消')

# 获取本地已经安装的python列表
def localpython():
  list = os.listdir(f'{python_path}\\')
  return list

# 初始化函数
def initpylv():
  # 建立一些文件夹
  """
  1、os.path.exists(path) 判断一个目录是否存在
  2、os.makedirs(path) 多层创建目录
  3、os.mkdir(path) 创建目录
  """
  # 写入最新版本json
  if os.path.exists(f'{python_path}') and os.path.exists(f'{tmp_path}'):
    return
  else:
    try:
      os.makedirs(f'{python_path}')
    except FileExistsError as e:
      print(e)
    try:
      os.makedirs(f'{tmp_path}')
    except FileExistsError as e:
      print(e)    
      
if __name__ == '__main__':
  # 一些变量
  # tmp_path
  # python_path
  tmp_path = 'c:\\pylv\\python_tmp' # 缓存path
  python_path = 'c:\\pylv\\python_vList' # Python安装位置
  # 一些变量
  initpylv()
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
