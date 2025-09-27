#!/usr/bin/env python3

import math
import sys
import unittest

def can_finish_eating(piles, h, k):
    hours_used = 0

    for p in piles:
        hours_used += math.ceil(p/k)

    return hours_used <= h

# solution: binary search
# complexity:
# run-time: O(n*log m) where n is number of piles and m is max pile size
# space: O(1)
def min_eatingspeed(piles: list[int], h: int) -> int:
    left = 1
    right = 1000000000
    ans = -1

    while left <= right:
        mid = left + (right-left)//2

        if can_finish_eating(piles, h, mid):
            # record if feasible, but keep searching for smaller k
            ans = mid
            right = mid-1
        else:
            left = mid+1

    return ans

class TestMinEatingSpeed(unittest.TestCase):
    
    def test_min_eatingspeed(self):
        self.assertEqual(min_eatingspeed([3,6,7,11], 8), 4)
        self.assertEqual(min_eatingspeed([30,11,23,4,20], 5), 30)
        self.assertEqual(min_eatingspeed([30,11,23,4,20], 6), 23)

if __name__ == "__main__":
    sys.exit(unittest.main())