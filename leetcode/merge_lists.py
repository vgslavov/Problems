#!/usr/bin/env python3

import sys
import unittest

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -10^9 <= nums1[i], nums2[j] <= 10^9
def merge_lists1(nums1, m, nums2, n):
    nums1[m:] = nums2
    nums1.sort()

# extra: 0(m + n) run-time
def merge_lists2(nums1, m, nums2, n):

if __name__ == '__main__':
    sys.exit(unittest.main())
