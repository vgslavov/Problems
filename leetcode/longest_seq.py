#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 128
# section: hashmap
# difficulty: medium
# tags: array, hash table, union find, top 150

# constraints
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

# solution: sort
# complexity
# run-time: O(n log n)
# space: O(1)
def longest_seq(nums):
    if not nums:
        return 0

    nums.sort()
    #print(f"sorted:{nums}")

    # at least 1 match
    ans = count = 1
    for i in range(1, len(nums)):
        if (nums[i-1] + 1) == nums[i]:
            count += 1
            ans = max(ans, count)
        else:
            count = 1

    return ans

# solution: defaultdict
# complexity
# run-time: O(n+k)
# space: O(k)
# TODO: fix bugs, attempted
def longest_seq2(nums):
    if not nums:
        return 0

    counts = defaultdict(int)

    for n in nums:
        counts[n] += 1

    for k,v in counts.items():
        if not v:
            continue
        elif k-1 not in counts and k+1 not in counts:
            counts[k] = 0

    #print("counts:{}".format(counts))

    nonzero = sum(1 for k in counts.keys() if counts[k])

    return nonzero if nonzero else 1

class TestLongestSeq(unittest.TestCase):

    def test_empty(self):
        nums = None
        expected = 0
        self.assertEqual(longest_seq(nums), expected)
        self.assertEqual(longest_seq2(nums), expected)

    def test_1(self):
        nums = [100,4,200,1,3,2]
        expected = 4
        self.assertEqual(longest_seq(nums), expected)
        self.assertEqual(longest_seq2(nums), expected)

    def test_2(self):
        nums = [0,3,7,2,5,8,4,6,0,1]
        expected = 9
        self.assertEqual(longest_seq(nums), expected)
        self.assertEqual(longest_seq2(nums), expected)

    def test_3(self):
        nums = [0]
        expected = 1
        self.assertEqual(longest_seq(nums), expected)
        self.assertEqual(longest_seq2(nums), expected)

    def test_4(self):
        nums = [0,0]
        expected = 1
        self.assertEqual(longest_seq(nums), expected)
        self.assertEqual(longest_seq2(nums), expected)

    def test_5(self):
        nums = [0,0]
        expected = 1
        self.assertEqual(longest_seq(nums), expected)
        self.assertEqual(longest_seq2(nums), expected)

    def test_6(self):
        nums = [9,1,4,7,3,-1,0,5,8,-1,6]
        expected = 7
        self.assertEqual(longest_seq(nums), expected)
        # TODO: counting multiple sequences
        #self.assertEqual(longest_seq2(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
