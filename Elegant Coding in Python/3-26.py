"""抽象"""
from abc import ABCMeta, abstractmethod

class Fruit(metaclass=ABCMeta):
    @abstractmethod
    def taste(self):
        pass

    @abstractmethod
    def originated(self):
        pass

class Apple:
    def originated(self):
        return 'Japan'

fruit = Fruit()