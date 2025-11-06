#!/usr/bin/env python3

from collections import defaultdict, Counter
import sys
import unittest

# number: 75
# title: Sort Colors
# url: https://leetcode.com/problems/sort-colors/
# difficulty: medium
# tags: array, two-pointers, sorting

# constraints:
# 1 <= nums.length <= 300
# nums[i] is either 0, 1, or 2.

def fill(nums, i, value, size):
    while i < size:
        nums[i] = value
        i += 1

    return i

# solution: two pointers
# complexity:
# run-time: O(n)
# space: O(1), range is const
def sort_colors(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    counts = defaultdict(int)
    max_val = 2

    for n in nums:
        counts[n] += 1

    i = 0
    for v in range(max_val+1):
        i = fill(nums, i, v, i+counts[v])

# solution: Pythonic Counter
# complexity:
# run-time: O(n log n)
# space: O(1)
def sort_colors2(nums: list[int]) -> None:
    c = Counter(nums)
    nums[:] = [0] * c[0] + [1] * c[1] + [2] * c[2]

# solution: Dutch National Flag
# complexity:
# run-time: O(n)
# space: O(1)
def sort_colors3(nums: list[int]) -> None:
    lo, i, hi = 0, 0, len(nums)-1

    while i <= hi:
        # swap 0s to the front
        if nums[i] == 0:
            nums[lo], nums[i] = nums[i], nums[lo]
            lo += 1
            i += 1
        # leave 1s in place
        elif nums[i] == 1:
            i += 1
        # swap 2s to the end
        else:
            nums[i], nums[hi] = nums[hi], nums[i]
            hi -= 1

class TestSortColors(unittest.TestCase):
    FUNCS = [sort_colors, sort_colors2, sort_colors3]

    def _assert_sorted_for_all(self, arr, expected):
        for fn in self.FUNCS:
            with self.subTest(impl=fn.__name__):
                nums = list(arr)  # copy
                fn(nums)
                self.assertEqual(nums, expected)

    def test_example1(self):
        self._assert_sorted_for_all([2,0,2,1,1,0], [0,0,1,1,2,2])

    def test_example2(self):
        self._assert_sorted_for_all([2,0,1], [0,1,2])

    def test_example3(self):
        self._assert_sorted_for_all([0], [0])

    def test_example4(self):
        self._assert_sorted_for_all([1], [1])

if __name__ == "__main__":
    sys.exit(unittest.main())