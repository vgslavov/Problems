#!/usr/bin/env python3

import sys
import unittest

# number: 17
# title: Letter Combinations of a Phone Number
# url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# section: backtracking
# difficulty: medium
# tags: string, backtracking, top 150, meta, grind 75, neetcode 150

# constraints
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
# return all possible letter combinations that the number could represent.
# return the answer in any order.

# solution: backtracking
# run-time: O(n*4^n), n is length of digits, 4 is max letters per digit
# space: O(n*4^n)
def letter_combinations(digits: str) -> list[str]:
    digit2str = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "prqs",
        8: "tuv",
        9: "wxyz"
    }

    def dfs(i, cur):
        # base case
        if not digits:
            return
        elif i == len(digits):
            ans.append(''.join(cur))
            return

        digit = int(digits[i])

        # recursion
        for c in digit2str[digit]:
            cur.append(c)
            dfs(i+1, cur)
            cur.pop()

    ans = []
    dfs(0, [])
    return ans

class TestLetterCombinations(unittest.TestCase):
    def test_example1(self):
        digits = "23"
        expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertCountEqual(letter_combinations(digits), expected)

    def test_example2(self):
        digits = ""
        expected = []
        self.assertCountEqual(letter_combinations(digits), expected)

    def test_example3(self):
        digits = "2"
        expected = ["a","b","c"]
        self.assertCountEqual(letter_combinations(digits), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())