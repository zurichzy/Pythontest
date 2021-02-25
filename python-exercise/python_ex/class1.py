#面向对象
'''
类就是模型，实体就是对象
属性：一组数据（身高、体重）
方法：行为、功能（跑、跳）
定义一个类：
class 类名：
    xxxxx

'''
#定义一个类
class  Cat:
    #属性:创建完对象后，立马自动调用
    def __init__(self):
        print('hahhahh')

    #方法（类里面定义的是方法，外边定义的是函数）
    def eat(self):
        print('吃')
    def drink(self):
        print('喝')
#创建一个对象
xiaomao = Cat()
#调用方法，有括号
xiaomao.eat()
xiaomao.drink()
#添加属性
#如果没有属性，去访问，会报错
xiaomao.color = '白色'
#获取xiaomao对象的数据，属性不加括号
a = xiaomao.color
print(a)


'''
#给一个对象添加属性的方法
#对象名.新的属性名 = 值

获取这个对象的属性，2种方法：
1.对象.属性
2.定义一个方法，这个方法种，使用self.属性

'''


