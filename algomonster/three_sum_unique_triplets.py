#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: two pointers, deduplication

# solution: two pointers
# complexity:
# run-time: O(n)
# space: O(1)
def two_sum(nums, left, right, target):
    ans = []

    while left < right:
        cur_sum = nums[left] + nums[right]
        if cur_sum == target:
            ans.append([nums[left], nums[right]])
            # skip dupes
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -= 1
            left += 1
            right -= 1
        elif cur_sum < target:
            left += 1
        else:
            right -= 1

    return ans

# solution: sort + two pointers + deduplication
# complexity:
# run-time: O(n*log n) + O(n^2) ~ O(n^2)
# space: O(n) if slicing, else O(1)
def three_sum_unique_triplets(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    ans = []

    for i in range(len(nums)):
        # skip dupes
        if i and nums[i] == nums[i-1]:
            continue

        tuples = two_sum(nums, i+1, len(nums)-1, target-nums[i])
        # slicing creates new list: O(n) space
        #tuples = two_sum(nums[i+1:], target-nums[i])
        for t in tuples:
            ans.append([nums[i],t[0],t[1]])
        
    return ans

class TestThreeSumUniqueTriplets(unittest.TestCase):
    def test_three_sum_unique_triplets(self):
        self.assertEqual(
            three_sum_unique_triplets([-1,0,1,2,-1,-4], 0),
            [[-1,-1,2],[-1,0,1]]
        )
        self.assertEqual(
            three_sum_unique_triplets([0,1,1], 2),
            [[0,1,1]]
        )
        self.assertEqual(
            three_sum_unique_triplets([0,0,0], 0),
            [[0,0,0]]
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    nums = [int(x) for x in input().split()]
    target = int(input())
    res = three_sum_unique_triplets(nums, target)
    for row in res:
        print(" ".join(map(str, row)))