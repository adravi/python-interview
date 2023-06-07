# https://www.youtube.com/watch?v=46dZH7LDbf8&ab_channel=NeetCode

# Design a class:
#  1. Inserting a value (no duplicates)
#  2. Removing a value
#  3. GetRandom value that is already inserted (with equal probability)
#       random.choice(list)

import random

class Store:
    def __init__(self):
        self.values = []
        self.map = []

    # O(1) time
    def insert(self, value):
        if value in self.map:   # check for duplicates
            return
        
        self.values.append(value)
        self.map[value] = len(self.values) - 1

    # O(1) 
    def remove(self, value):     # a remove-operation is O(1) in a list, if the element removed is the LAST ONE
        if value not in self.map:
            return
        
        lastValue = self.values[-1]
        index = self.map[value]
        
        self.values[index] = lastValue  # swap to-be-removed value to with the last one
        self.values[-1] = value
        
        self.values.pop()               # remove last element from list
        del self.map[value]             # remove element (pair) from map

    # O(1)
    def getRandom(self):
        return random.choice(self.values) # built-in method accepts a list
        

