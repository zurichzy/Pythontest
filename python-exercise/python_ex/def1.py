'''#定义一个函数的时候是不会执行的
def func():
    print('hhdh')

#调用函数：函数名（）
func()
#函数定义一次，调用多次'''

'''
#函数参数
def sum1(num1,num2): #形参
    print(num1+num2)
#实参
sum1(100,123)
'''

'''#1、函数又return就有返回值，没有就没有返回值；
# 2、只要遇到return就结束（可以写多个return）
#3、但是只有第一个有用--第一个return执行后，函数结束，接下来的return不会执行
def add(a,b):
    return a+b
result = add(12,13)
print(result)'''

'''#main函数，主函数，程序刚开始执行的函数，整体控制
def main():
    print('xxxx')

#调用main函数
main()
'''

#函数嵌套：一个函数里面调用了另一个函数


''''#打印自定义横线
def printLine(n):
    i=0
  5
while i<n:
        print('-'*30)
        i+=1
num = int(input("请输入需要打印的个数："))
printLine(num)

#局部变量：函数内部的，出了函数没用
#全局变量：在函数外边定义的变量--在函数中直接修改全局变量，会报错
#但如果真的需要修改，可以在函数里面进行声明，是加上global
'''
num =100
def test1():
    global  num
    num+=2
    print(num)

test1()

