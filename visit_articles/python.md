# python文件
## **forbid.py**
禁止访问某些网站，这些网站被存放在forbid.json中。
### =>def forbidden(link)
**返回值：[bool forbidden, bool error]**

```
forbidden: True已被禁止，False没有被禁止。
error：False异常，True正常。
```

## **is_favourite.py**
### =>def originate(title)
将字符串还原成最简单的形式。

**返回值：字符串**
### =>def is_favourite(title)
是否喜欢这个标题。

**返回值：[bool is_favourite, 字符串 tag]**

is_favourite：是否喜欢。

tag：标签。

是否喜欢会联系favourite.json计算。

### =>def check_favourite()

检查favourite.json是否符合格式。

**返回值：bool**

## **links.py**

### =>def new_link(title, link)
在links.json中创建链接。

links.json存储已经爬取到的你喜欢的文章的链接。

### =>def check_links()
检查links.json是否符合格式。

**返回值：bool**

### =>def link_exists(link)
检查链接是否已经被标记为喜欢了。

**返回值：[bool exists, bool error]**

exists：链接是否存在。

error：是否有错误，False代表有，True代表没有。

## **visit.py**
访问文章。
### =>def visit(site, __, depth=100)
site：要访问的链接。

__：printc属性。

depth：允许访问的层数。（就当是一棵树，然后不能超过那么多层）。

### =>def fetch_item(site, __, in_depth, depth=100)
site：要访问的链接。

__：printc属性。

in_depth：现在层数。

depth：允许访问的层数。（就当是一棵树，然后不能超过那么多层）。

### `=>小技巧：禁止跨域名访问`
在79~81行：
```python
'''if urlparse(href).netloc!=urlparse(site).netloc:
out.printcf('链接跨域名。', __, fg=Fore.RED)
continue'''
去掉注释可以禁止跨域名访问。建议不要在CSDN使用，除非单独访问blog.csdn.net，否则会将所有的CSDN文章都禁掉。
```

## **visited.py**

### =>def new_visited(title, link)
在visited.json中创建链接。

visited.json存储已经爬取过的链接。

### =>def check_visited()
检查links.json是否符合格式。

**返回值：bool**

### =>def visited(link)
检查链接是否已经被访问过了。

**返回值：[bool exists, bool error]**

exists：链接是否存在。

error：是否有错误，False代表有，True代表没有。

## **open_in_browser.py**
用浏览器打开可能喜欢的文章。直接用python运行即可。