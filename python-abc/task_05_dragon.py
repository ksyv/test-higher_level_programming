#!/usr/bin/env python3
"""Module for Inheritance and mixins."""


class SwimMixin():
    """Mixin class providing swimming capability."""

    def swim(self):
        """Print a message indicating the creature is swimming."""
        print("The creature swims!")


class FlyMixin():
    """Mixin class providing flying capability."""

    def fly(self):
        """Print a message indicating the creature is flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon with swimming and flying abilities."""

    def roar(self):
        """Print a message of the dragon roaring."""
        print("The dragon roars!")

if __name__ == "__main__":
    draco = Dragon()

    draco.swim()
    draco.fly()
    draco.roar()