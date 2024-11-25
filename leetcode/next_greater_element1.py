#!/usr/bin/env python3

import sys
import unittest

# number: 496
# section: assessment
# difficulty: easy
# tags: array, hash table, stack, monotonic stack, meta

# constraints
# 1 <= nums1.length <= nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 10^4
# All integers in nums1 and nums2 are unique.
# All the integers of nums1 also appear in nums2.

# solution: dict
# complexity
# run-time: O(n*m)
# space: O(n)
def next_greater_element1(nums1, nums2):
    ans = []
    num2index = {num: i for i, num in enumerate(nums2)}

    for i in range(len(nums1)):
        j = num2index[nums1[i]]
        for k in range(j, len(nums2)):
            if nums2[k] > nums1[i]:
                ans.append(nums2[k])
                break
        else:
            ans.append(-1)

    return ans

# TODO: solve linearly

class TestNextGreaterElement1(unittest.TestCase):
    def test1(self):
        nums1 = [4,1,2]
        nums2 = [1,3,4,2]
        expected = [-1,3,-1]
        self.assertEqual(next_greater_element1(nums1, nums2), expected)

    def test2(self):
        nums1 = [2,4]
        nums2 = [1,2,3,4]
        expected = [3,-1]
        self.assertEqual(next_greater_element1(nums1, nums2), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
