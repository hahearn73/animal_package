from .mammal import Mammal

class Bear(Mammal):
    def __init__(self, name, isMale=True, color="black"):
        super().__init__(name, "bear", isMale)
        self.color = color

    def __str__(self):
        if isMale:
            sex = "male"
        else:
            sex = "female"
        return f'{self.name} is a {self.color}, {sex} bear'

    def eat(self, other=None):
        print(f'{self.name} ate {other.name}')

    def give_live_birth():
        return self.__init__(self.name + "Jr.", self.color)
