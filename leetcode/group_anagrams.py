#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 49
# title: Group Anagrams
# url: https://leetcode.com/problems/group-anagrams/
# section: hashmap
# difficulty: medium
# tags: array, hash table, string, sorting, top 150, meta, citadel

# constraints
# k: len(strs[i])
# n: len(strs)
# 1 <= n <= 10^4
# 0 <= k <= 100
# strs[i] consists of lowercase English letters.

# solution: dict + sort
# complexity
# run-time: O(n * k * log(k))
# space: O(n * k)
def group_anagrams(strs):
    d = defaultdict(list)

    for i in range(len(strs)):
        # sort each string
        ss = ''.join(sorted(strs[i]))
        # key: sorted str, value: list of original str
        d[ss].append(i)

    ans = []
    for v in d.values():
        ans.append([strs[i] for i in v])

    return ans

# TODO: faster?

class TestGroupAnagrams(unittest.TestCase):
    def test_empty(self):
        strs = [""]
        expected = [[""]]
        self.assertEqual(group_anagrams(strs), expected)

    def test_1(self):
        strs = ["a"]
        expected = [["a"]]
        self.assertEqual(group_anagrams(strs), expected)

    # order of expected doesn't matter
    def test_2(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        expected = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertEqual(group_anagrams(strs), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
