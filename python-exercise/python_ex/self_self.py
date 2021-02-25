class Dog:
    #私有方法
    def __send_m(self):
        print('....1....')

    #共有方法
    def send_m(self,new_m):
        if new_m >100:
            self.__send_m()
        else:
            print('buzu')

dog =Dog()
dog.send_m(120)