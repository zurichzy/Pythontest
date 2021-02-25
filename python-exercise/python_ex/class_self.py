class Dog:
    def __init__(self,newColor):
        self.color = newColor

    def bark(self):
        print('....wangwnagjiao...')

    def printColor(self):
        print("颜色为： %s"%self.color)
wangcai = Dog('白')
wangcai.printColor()