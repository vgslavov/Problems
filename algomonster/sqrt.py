#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: binary search
# leetcode: 69

# solution: binary search
# complexity:
# run-time: O(log n)
# space: O(1)
def sqrt(n: int) -> int:
    if not n:
        return 0

    left = 1
    right = n
    ans = 0

    while left <= right:
        mid = left + (right-left) // 2
        squared = mid * mid
        
        if squared == n:
            return mid
        elif squared > n:
            # record first not smaller
            ans = mid
            right = mid-1
        else:
            left = mid+1
            
    # square root is b/w ans and ans-1
    return ans-1

class TestSqrt(unittest.TestCase):
    def test_example_1(self):
        n = 16
        self.assertEqual(sqrt(n), 4)
        
    def test_example_2(self):
        n = 14
        self.assertEqual(sqrt(n), 3)

    def test_example_3(self):
        n = 0
        self.assertEqual(sqrt(n), 0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    n = int(input())
    res = sqrt(n)
    print(res)