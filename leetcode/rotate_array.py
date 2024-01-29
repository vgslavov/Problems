#!/usr/bin/env python3

import sys
import unittest

# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5
def rotate_array1(nums, k):
    return nums[-k:] + nums[:-k]

# extra: in-place w/ O(1) space
def rotate_array2(nums, k):

if __name__ == '__main__':
    sys.exit(unittest.main())
