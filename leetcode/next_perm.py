#!/usr/bin/env python3

import itertools
import sys
import unittest

# number: 31
# section: meta
# difficulty: medium
# tags: array, two pointers, meta

# constraints
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

def get_next(perms, i):
    if len(perms) == 1:
        return list(perms[0])
    elif i == len(perms)-1:
        return list(perms[0])
    else:
        return list(perms[i+1])

# solution: Pythonic itertools
# complexity
# run-time: O(n)?
# space: O(n)
# TODO: fix bugs
def next_perm(nums):
    """
    Do not return anything, modify nums in-place instead.
    """

    perms = sorted(list(itertools.permutations(nums, len(nums))))
    #print(f"perms:{perms}")

    nextp = []

    for i in range(len(perms)):
        if list(perms[i]) != nums:
            continue

        nextp = get_next(perms, i)

        if nextp == nums:
            nextp = get_next(perms, i+1)

        break

    #print(f"nextp:{nextp}")

    if not nextp:
        return

    # LeetCode: deep copy & list comp doesn't work
    #for i in range(len(nextp)):
        #nums[i] = nextp[i]

    return nextp

# TODO: solve w/o itertools

class TestNextPerm(unittest.TestCase):
    def test1(self):
        nums = [1,2,3]
        expected = [1,3,2]
        self.assertEqual(next_perm(nums), expected)

    def test2(self):
        nums = [3,2,1]
        expected = [1,2,3]
        self.assertEqual(next_perm(nums), expected)

    def test3(self):
        nums = [1,1,5]
        expected = [1,5,1]
        self.assertEqual(next_perm(nums), expected)

    def test4(self):
        nums = [1]
        expected = [1]
        self.assertEqual(next_perm(nums), expected)

    # TODO: fix bugs for test
    def test5(self):
        nums = [2,2,7,5,4,3,2,2,1]
        expected = [2,2,7,5,4,3,2,2,1]
        self.assertEqual(next_perm(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
