class Person:
    def __init__(self,walk):
        self.walk = walk

class Dog(Person):
    def __init__(self,walk,bark,run):
        self.walk = walk
        self.bark = bark
        self.run = run


class Cat(Dog):
    def __init__(self,walk,purr,run,heal):
        self.walk = walk
        self.purr = purr
        self.run = run
        self.heal = heal