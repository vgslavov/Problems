#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: binary search
# leetcode: 153

# ugly solution
# complexity:
# run-time: O(log n)
# space: O(1)
def find_min2(arr: list[int]) -> int:
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = left + (right-left) // 2

        # rotation is to the right
        if arr[mid] > arr[-1]:
            left = mid+1
        elif mid > 0 and mid < len(arr)-1 and arr[mid-1] > arr[mid] and arr[mid] < arr[mid+1]:
            return mid
        else:
            right = mid-1
            
    return mid

# solution: follow pattern
# complexity:
# run-time: O(log n)
# space: O(1)
def find_min(arr: list[int]) -> int:
    left = 0
    right = len(arr)-1
    boundary = 0

    while left <= right:
        mid = left + (right-left) // 2

        # min is to the left
        if arr[mid] <= arr[-1]:
            # record first not larger
            boundary = mid
            right = mid-1
        else:
            left = mid+1
            
    return boundary

class TestFindMinRotated(unittest.TestCase):

    def test_find_min_rotated(self):
        self.assertEqual(find_min([4, 5, 6, 7, 0, 1, 2]), 4)
        self.assertEqual(find_min2([4, 5, 6, 7, 0, 1, 2]), 4)

        self.assertEqual(find_min([1, 2, 3, 4, 5]), 0)
        self.assertEqual(find_min2([1, 2, 3, 4, 5]), 0)

        self.assertEqual(find_min([5, 1, 2, 3, 4]), 1)
        self.assertEqual(find_min2([5, 1, 2, 3, 4]), 1)

        self.assertEqual(find_min([2, 3, 4, 5, 1]), 4)
        self.assertEqual(find_min2([2, 3, 4, 5, 1]), 4)

        self.assertEqual(find_min([3, 4, 5, 1, 2]), 3)
        self.assertEqual(find_min2([3, 4, 5, 1, 2]), 3)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    arr = [int(x) for x in input().split()]
    res = find_min(arr)
    print(res)