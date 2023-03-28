from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name=None, species=None, isMale=True):
        self.name = name
        self.species = species
        self.isMale = isMale

    @abstractmethod
    def eat(self, other=None):
        pass
        
    @abstractmethod
    def __str__(self):
        pass
