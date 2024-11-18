#!/usr/bin/env python3
""" module for iterator. """

class CountedIterator():
    """ Class for extends the buil-in iterator """

    def __init__(self, iterator):
        """ Method that initialise iterator and counter """

        self.iterator = iter(iterator)
        self.counter = 0

    def __next__(self):
        """ Method that count items """
        try:
            next_item = next(self.iterator)
            self.counter += 1
            return next_item
        except StopIteration:
            raise StopIteration("End of iterator reached.")

    def get_count(self):
        """ Method that returns number of return"""
        return self.counter

if __name__ == "__main__":
    test_counter = [1, 2, 4, 8, 16]
    counted = CountedIterator(test_counter)

    try:
        while True:
            item = next(counted)
            print(f"Got {item}, total {counted.get_count()} items iterated.")
    except StopIteration:
        print("No more items.")