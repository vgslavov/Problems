#!/usr/bin/env python3

import random
import sys
import unittest

# number: 380
# section: array / string
# difficulty: medium 
# tags: array, hash table, math, design, randomized, top 150

# constraints
# -2^31 <= val <= 2^31 - 1
# At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is called.

# solution: Python dict & list
# complexity
# run-time: O(1) per op
# space: O(n)
class RandomizedSet:

    def __init__(self):
        self.__dict = {}
        self.__list = []

    def insert(self, val: int) -> bool:
        if val in self.__dict:
            return False

        self.__list.append(val)
        self.__dict[val] = len(self.__list)-1
        #print(f"inserted:{val},dict:{self.__dict},list:{self.__list}")

        return True

    def remove(self, val: int) -> bool:
        if val not in self.__dict:
            return False
        
        idx = self.__dict[val]
        del self.__dict[val]

        # swap with last
        self.__list[idx] = self.__list[-1]
        self.__list.pop()

        if idx < len(self.__list):
            self.__dict[self.__list[idx]] = idx

        #print(f"removed:{val},dict:{self.__dict},list:{self.__list}")
        return True

    def remove2(self, val: int) -> bool:
        if val not in self.__dict:
            return False

        last_element, idx = self.__list[-1], self.__dict[val]
        self.__dict[last_element], self.__list[idx] = idx, last_element

        # remove
        del self.__dict[val]
        self.__list.pop()

        return True
        
    def getRandom(self) -> int:
        return random.choice(self.__list) if self.__list else None

    # TODO: getRandom w/o random.choice

# non-solution: Python set
# complexity
# run-time: O(1) per op
# space: O(n)
class RandomizedSet2:

    def __init__(self):
        self.__set = set()

    def insert(self, val: int) -> bool:
        if val in self.__set:
            return False

        self.__set.add(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.__set:
            return False
        
        self.__set.remove(val)

        return True

    def getRandom(self) -> int:
        # removes random element from the set
        val = self.__set.pop()
        self.__set.add(val)

        return val

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(3)
param_2 = obj.remove(2)
param_3 = obj.getRandom()

if __name__ == '__main__':
    sys.exit(unittest.main())