
#__str__
class Dog:
    def __init__(self,newColor):
        self.color = newColor

    def bark(self):
        print('....wangwnagjiao...')

    def printColor(self):
        print("颜色为： %s"%self.color)

    def __str__(self):
        return self.color
def test(aaa):
    aaa.printColor()

wangcai = Dog('白')
wangcai.printColor()

xiaoqing = Dog('hei')
xiaoqing.printColor()

print(wangcai)