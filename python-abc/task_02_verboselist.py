#!/usr/bin/env python3
"""
Module with class VerboseList
"""


class VerboseList(list):
    """Class with methode for append, axtend, remove and pop"""
    def append(self, item):
        '''Appends an item to the list.'''
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, extension):
        '''Extends the list.'''
        count = len(extension)
        super().extend(extension)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        '''Removes an item from the list.'''
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        '''Pops an item from the list.'''
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)