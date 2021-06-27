import requests
import json
from printc import Fore, Back, Style
import printc as out
import os
from visit import visit
from urllib.parse import urljoin
#引入模块

out.setup_color()  #设置颜色
__=out.get_data()

#json处理
sites=[]  #需要读取的站点
json_sites=open('sites.json', encoding='utf-8')  #打开文件
__json=json_sites.read()  #读取数据
json_sites.close()  #关闭文件
'''详细json数据请见json.md'''

#清除已经访问
visited_sites=open('visited.json', 'w', encoding='utf-8')  #打开文件
visited_sites.write('')
visited_sites.close()  #关闭文件


#判断json是否异常
if __json=='':  #没有json可读
    out.printcf('There\'s no site to read.', __, fg=Fore.RED)
    exit()
try:  #json读取出错
    __json=json.loads(__json)
    out.printcf('站点设置在sites.json，以下是json数据：', __, fg=Fore.GREEN)
    out.printcf(__json, __)
except:
    out.printcf('It seems like there is something wrong with the sites. Please try again.', __, fg=Fore.RED)
    exit()


#开始检查数据是否完整
doing=0
while doing<len(__json):
    __now=__json[doing]  #获取当前项目

    out.printcf('Checking item '+str(doing+1), __, fg=Fore.GREEN)  #输出检查信息

    try:  #json数据是否完好
        if type(__now['url'])!=type(str()) or type(__now['start_from'])!=type(str()):  #数据类型是否完好
            out.printcf('数据出错', __, fg=Fore.RED)
            del __json[doing]
            continue
        out.printcf('链接: '+__now['url'], __)
        out.printcf('开始链接: /'+__now['start_from'], __)
    except:
        out.printcf('数据出错', __, fg=Fore.RED)
        del __json[doing]
        continue

    doing+=1

out.printcf(__json, __)

for site in __json:
    visit(urljoin(site['url'], site['start_from']), __, depth=5)
