




class Person:
    name = 'qianxi'
    gender = 'male'
    weight = 0

    def __init__(self,name):
        self.name = name

    def eat(self):
        print('eating')

zs =Person('zhangsan')
zs.eat()