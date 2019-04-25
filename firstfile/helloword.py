class Person:
    def __init__(self,personName):
        self.name = personName
    def printName(self):
        print("我的名字是：", self.name)
def userInput(name):
    userInputname = Person(name) #实例化对象
    userInputname.printName() #调用函数

userInput("liubaoqiang")
