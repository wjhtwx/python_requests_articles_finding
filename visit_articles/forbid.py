import json
from urllib.parse import urlparse

def forbidden(link):
    link=urlparse(link).netloc
    try:
        file=open('forbid.json', encoding='utf-8')  #尝试打开json
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