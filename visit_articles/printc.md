# printc使用

## setup_color()

使用setup_color()来设置颜色。

在初次使用printc时需要设置系统颜色。如果已经设置，这个函数可以帮助你跳过这一步。如果没有设置，这个函数可以帮你设置。

## printc(text, fg='', bg='', css=Style.NORMAL)

输出有颜色的文字。

text：要输出的文字

fg：前景色。

bg：背景色。

css：样式。

fg、bg、css应该用colorama中的Fore、Back、Style。

## printcf(text, __, fg='', bg='', css=Style.NORMAL)

输出有颜色的文字。

text：要输出的文字

__：颜色设置。参考json.md中color.json中的描述。

fg：前景色。

bg：背景色。

css：样式。

fg、bg、css应该用colorama中的Fore、Back、Style。

**__示例**
```python
{"enabled":True, "fg_black":Fore.BLACK, "bg_white":Back.WHITE}
```

## color_test()

颜色设置并将设置保存到color.json中。

## 使用示例
```python
import time
from colorama import Fore, Back, Style
t=time.time()
print(Fore.GREEN+Back.BLACK+Style.NORMAL+'你好'+Style.RESET_ALL)
print(str(time.time()-t))
from printc import *
setup_color()
__json_save=get_data()
printcf('你好。', __json_save)
printcf('printc', __json_save)
printcf('你好', __json_save, fg=Fore.GREEN)
printcf('printc', __json_save, bg=Back.RED)
```