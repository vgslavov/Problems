#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 49
# title: Group Anagrams
# url: https://leetcode.com/problems/group-anagrams/
# section: hashmap
# difficulty: medium
# tags: array, hash table, string, sorting, top 150, meta, citadel, grind 75

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

    for s in strs:
        # normalize to lowercase for key; keep original in value
        ss = ''.join(sorted(s.lower()))
        d[ss].append(s)

    return list(d.values())

# solution: dict
# complexity
# run-time: O(n * k)
# space: O(k)
def group_anagrams2(strs):
    d = defaultdict(list)

    for s in strs:
        # const space
        counts = [0] * 26
        for c in s.lower():
            counts[ord(c) - ord('a')] += 1
        d[tuple(counts)].append(s)

    return list(d.values())

class TestGroupAnagrams(unittest.TestCase):
    def test_empty(self):
        strs = [""]
        expected = [[""]]
        self.assertEqual(group_anagrams(strs), expected)
        self.assertEqual(group_anagrams2(strs), expected)

    def test_1(self):
        strs = ["a"]
        expected = [["a"]]
        self.assertEqual(group_anagrams(strs), expected)
        self.assertEqual(group_anagrams2(strs), expected)

    # order of expected doesn't matter
    def test_2(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        expected = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertEqual(group_anagrams(strs), expected)
        self.assertEqual(group_anagrams2(strs), expected)

    def test_uppercase(self):
        # case-insensitive: normalize to lowercase for key, keep originals in groups
        strs = ["Eat", "eat", "tea"]
        expected = [["Eat", "eat", "tea"]]
        self.assertEqual(group_anagrams(strs), expected)
        self.assertEqual(group_anagrams2(strs), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
