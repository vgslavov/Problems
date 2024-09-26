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
# run-time: O(n^2), too slow, TLE
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
def two_sum_dict(nums, target):
    if not nums:
        return []

    counts = defaultdict(list)

    for i in range(len(nums)):
        counts[nums[i]].append(i)

    ans = []
    values = set()

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff not in counts:
            continue

        for j in counts[diff]:
            pair = tuple(sorted([nums[i],nums[j]]))
            if i == j or pair in values:
                continue

            # need indices, not values!
            ans.append(sorted([i,j]))
            values.add(pair)

    return ans

# solution: two-sum using dict
# run-time: O(n^2)
# space: O(n)
def three_sum2(nums):
    #print(f"len(nums):{len(nums)}")

    if not nums:
        return []

    ans = []
    values = set()

    # O(n)
    for k in range(len(nums)):
        # O(n)
        pair_idx = two_sum_dict(nums, -nums[k])

        #print(f"n:{nums[k]},k:{k},pair_idx:{pair_idx}")
        #print(f"len(pair_idx):{len(pair_idx)}")

        # O(?)
        for i,j in pair_idx:
            if i == j or k == i or k == j:
                continue

            triple = tuple(sorted([nums[i],nums[j],nums[k]]))
            if triple in values:
                continue

            # optimization: don't have to convert set to list later
            ans.append(sorted([nums[i],nums[j],nums[k]]))
            values.add(triple)

    return sorted(ans)

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
def two_sum_binsearch(nums, target):
    if not nums:
        return []

    ans = []
    values = set()

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
        if i == diff_idx:
            continue

        # optimization: don't store indices pointing to same values
        pair = tuple(sorted([nums[i],nums[diff_idx]]))
        if pair not in values:
            ans.append(tuple(sorted([i,diff_idx])))
            values.add(pair)

    return ans

# solution: sort + two-sum using binary search
# run-time: O(n*log n + (n^2)*log n) ~ O((n^2)*log n)
# space: O(1)
def three_sum3(nums):
    #print(f"len(nums):{len(nums)}")

    if not nums:
        return []

    # O(n*log n)
    nums.sort()
    ans = []
    values = set()

    # O(n)
    for k in range(len(nums)):
        # O(n*log n)
        pair_idx = two_sum_binsearch(nums, -nums[k])

        #print(f"n:{nums[k]},k:{k},pair_idx:{pair_idx}")
        #print(f"len(pair_idx):{len(pair_idx)}")

        for i,j in pair_idx:
            if i == j or k == i or k == j:
                continue

            triple = tuple(sorted([nums[i],nums[j],nums[k]]))
            if triple in values:
                continue

            # optimization: don't have to convert set to list later
            ans.append(sorted([nums[i],nums[j],nums[k]]))
            values.add(triple)

    return sorted(ans)

# solution: two pointers
# run-time: O(n^2)
# space: O(1)
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
