import json

def originate(title):
    if type(title)!=type(str()):
        return ''
    title=title.replace(' ', '')
    title=title.replace('\n', '')
    title=title.lower()
    return title

def is_favourite(title):
    if type(title)!=type(str()):
        return [False, '']
    try:
        file=open('favourite.json', encoding='utf-8')  #尝试打开json
        __json=file.read()
        file.close()
    except:  #如果读取失败就返回错误
        return [False, '']
    title=originate(title)
    
    __json=json.loads(__json)  #解析json
    __retu=False  #返回值
    __retu_key=''

    for keys in __json:  #去除所有的验证锁
        points=0  #分数=0
        for key in keys['keys']:  #一个一个锁验证
            key=originate(key)
            if key in title:  #如果锁符合就加分
                points+=1
            elif points-1>0:  #如果不符合就扣分
                points-=1
        if points/len(keys)>=keys['points']:
            __retu=True
            __retu_key=keys['key']
            break
    
    return [__retu, __retu_key]


def check_favourite():
    try:
        file=open('favourite.json', encoding='utf-8')  #尝试打开json
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
        if type(keys['key'])!=type(str()):
            return False
        if type(keys['points'])!=type(int()) and type(keys['points'])!=type(float()):
            return False
        if type(keys['keys'])!=type(list()):
            return False
        for key in keys['keys']:  #一个一个锁验证
            if type(key)!=type(str()):  #如果关键词不是字符串
                return False
    return __retu

if __name__=='__main__':
    print(check_favourite())
    print(is_favourite('Windows 11 发布'))
