import json
from colorama import init, Fore, Back, Style
from errors import *

init(convert=True)


#前景色和背景色设置
bg_range=[[Back.BLACK, 'black'], [Back.WHITE, 'white'], [Back.BLUE, 'blue'], [Back.CYAN, 'cyan'], [Back.GREEN, 'green'], [Back.MAGENTA, 'magenta'], [Back.RED, 'red'], [Back.YELLOW, 'yellow']]  #背景色

fg_range=[[Fore.WHITE, 'white'], [Fore.BLACK, 'black'], [Fore.BLUE, 'blue'], [Fore.CYAN, 'cyan'], [Fore.GREEN, 'green'], [Fore.MAGENTA, 'magenta'], [Fore.RED, 'red'], [Fore.YELLOW, 'yellow']]  #前景色


def setup_color():  #背景颜色设置
    try:  #尝试打开json
        file=open('color.json', encoding='utf-8')
        file.close()
    except:  #如果没有配置文件就进行颜色测试
        color_test()


def printc(text, fg='', bg='', css=Style.NORMAL):  #带有颜色的输出
    try:
        __json=get_data()
        #当没有定义fg和bg时就自己加载
        if fg=='':
            fg=__json['fg_black']
        if bg=='':
            bg=__json['bg_white']
        #输出
        if __json['enabled']:
            try:
                print(fg+bg+css+text+Style.RESET_ALL)
            except:
                print(text)
        else:
            print(text)
    except:
        raise unexpected_json_data('错误：json数据错误。')


def printcf(text, __, fg='', bg='', css=Style.NORMAL):  #带有颜色的输出
    #当没有定义fg和bg时就自己加载
    if fg=='':
        fg=__['fg_black']
    if bg=='':
        bg=__['bg_white']
    #输出
    if __['enabled']:
        try:
            print(fg+bg+css+text+Style.RESET_ALL)
        except:
            print(text)
    else:
        print(text)


def get_data():  #读取json数据
    try:
        __retu=dict()  #返回的数据
        #读取json
        file=open('color.json', encoding='utf-8')
        __json=file.read()
        __json=json.loads(__json)  #解析json
        file.close()
        #检查数据类型
        if type(__json['enabled'])!=type(bool()):
            printcf('错误：json文件可能已经损坏或不存在。尝试删除color.json并重启程序。', {"enabled":True, "fg_black":Fore.RED, "bg_white":Back.CYAN}, css=Style.BRIGHT)
            return {"enabled":True, "fg_black":Fore.BLACK, "bg_white":Back.WHITE}  #json数据
        #颜色是否可用
        __retu['enabled']=__json['enabled']
        #前景色
        for color in fg_range:
            if color[1]==__json['fg_black']:
                __retu['fg_black']=color[0]
        #背景色
        for color in bg_range:
            if color[1]==__json['bg_white']:
                __retu['bg_white']=color[0]
        return __retu
    except:
        printcf('错误：json文件可能已经损坏或不存在。尝试删除color.json并重启程序。', {"enabled":True, "fg_black":Fore.RED, "bg_white":Back.CYAN}, css=Style.BRIGHT)
        return {"enabled":True, "fg_black":Fore.BLACK, "bg_white":Back.WHITE}  #json数据


def color_test():  #测试颜色
    print('对不起，但是你必须要通过这个颜色测试才能继续使用我们的产品，因为这个测试能够帮助我们更好地为你提供服务。我们不会收集你的任何信息。经过这个测试之后，我们会把测试结果存放到color.json中，这样你就不用重复进行这个测试了。')
    print('I am really sorry to disturb you but you have to pass this color test to use out products so that we can provide a greater service. We will save your answers to color.json so that you won\'t need to pass this test again.')
    print('\n')


    __json={"enabled":True, "fg_black":"black", "bg_white":"white"}  #json数据


    #背景色测试
    print('首先我们要测试背景颜色。接下来你将看到白色背景的“你好”。')
    print('First we are going to test the background. You will see text with white background.')
    __found=False  #是否找到可用的颜色
    __bg=Back.BLACK
    #把每一个颜色都试一遍
    for color in bg_range:
        #询问
        print(color[0]+'\n\n你好\n\n'+Style.RESET_ALL)
        print('你看到的是白色背景吗？Are you seeing the text with white background? 不需要管有没有文字。You needn\'t worry if you can\'t see the text.')
        #输入
        answer=input('是：Y，不是：N，乱码：C。Yes:Y, No:N, Chaos:C. 请输入（please input）：')
        #判断
        if answer=='C':  #乱码就是不能用颜色模式
            __json['enabled']=False
            break
        elif answer=='Y':  #测试成功
            __json['bg_white']=color[1]  #设置背景色
            __found=True  #找到了可用的颜色
            __bg=color[0]
            break
    if __found==False:  #找不到可用的背景色
        __json['enabled']=False
    

    #前景色测试
    print('接下来我们要测试前景颜色。接下来你将看到黑色前景的“你好”。')
    print('Then we are going to test the foreground. You will see text with black foreground.')
    __found=False  #是否找到可用的颜色
    #把每一个颜色都试一遍
    for color in fg_range:
        #询问
        print(__bg+color[0]+'\n\n你好\n\n'+Style.RESET_ALL)
        print('你看到的是黑色前景吗？Are you seeing the text with black foreground?')
        #输入
        answer=input('是：Y，不是：N，乱码：C。Yes:Y, No:N, Chaos:C. 请输入（please input）：')
        #判断
        if answer=='C':  #乱码就是不能用颜色模式
            __json['enabled']=False
            break
        elif answer=='Y':  #测试成功
            __json['fg_black']=color[1]  #设置前景色
            __found=True  #找到了可用的颜色
            break
    if __found==False:  #找不到可用的前景色
        __json['enabled']=False

    #写入文件
    __json=json.dumps(__json)  #json解析
    print('你的json文件将是：')
    print(__json)  #输出json数据
    file=open('color.json', 'w', encoding='utf-8')  #打开json
    file.write(__json)  #写入数据
    file.close()

if __name__=='__main__':
    setup_color()
    __json_save=get_data()
    printc('你好。')
    printc('printc')
    printc('你好', fg=Fore.GREEN)
    printc('printc', bg=Back.RED)
    printcf('你好。', __json_save)
    printcf('printc', __json_save)
    printcf('你好', __json_save, fg=Fore.GREEN)
    printcf('printc', __json_save, bg=Back.RED)