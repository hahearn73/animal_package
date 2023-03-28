from ..animal import Animal
from abc import ABC, abstractmethod

class Mammal(Animal):
    def __init__(self, name=None, species=None, isMale=True):
        super().__init__(name, species, isMale)

    @abstractmethod
    def give_live_birth():
        pass
