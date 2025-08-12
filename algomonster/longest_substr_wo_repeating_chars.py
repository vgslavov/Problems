#!/usr/bin/env python3

from collections import defaultdict
import argparse
import sys
import unittest

# tags: sliding window, longest

# solution: sliding window + dict
# complexity
# run-time: O(n)
# space: O(n)
def longest_substring_wo_repeating_characters2(s: str) -> int:
    left = 0
    ans = 0
    curr_win = defaultdict(int)

    for right in range(len(s)):
        if not s[right] in curr_win:
            curr_win[s[right]] = right
            ans = max(ans, len(curr_win))
            continue

        left = curr_win[s[right]]
        curr_win[s[right]] = right
        ans = max(ans, len(curr_win))
        
        for k in list(curr_win.keys()):
            if curr_win[k] <= left:
                del curr_win[k]

    #print(f"curr_win:{curr_win}")
    
    return ans

# solution: simpler sliding window + dict
# complexity
# run-time: O(n)
# space: O(n)
def longest_substring_wo_repeating_characters(s: str) -> int:
    left = 0
    ans = 0
    curr_win = defaultdict(int)

    for right in range(len(s)):
        curr_win[s[right]] += 1

        # loop of 1 :)
        while curr_win[s[right]] > 1:
            curr_win[s[left]] -= 1
            left += 1

        ans = max(ans, right-left+1)
    
    return ans

class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(longest_substring_wo_repeating_characters(""), 0)

    def test_1(self):
        self.assertEqual(longest_substring_wo_repeating_characters("abcabcbb"), 3)

    def test_2(self):
        self.assertEqual(longest_substring_wo_repeating_characters("bbbbb"), 1)

    def test_3(self):
        self.assertEqual(longest_substring_wo_repeating_characters("pwwkew"), 3)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    s = input()
    res = longest_substring_wo_repeating_characters(s)
    print(res)