#!/usr/bin/env python3

import argparse
from collections import defaultdict
import sys
import unittest

# leetcode: 438
# tags: sliding window

# solution: sliding window + defaultdict
# complexity:
# run-time: O(n)
# space:O(1)
def find_all_anagrams(original: str, check: str) -> list[int]:
    if len(check) > len(original):
        return []

    check_win = defaultdict(int)

    for c in check:
        check_win[c] += 1

    curr_win = defaultdict(int)
    left = 0
    ans = []

    for right in range(len(original)):
        curr_win[original[right]] += 1

        # compare to length of check, not check_win!
        if right-left+1 < len(check):
            continue

        if curr_win == check_win:
            ans.append(left)

        if curr_win[original[left]] > 1:
            curr_win[original[left]] -= 1
        else:
            del curr_win[original[left]]

        left += 1

    return ans

# TODO: use array of 26 chars

class TestFindAllAnagrams(unittest.TestCase):
    def test_empty(self):
        original = ""
        check = ""
        expected = []
        self.assertEqual(find_all_anagrams(original, check), expected)

    def test_1(self):
        original = "cbaebabacd"
        check = "abc"
        expected = [0, 6]
        self.assertEqual(find_all_anagrams(original, check), expected)

    def test_2(self):
        original = "abab"
        check = "ab"
        expected = [0, 1, 2]
        self.assertEqual(find_all_anagrams(original, check), expected)

    def test_3(self):
        original = "nabanabannaabbaanana"
        check = "banana"
        expected = [0, 3, 5, 6, 7, 13]
        self.assertEqual(find_all_anagrams(original, check), expected)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    original = input()
    check = input()
    res = find_all_anagrams(original, check)
    print(" ".join(map(str, res)))