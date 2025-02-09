# 对于 类属性  和 实例属性  的理解 以及调用的方法和优先级
class Person:
    a = 10  # 类属性

    def __init__(self, a=5):
        self.a = a

    def show(self):
        print(self.__class__.a)  # 使用类属性
    def show1(self):
        print(self.a)  # 使用类属性
b = Person()
b.show()  # 输出 10
b.show1()  # 输出 5