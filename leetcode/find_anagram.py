#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 438
# similar: 567
# section: meta
# difficulty: medium
# tags: hash table, string, sliding window, meta

# constraints
# 1 <= s.length, p.length <= 3 * 10^4
# s and p consist of lowercase English letters.

# solution: LeetCode solution, sliding window + defaultdict
# complexity
# run-time: O(n^2)
# space: O(1) (only 26 letters per dict)
def findAnagrams(s: str, p: str) -> list[int]:
    if len(p) > len(s):
        return []
    
    pmap = defaultdict(int)
    
    for c in p:
        pmap[c] += 1
        
    # sliding window counter
    winmap = defaultdict(int)
    left = 0
    ans = []

    for right in range(len(s)):
        winmap[s[right]] += 1
        
        # window is smaller than p
        if right-left+1 < len(p):
            continue
            
        # check if the current window is a permutation of p
        if pmap == winmap:
            ans.append(left)
        
        # remove the leftmost character from the window
        if winmap[s[left]] > 1:
            winmap[s[left]] -= 1
        else:
            del winmap[s[left]]
            
        # slide the window
        left += 1
            
    return ans

class TestFindAnagram(unittest.TestCase):
    def test_empty(self):
        s = ""
        p = ""
        expected = []
        self.assertEqual(findAnagrams(s, p), expected)

    def test_1(self):
        s = "cbaebabacd"
        p = "abc"
        expected = [0, 6]
        self.assertEqual(findAnagrams(s, p), expected)

    def test_2(self):
        s = "abab"
        p = "ab"
        expected = [0, 1, 2]
        self.assertEqual(findAnagrams(s, p), expected)

if __name__ == "__main__":
    sys.exit(unittest.main())