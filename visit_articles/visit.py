import requests
from printc import Fore, Back, Style
import printc as out
from bs4 import BeautifulSoup as bs
from is_favourite import check_favourite, is_favourite
from links import check_links, new_link, link_exists
from urllib.parse import urlparse, urljoin  #解析链接
from visited import check_visited, new_visited, visited  #是否访问过
from forbid import forbidden

def visit(site, __, depth=100):
    try:
        response=requests.get(site, timeout=10)  #请求根链接
    except:
        out.printcf('无法访问\'{}\'。'.format(site), __, fg=Fore.RED)
        return
    status=response.status_code  #返回值
    if status!=200:  #如果请求失败
        out.printcf('Can not visit the site. Error: '+str(status), __, fg=Fore.RED)
    else:
        out.printcf('Got data from the site \'{}\'.'.format(site), __, fg=Fore.GREEN)
        if check_favourite():  #如果json文件正常
            fetch_item(site, __, 0, depth)  #开始请求
            out.printcf('\'{}\'已访问完毕。'.format(site), __, fg=Fore.GREEN)
        else:
            out.printcf('favourite.json不正确。请重新编辑文件然后重启程序。', __, fg=Fore.RED)

def fetch_item(site, __, in_depth, depth=100):
    #如果深度达到了最大限度
    if in_depth>=depth:
        return
    in_depth+=1

    #请求页面
    try:
        response=requests.get(site, timeout=10)  #请求
    except:
        out.printcf('无法访问页面{}。'.format(site), __, fg=Fore.RED)
        return
    status=response.status_code  #状态
    if status!=200:  #如果失败
        out.printcf('Can not visit the site \'{}\'. Error: {}'.format(site, str(status)), __, fg=Fore.RED)
        return
    out.printcf('Got data from the site \'{}\'.'.format(site), __, fg=Fore.GREEN)

    #解析HTML
    html=response.content  #HTML
    soup=bs(html, 'lxml')
    links=soup.find_all('a')  #所有链接


    for link in links:  #解析链接
        try:  #检查链接是否有href属性
            href=link.attrs['href']
        except:
            continue

        #如果href不存在
        if type(href)!=type(str()) or href==None:
            out.printcf('找不到链接。', __, fg=Fore.CYAN)
            continue
        
        #链接文字
        title=link.string
        if title==None:  #如果没有文字
            #out.printcf('链接没有文字。', __, fg=Fore.CYAN)
            continue
        title=str(title)  #将链接文字转换成字符串

        #链接操作
        href=urljoin(site, href)  #将href转换为绝对路径
        status=visited(href)  #是否访问过
        if status[0]==True:
            continue
        if status[1]==False:
            out.printcf('links.json有错，请清空文件并重启程序', __, fg=Fore.RED)
        new_visited(href, href)

        '''if urlparse(href).netloc!=urlparse(site).netloc:
            out.printcf('链接跨域名。', __, fg=Fore.RED)
            continue'''

        status=forbidden(href)  #是否被禁止
        if status[0]==True:
            out.printcf('\'{}\'已被禁止访问。'.format(site), __, fg=Fore.RED)
            continue
        if status[1]==False:
            out.printcf('forbid.json有错，请修改文件并重启程序', __, fg=Fore.RED)

        status=is_favourite(title)
        if status[0]:
            out.printcf('已找到你可能喜欢的文章：\'{}\'，链接：\'{}\'，类型：\'{}\''.format(title, href, status[1]), __, fg=Fore.CYAN)
            if not check_links():
                out.printcf('links.json有错，请清空文件并重启程序', __, fg=Fore.RED)
            else:
                new_link(title, href)
        fetch_item(href, __, in_depth, depth)

if __name__=='__main__':
    visit('https://www.bing.com', out.get_data())