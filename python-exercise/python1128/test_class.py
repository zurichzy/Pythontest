

#创建一个人类
#通过class关键字，进行定义一个人类
class Preson:
    #类变量
    name = "dedault"
    age =10
    gender  = 'male'
    weight=0

    #构造方法，在实例化的时候被调用
    def __init__(self,name,age,gender,weight):
        #self.变量名的方式，访问的问题，叫做实例变量
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    @classmethod
    def eat(self):
        print(f"{self.name} eating")

'''
类变量和实例变量的区别
类变量是需要类来访问，实例需要实例来访问

'''



