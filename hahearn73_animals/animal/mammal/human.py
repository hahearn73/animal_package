from .mammal import Mammal

class Human(Mammal):
    def __str__(self):
        return f'Human: {self.name}, {self.age} yo, {self.weight} lbs, {self.height} inches'

    def __init__(self, name, age=None, height=None, weight=None, isMale=True):
        super().__init__(name, "Human", isMale)
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self, other=None):
        print(f'{self.name} ate {other.name}')

    def give_live_birth():
        return self.__init__(self.name + " Jr.", 0, 10, 10)
