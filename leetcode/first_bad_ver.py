#!/usr/bin/env python3

import sys
import unittest

# number: 278
# title: First Bad Version
# url: https://leetcode.com/problems/first-bad-version/
# section: meta
# difficulty: easy
# tags: binary search, interactive, meta, grind 75

# constraints
# 1 <= bad <= n <= 2^31 - 1
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# solution: binary search
# complexity
# run-time: O(log n)
# space: O(1)
def first_bad_ver(n: int) -> int:
    left = 0
    right = n-1
    min_bad = -1

    while left <= right:
        mid = left + (right-left) // 2

        if isBadVersion(mid):
            if mid < min_bad:
                min_bad = mid
            right = mid-1
        else:
            left = mid+1

    return min_bad if min_bad > -1 else left

if __name__ == '__main__':
    sys.exit(unittest.main())
