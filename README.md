# python_requests_articles_finding

使用python自动划水找你感兴趣的文章。

Use python to find articles you might like automatically.

```
I am sorry my American and other foreign friends, I am really sorry but this readme file and python files haven't been translated into English yet. Please, wait for me, just for a second, for me to translate them into English.
```

# python自动查找你喜欢的文章

在划水的时候难免要到掘金、CSDN逛一圈，这个时候就要找一些文章看看了。

首页有许多文章和视频，但是那些是我们喜欢的呢？

这个问题自己解决好累啊，划水划惯了，什么都懒得做，算了，还是拿python找吧。

随手打开了Eclipse Theia

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d11a292da1444c6b93034e7f56699767~tplv-k3u1fbpfcp-watermark.image)

这个问题很简单，实质上就是拿python把所有的文章遍历一遍。
可是居然花了我两天才做完，弄了一个庞（迷）大（你）的开源项目。好吧，毕竟是我第一次在GitHub上发布代码。
[https://github.com/wjhtwx/python_requests_articles_finding/tree/visit_articles](https://github.com/wjhtwx/python_requests_articles_finding/tree/visit_articles)

## 制作思路
建立favourite.json存储喜欢的关键词，links.json存放找出来的链接，forbid.json存储不让访问的网站，sites.json存储要爬取的网站。
printc用于彩色输出。visit_articles.py是主文件。
流程：

- 启动。
- 检查json文件是否完好。
- 开始按照sites.json访问网站。
- 检查当前页面有没有被访问过，避免循环。
- 处理，将喜欢的页面存入links.json方便一起打开

## 所需环境

|  |  |
|--|--|
|python3|必须是CPython，Pypy3可能会有一些模块装不了。|
|colorama|显示彩色文字，printc就是用它封装的。|
|requests|请求网页|
|beautifulsoup4|解析HTML|
|lxml|beautifulsoup4依赖|
|urllib|python自带，解析url|


## 文件目录

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cd02b09095840b39f95ba2608884034~tplv-k3u1fbpfcp-watermark.image)

## readme

[printc：https://github.com/wjhtwx/python_requests_articles_finding/blob/visit_articles/printc.md](https://github.com/wjhtwx/python_requests_articles_finding/blob/visit_articles/printc.md)

[json：https://github.com/wjhtwx/python_requests_articles_finding/blob/visit_articles/json.md](https://github.com/wjhtwx/python_requests_articles_finding/blob/visit_articles/json.md)

[https://github.com/wjhtwx/python_requests_articles_finding/blob/visit_articles/python.md](https://github.com/wjhtwx/python_requests_articles_finding/blob/visit_articles/python.md)

代码有很详细的注释，可以直接在GitHub上看。

## 运行效果


![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c962bf0245f4c4796d6dbc923e1cfd2~tplv-k3u1fbpfcp-watermark.image)

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f847bce484b64496936412e8e9ccd300~tplv-k3u1fbpfcp-watermark.image)

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81a705ee988e483597f2d47cee5ac602~tplv-k3u1fbpfcp-watermark.image)

## 更新
### printc
printc是封装了colorama用于在命令行中输出颜色的。更新版本支持Windows系统。

