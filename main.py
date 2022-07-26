class Person:
    def __init__(self,name,age,intern,income):
        self.name = name
        self.age = age
        self.intern = intern
        self.income = income

    def myfunc(self):
        print("Hello my name is " + self.name)
        print("My age is ", self.age)
        print("I work at  " + self.intern)
        print("I Earn Rs ", self.income)

p1=Person("Mats",19,"Code Base",10000)
p1.myfunc()



