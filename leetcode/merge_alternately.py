#!/usr/bin/env python3

import sys
import unittest

# number: 1768
# title: Merge Strings Alternately
# url: https://leetcode.com/problems/merge-strings-alternately/
# difficulty: easy
# tags: two pointers, string

# constraints:
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

# solution: two pointers
# complexity
# run-time: O(n+m)
# space: O(n+m)
def merge_alternately(word1: str, word2: str) -> str:
    i = j = 0
    alternate = True
    ans = []

    while i < len(word1) and j < len(word2):
        if alternate:
            ans.append(word1[i])
            i += 1
        else:
            ans.append(word2[j])
            j += 1

        alternate = not alternate

    if i < len(word1):
        ans.extend(word1[i:])
    else:
        ans.extend(word2[j:])

    return ''.join(ans)

if __name__ == '__main__':
    sys.exit(unittest.main())