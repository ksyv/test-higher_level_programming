#!/usr/bin/env python3
"""
Module to create abstract class
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract Class Mother of Shape """
    @abstractmethod
    def area(self):
        """abstract methode for implement it in the child class"""
        pass

    @abstractmethod
    def perimeter(self):
        """abstract methode for implement it in the child class"""
        pass

class Circle(Shape):
    """class for create a circle"""
    def __init__(self, radius):
        """initialize a circle"""
        self.radius = radius

    def area(self):
        """return the area of circle"""
        return (pi * self.radius ** 2)
    
    def perimeter(self):
        """return the perimeter of circle"""
        return (2 * self.radius * pi)
    
class Rectangle(Shape):
    """class for create a rectangle"""
    def __init__(self, height, width):
        """initialize a rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """return the area of rectangle"""
        return (self.width * self.height)
    
    def perimeter(self):
        """return the perimeter of rectangle"""
        return ((self.width + self.height) * 2)
    
def shape_info(shape):
    """print area n perimeter of shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
