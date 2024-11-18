#!/usr/bin/env python3
"""Module for Inheritance."""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Print the fish shift."""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Print the bird shift."""
        print("The bird is flying")

    def habitat(self):
        """Print the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish, inheriting from Fish and Bird."""

    def fly(self):
        """Print the flying fish shift."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print the flying fish shift."""
        print("The flying fish is swimming")

    def habitat(self):
        """Print the flying fish's dual habitat."""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    silver_fish = FlyingFish()

    silver_fish.fly()
    silver_fish.swim()
    silver_fish.habitat()

    print(FlyingFish.mro())