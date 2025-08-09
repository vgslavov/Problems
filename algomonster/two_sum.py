#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: two pointers

# solution: two pointers, opposite direction
# complexity:
# run-time: O(n)
# space: O(1)
def two_sum_sorted(arr: list[int], target: int) -> list[int]:
    left = 0
    right = len(arr)-1

    while left < right:
        two_sum = arr[left] + arr[right]

        if two_sum == target:
            return [left,right]
        elif two_sum > target:
            right -= 1
        else:
            left += 1

    return []

class TestTwoSumSorted(unittest.TestCase):
    def test_example_1(self):
        arr = [1, 2, 3, 4, 5]
        target = 6
        self.assertEqual(two_sum_sorted(arr, target), [0, 4])
        
    def test_example_2(self):
        arr = [1, 2, 3, 4, 5]
        target = 10
        self.assertEqual(two_sum_sorted(arr, target), [])

    def test_example_3(self):
        arr = [1, 2, 3, 4, 5]
        target = 8
        self.assertEqual(two_sum_sorted(arr, target), [2, 4])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    arr = [int(x) for x in input().split()]
    target = int(input())
    res = two_sum_sorted(arr, target)
    print(" ".join(map(str, res)))