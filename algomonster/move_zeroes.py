#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: two pointers, sliding window

# solution: two pointers, fast & slow
# complexity:
# run-time: O(n)
# space: O(1)
def move_zeros(nums: list[int]) -> None:
    slow, fast = 0, 0
    
    while fast < len(nums):
        # if fast is zero, do nothing

        # if fast is not zero, swap with slow
        if nums[fast] != 0:        
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

        fast += 1

# solution: overwrite
# complexity:
# run-time: O(n)
# space: O(1)
def move_zeros2(nums: list[int]) -> None:
    # copy in-place
    i = 0

    for n in nums:
        if n != 0:
            nums[i] = n
            i += 1

    # fill rest with zeros
    while i < len(nums):
        nums[i] = 0
        i += 1

class TestMoveZeroes(unittest.TestCase):
    def test_empty(self):
        nums = []
        expected = []
        move_zeros(nums)
        self.assertEqual(nums, expected)
        
    def test1(self):
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        move_zeros(nums)
        self.assertEqual(nums, expected)

    def test2(self):
        nums = [0]
        expected = [0]
        move_zeros(nums)
        self.assertEqual(nums, expected)
        
    def test3(self):
        nums = [1, 0, 1]
        expected = [1, 1, 0]
        move_zeros(nums)
        self.assertEqual(nums, expected)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Binary Search Implementation")
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    nums = [int(x) for x in input().split()]
    move_zeros(nums)
    print(" ".join(map(str, nums)))

