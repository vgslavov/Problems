#!/usr/bin/env python3

import sys
import unittest

# number: 287
# section:
# difficulty: medium
# tags: 

# constraints
# 1 <= n <= 10^5
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer
# which appears two or more times.

def set_bit(value, index):
    return value | (1 << index)

def get_bit(value, index):
    return value & (1 << index)

# solution: bitmap
# complexity
# run-time: O(n)
# space: O(1)
def find_duplicate(nums):
    bitmap = 0
    for num in nums:
        #print("{}:{}:{}".format(num, bin(num), bin(bitmap)))
        if get_bit(bitmap, num):
            return num
        else:
            bitmap = set_bit(bitmap, num)

class TestFindDuplicate(unittest.TestCase):
    def test1(self):
        nums = [1,5,1,3,1,4]
        expected = 1
        self.assertEqual(find_duplicate(nums), expected)

    def test2(self):
        nums = [1,3,4,2,2]
        expected = 2
        self.assertEqual(find_duplicate(nums), expected)

    def test3(self):
        nums = [3,1,3,4,2]
        expected = 3
        self.assertEqual(find_duplicate(nums), expected)

    def test4(self):
        nums = [3,3,3,3,3]
        expected = 3
        self.assertEqual(find_duplicate(nums), expected)

    def test5(self):
        nums = [13,46,8,11,20,17,40,13,13,13,14,1,13,36,48,41,13,13,13,13,45,
                13,28,42,13,10,15,22,13,13,13,13,23,9,6,13,47,49,16,13,13,39,
                35,13,32,29,13,25,30,13]
        expected = 13
        self.assertEqual(find_duplicate(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
