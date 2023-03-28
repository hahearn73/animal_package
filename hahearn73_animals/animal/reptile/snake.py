from .reptile import Reptile

class Snake(Reptile):
    def __init__(self, name=None, length=0, species="Snake"):
        super().__init__(self, name, species)
        self.length = length

    def eat(self, other=None):
        return f'{self.name} the {self.species} ate {other.name}'

    def __str__(self):
        return f'{self.name} the {self.species} is of length {self.length}'
