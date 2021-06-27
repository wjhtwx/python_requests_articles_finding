import webbrowser
import json
import printc as out

def open_links():
    try:
        file=open('links.json', encoding='utf-8')  #尝试打开json
        __json=file.read()
        file.close()
    except:  #如果读取失败就返回错误
        return False
    if __json=='':
        __json='[]'
    __json=json.loads(__json)
    __retu=True  #返回值

    if type(__json)!=type(list()):  #如果__json不是列表
        return False

    __=out.get_data()
    out.printcf('接下来你将会看到一些链接，这些是你可能喜欢的文章。按下回车以打开它们，输入N或n关闭它们。', __, fg=out.Fore.GREEN)
    for keys in __json:  #去除所有的验证锁
        if type(keys['title'])!=type(str()):
            return False
        if type(keys['link'])!=type(str()):
            return False
        out.printcf('你可能喜欢的文章：\'{}\'。'.format(keys['title']), __, fg=out.Fore.CYAN)
        out.printcf('链接：\'{}\'。'.format(keys['link']), __)
        __now=input('')
        if __now.lower()!='n':
            webbrowser.open(keys['link'])
    return __retu


if __name__=='__main__':
    open_links()