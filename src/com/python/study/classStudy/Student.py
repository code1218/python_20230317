class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print(f'이름: {self.name}')
        print(f'나이: {self.age}')

    @classmethod
    def classMethod(cls, _name):
        cls._name = _name

    @classmethod
    def classMethod2(cls):
        print(cls._name)

    @staticmethod
    def staticMethod():
        print('static test')

