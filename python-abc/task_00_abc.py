#!/usr/bin/env python3
"""
Module to create abstract class
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Class Mother of other animal detailed class"""
    @abstractmethod
    def sound(self):
        """abstract methode for implement it in the child class"""
        pass

class Dog(Animal):
    """class for create a dog"""
    def sound(self):
        """return the sound of dog"""
        return ("Bark")
    
class Cat(Animal):
    """class for create a cat"""
    def sound(self):
        """return the sound of cat"""
        return ("Meow")
