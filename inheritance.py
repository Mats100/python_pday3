class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I am", self.name, "and I am", self.age, "years old")


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = "dog"

class Cat(Dog):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.type="cat"

tim = Dog("Teddy", 5)
tim.speak()
meow = Cat("Milo",3)
meow.speak()