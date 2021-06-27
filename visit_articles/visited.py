import json

def new_visited(title, link):
    if not check_visited():
        return [False, 'visited.json错误，请重写文件并重启程序。']
    try:
        file=open('visited.json', encoding='utf-8')  #尝试打开json
        __json=file.read()
        file.close()
    except:  #如果读取失败就返回错误
        return [False, '无法打开visited.json。']
    if __json=='':
        __json='[]'
    __json=json.loads(__json)
    __json.append({"title":title, "link":link})
    try:
        file=open('visited.json', 'w', encoding='utf-8')  #尝试打开json
        file.write(json.dumps(__json))
        file.close()
    except:  #如果读取失败就返回错误
        return [False, '无法编辑visited.json。']
    return True

def check_visited():
    try:
        file=open('visited.json', encoding='utf-8')  #尝试打开json
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


def visited(link):
    try:
        file=open('visited.json', encoding='utf-8')  #尝试打开json
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