#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: two pointers
# leetcode: 11

# solution: two pointers, opposite direction
# complexity:
# run-time: O(n)
# space: O(1)
def max_area(arr: list[int]) -> int:
    left = 0
    right = len(arr)-1
    max_area = 0

    while left < right:
        area = min(arr[left], arr[right]) * (right-left)
        max_area = max(area, max_area)

        # advance shorter line
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
        
    return max_area

class TestContainerWithMostWater(unittest.TestCase):
    
    def test_container_with_most_water(self):
        self.assertEqual(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(max_area([1, 1]), 1)
        self.assertEqual(max_area([4, 3, 2, 1, 4]), 16)
        self.assertEqual(max_area([1, 2, 1]), 2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    arr = [int(x) for x in input().split()]
    res = max_area(arr)
    print(res)