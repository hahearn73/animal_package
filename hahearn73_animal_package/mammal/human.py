from ..animal import Animal

class Human(Animal):
    def __str__(self):
        return f'Human: {self.name}, {self.age} yo, {self.weight} lbs, {self.height} inches'

    def __init__(self, name, age=None, height=None, weight=None):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self, other=None):
        print(f'{self.name} ate {other.name}')
