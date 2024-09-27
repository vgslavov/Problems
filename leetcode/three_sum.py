#!/usr/bin/env python3

import bisect
from collections import defaultdict
import sys
import unittest

# number: 15
# section: two pointers
# difficulty: medium
# tags: array, two pointers, sorting, top 150

# constraints
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5

# solution: dict + brute-force
# run-time: O(n^3)?, too slow, TLE
# space: O(n)
def three_sum(nums):
    #print(f"len(nums):{len(nums)}")

    counts = defaultdict(list)

    # key: number
    # values: list of indices in nums
    for i in range(len(nums)):
        counts[nums[i]].append(i)

    #print(f"counts:{counts}")

    ans = set()

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue

            third = -nums[i] - nums[j]

            if third not in counts:
                continue

            #print(f"third:{third},counts[third]:{counts[third]}")
            for k in counts[third]:
                if i != k and j != k:
                    ans.add(tuple(sorted([nums[i], nums[j], third])))
                    # optimization: don't go through all counts' values
                    break

    return sorted([list(v) for v in ans])

# solution: dict
# complexity
# run-time O(n)
# space: O(n)
def two_sum_dict(nums, k, counts, ans):
    if not nums:
        return

    target = -nums[k]

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff not in counts:
            continue

        for j in counts[diff]:
            if i == j or i == k or j == k:
                continue
            ans.add(tuple(sorted([nums[i],nums[j],nums[k]])))

# solution: two-sum using dict
# run-time: O(n^2), too slow, TLE
# space: O(n)
def three_sum2(nums):
    #print(f"len(nums):{len(nums)}")

    if not nums:
        return []

    # O(n*log n)
    nums.sort()
    ans = set()

    counts = defaultdict(list)
    for i in range(len(nums)):
        counts[nums[i]].append(i)

    # O(n)
    for k in range(len(nums)):
        # optimization
        if nums[k] > 0:
            break

        # O(n)
        two_sum_dict(nums, k, counts, ans)

    return sorted([list(v) for v in ans])

# complexity
# run-time: O(log n)
# space: O(1)
def binary_search(nums, k):
    if not nums:
        return None

    left = 0
    right = len(nums)-1

    while left <= right:
        mid = left + (right-left)//2

        if nums[mid] == k:
            return mid
        elif nums[mid] > k:
            right = mid-1
        else:
            left = mid+1

    return left

# solution: binary search
# complexity
# run-time O(n*log n)
# space: O(1)
def two_sum_binsearch(nums, k, ans):
    if not nums:
        return

    target = -nums[k]

    for i in range(len(nums)):
        diff = target - nums[i]

        # optimization: don't search for smaller numbers later (it's sorted)
        if diff < nums[i]:
            continue

        # binary search
        # manual
        #diff_idx = binary_search(nums, diff)
        # Pythonic
        diff_idx = bisect.bisect_left(nums, diff)
        #print(f"diff_dix:{diff_idx}")

        # not found
        if diff_idx >= len(nums) or nums[diff_idx] != diff:
            continue

        # same index/value
        if i == diff_idx or i == k or k == diff_idx:
            continue

        ans.add(tuple(sorted([nums[i],nums[diff_idx],nums[k]])))

# solution: sort + two-sum using binary search
# run-time: O(n*log n + (n^2)*log n) ~ O((n^2)*log n), too slow, TLE
# space: O(1)
def three_sum3(nums):
    #print(f"len(nums):{len(nums)}")

    if not nums:
        return []

    # O(n*log n)
    nums.sort()
    ans = set()

    # O(n)
    for k in range(len(nums)):
        # optimization: sorted input, can't add up to 0 if all positive
        if nums[k] > 0:
            break

        # O(n*log n)
        two_sum_binsearch(nums, k, ans)

    return sorted([list(v) for v in ans])

# solution: two pointers
# run-time: O(n^2)?
# space: O(1)
# TODO: finish/fix
def three_sum4(nums):
    # O(n*log n)
    nums.sort()

    i = 0
    j = len(nums)-1

    ans = set()

    # O(n)
    while i < j:
        third = -nums[i] - nums[j]

        # O(log n)
        k = bisect.bisect_left(nums, third)
        print(f"third:{third} @ k:{k}")

        # not found
        if k >= len(nums) or nums[k] != third:
            if nums[i] > nums[j]:
                i += 1
            else:
                j -= 1
            continue

        # same
        if i == j or i == k or j == k:
            if nums[i] > nums[j]:
                i += 1
            else:
                j -= 1
            continue

        ans.add(tuple(sorted([nums[i],nums[j],nums[k]])))

        if nums[i] > nums[j]:
            i += 1
        else:
            j -= 1

    return sorted([list(v) for v in ans])

class TestThreeSum(unittest.TestCase):
    def test_none(self):
        nums = [0,1,1]
        expected = []
        self.assertEqual(three_sum(nums), expected)
        self.assertEqual(three_sum2(nums), expected)
        self.assertEqual(three_sum3(nums), expected)
        #self.assertEqual(three_sum4(nums), expected)

    def test_0s(self):
        nums = [0,0,0]
        expected = [[0,0,0]]
        self.assertEqual(three_sum(nums), expected)
        self.assertEqual(three_sum2(nums), expected)
        self.assertEqual(three_sum3(nums), expected)
        #self.assertEqual(three_sum4(nums), expected)

    def test_many_0s(self):
        nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        expected = [[0,0,0]]
        self.assertEqual(three_sum(nums), expected)
        # too slow
        #self.assertEqual(three_sum2(nums), expected)
        self.assertEqual(three_sum3(nums), expected)

    def test1(self):
        nums = [-1,0,1,2,-1,-4]
        expected = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(three_sum(nums), expected)
        self.assertEqual(three_sum2(nums), expected)
        self.assertEqual(three_sum3(nums), expected)

    def test2(self):
        nums = [3,0,-2,-1,1,2]
        expected = [[-2,-1,3],[-2,0,2],[-1,0,1]]
        self.assertEqual(three_sum(nums), expected)
        self.assertEqual(three_sum2(nums), expected)
        self.assertEqual(three_sum3(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
