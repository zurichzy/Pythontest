
#装饰器写法就是闭包函数
import time
def func1(func):
    def func2():
        print('开始时间为',time.strftime('%S'))
        #代表传入的函数对象被调用
        func()
        print('我是func2')
        print('结束时间为', time.strftime('%S'))
    return func2

@func1
def be_decorate():
    time.sleep(3)
    print('被装饰的函数')

be_decorate()

#返回传入的函数对象
#func1(be_deaorate)
#再加一个括号代表调用函数对象
#func1(be_deaorate)