#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract class representing an animal.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method for making a sound.
        """
        pass

class Dog(Animal):
    """
    Dog class inheriting from Animal.
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    Cat class inheriting from Animal.
    """
    def sound(self):
        return "Meow"
