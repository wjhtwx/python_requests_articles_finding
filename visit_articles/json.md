# json文件数据
## sites.json
### 文件示例
```json
[
    {
        "url":"", 
        "start_from":""
    }
]
```
### 文件解释
```json
[
    {
        "url":"",   //需要读取的url，必须是主机名或ip加上https://或http://，如https://www.ysdz.com或http://192.168.1.101
        "start_from":""  //从哪里开始，两端不加斜杠，如articles或about/edge，不可以是/articles/或/about/edge/
    }
]
```

## color.json
### 文件示例
```json
{
    "enabled":true, 
    "fg_black":"black", 
    "bg_white":"white"
}
```
### 文件解释
```json
{
    "enabled":true,   //是否可以使用颜色
    "fg_black":"black",   //前景色黑色
    "bg_white":"white"  //背景色白色
}
```
**为什么要有前景色黑色和背景色白色？**
因为在不同的命令行中，黑色和白色的表示方式是不一样的。在Linux命令行中，黑色应该用Fore.BLACK或者Back.BLACK表示，白色用Fore.WHITE或Back.WHITE表示，Theia命令行则刚好相反，黑色用Fore.WHITE表示，以此类推。

**为什么要有是否可以使用颜色？**
因为Windows命令行可能不支持颜色。

## favourite.json
### 文件示例
```json
[
    {
        "key":"划水", 
        "points":1, 
        "keys":[
            "划水"
        ]
    }, 
    {
        "key":"Windows 11 发布", 
        "points":0.3, 
        "keys":[
            "Windows11", 
            "Microsoft", 
            "官宣"
        ]
    }, 
    {
        "key":"后端", 
        "points":1, 
        "keys":[
            "后端"
        ]
    }
]
```
### 文件解释
```json
[
    {
        "key":"划水",   //类型名称
        "points":1,   //最低要多少分才能算满足条件
        "keys":[  //关键词
            "划水"
        ]
    }, 
    {
        "key":"Windows 11 发布", 
        "points":0.3, 
        "keys":[
            "Windows11", 
            "Microsoft", 
            "官宣"
        ]
    }, 
    {
        "key":"后端", 
        "points":1, 
        "keys":[
            "后端"
        ]
    }
]
```
**最低要多少分才能满足条件**

在is_favourite.py中有关于分数计算的代码。

```python
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
```

简单的来说，分数就是

```
关键词在标题中出现的次数/关键词个数
```

比如说关键词有“Java”，“Python”，标题是“Python自动找你感兴趣的文章”，出现的次数是1，关键词个数是2，分数=1/2=0.5。

## forbid.json
### 文件示例
```json
[
    {
        "title":"github", 
        "link":"www.github.com"
    }
]
```
### 文件解释
```json
[
    {
        "title":"github",   //网页简介或标题
        "link":"www.github.com"  //被禁止的url或域名，必须是主机名或ip并且不能带https://或http://，如www.ysdz.com或192.168.1.101
    }
]
```
**为什么要有forbid.json？**

我们不是有意排除某些网站，但是有些网站加载过慢，会影响程序运行速度，所以可以将加载不出来的网站加到forbid.json中加快程序运行速度。

## links.json
### 文件示例
```json
[
    {
        "title":"Windows11发布", 
        "link":"https://csdnnews.blog.csdn.net/article/details/118208695"
    }
]
```
### 文件解释
```json
[
    {
        "title":"Windows11发布",   //网页简介或标题
        "link":"https://csdnnews.blog.csdn.net/article/details/118208695"  //你可能感兴趣的文章的url
    }
]
```
这个json文件可以帮你方便找到爬虫爬到的网站，然后再浏览器里打开。

## visited.json
### 文件示例
```json
[
    {
        "title":"Windows11发布", 
        "link":"https://csdnnews.blog.csdn.net/article/details/118208695"
    }
]
```
### 文件解释
```json
[
    {
        "title":"Windows11发布",   //网页简介或标题
        "link":"https://csdnnews.blog.csdn.net/article/details/118208695"  //已经访问过的url
    }
]
```
这个json文件可以帮爬虫避免重复访问已经爬取过的url，避免重复访问。