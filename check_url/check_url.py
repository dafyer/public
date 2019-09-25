#-*- coding:utf-8 -*-

import time
import requests
import sys

url_list = []
num = 1
#读取url文件
try:
    file = open("zjfwpt_url_pro.txt")
    lines = file.readlines()
    for line in lines:
        url_list.append(line.replace("\n",""))
except IOError:
    print("Error,读取文件失败或没有找到文件！")
    sys.exit(1)
else:
    file.close()

print("=========开始检查URL============")
for url in url_list:
    try:
        req = requests.get(url,timeout=10)
        state_code = req.status_code
        print(num,"返回状态码：",state_code)
        if state_code == 200:
            print("OK,", url, "访问正常。")
        else:
            print("Error,", url, "访问异常！！！")
        num += 1
    except:
        print("异常报错：",url)
    time.sleep(1)
print("==========检查完成============")