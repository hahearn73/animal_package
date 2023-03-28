from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __str__(self):
        pass

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def eat(self, other=None):
        pass
