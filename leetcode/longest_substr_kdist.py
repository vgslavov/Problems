#!/usr/bin/env python3

from collections import defaultdict
import math
import sys
import unittest

# number: 340
# title: Longest Substring with At Most K Distinct Characters
# url: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# difficulty: medium
# tags: hash table, string, sliding window

# constraints:
# 1 <= s.length <= 5 * 10^4
# 0 <= k <= 50

# solution: sliding window
# complexity:
# run-time: O(n)
# space: O(k)
def longest_substr_kdist(s: str, k: int) -> int:
    if not len(s) or k == 0:
        return 0
    elif k >= len(s):
        return len(s)

    left = 0
    # or use Counter
    counts = defaultdict(int)
    ans = -math.inf

    for right in range(len(s)):
        counts[s[right]] += 1

        while len(counts) > k:
            if counts[s[left]] > 1:
                counts[s[left]] -= 1
            else:
                del counts[s[left]]

            left += 1

        ans = max(ans, right-left+1)

    return ans

class TestLongestSubstrKDist(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_substr_kdist("eceba", 2), 3)  # "ece" or "ba"
        self.assertEqual(longest_substr_kdist("aa", 1), 2)      # "aa"

    def test_edge_cases(self):
        self.assertEqual(longest_substr_kdist("", 0), 0)        # empty string
        self.assertEqual(longest_substr_kdist("a", 1), 1)       # single character
        self.assertEqual(longest_substr_kdist("aabbcc", 3), 6) # all characters are distinct
        self.assertEqual(longest_substr_kdist("aabbcc", 2), 4) # "aabb" or "bbcc"
        self.assertEqual(longest_substr_kdist("abcde", 5), 5)   # all characters are distinct
        self.assertEqual(longest_substr_kdist("abcde", 1), 1)   # only one character allowed

if __name__ == "__main__":
    sys.exit(unittest.main())