
#1、理解闭包函数
#理解闭包函数的定义
#2、变量在不同函数中的作用
#闭包函数
#定义函数
name ='鲸鱼'
def func1():
    print(name)
    #在函数func1内再定义一个函数
    def func2():
        name = '虾米'
        print('我是func2')
    #返回肚子里面的函数对象
    return func2
#函数对象--不加括号
func1
#函数调用--加了括号
#func1的调用,其实=func2
func22=func1()
#func22是return的func2的函数对象
func22()