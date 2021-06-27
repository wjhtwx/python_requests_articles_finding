import json

def new_link(title, link):
    if not check_links():
        return [False, 'links.json错误，请重写文件并重启程序。']
    try:
        file=open('links.json', encoding='utf-8')  #尝试打开json
        __json=file.read()
        file.close()
    except:  #如果读取失败就返回错误
        return [False, '无法打开links.json。']
    if __json=='':
        __json='[]'
    __json=json.loads(__json)
    __json.append({"title":title, "link":link})
    try:
        file=open('links.json', 'w', encoding='utf-8')  #尝试打开json
        file.write(json.dumps(__json))
        file.close()
    except:  #如果读取失败就返回错误
        return [False, '无法编辑links.json。']
    return True

def check_links():
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

    for keys in __json:  #去除所有的验证锁
        if type(keys['title'])!=type(str()):
            return False
        if type(keys['link'])!=type(str()):
            return False
    return __retu


def link_exists(link):
    try:
        file=open('links.json', encoding='utf-8')  #尝试打开json
        __json=file.read()
        file.close()
    except:  #如果读取失败就返回错误
        return [False, False]
    if __json=='':
        __json='[]'
        return [False, True]
    __json=json.loads(__json)

    if type(__json)!=type(list()):  #如果__json不是列表
        return [False, False]

    for keys in __json:  #去除所有的验证锁
        if type(keys['title'])!=type(str()):
            return [False, False]
        if type(keys['link'])!=type(str()):
            return [False, False]
        if keys['link']==link:
            return [True, True]
    return [False, True]

if __name__=='__main__':
    print(check_links())
    print(new_link('ysdz', 'https://www.ysdz.com'))