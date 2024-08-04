#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 49
# section: hashmap
# difficulty: medium
# tags: array, hash table, string, sorting, top 150

# constraints
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# complexity
# run-time: O(n * k * log(k))
# space: O(n * k)
def group_anagrams(strs):
    d = defaultdict(list)

    for i in range(len(strs)):
        ss = ''.join(sorted(strs[i]))
        d[ss].append(i)

    ans = []
    for v in d.values():
        ans.append([strs[i] for i in v])

    return ans

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
