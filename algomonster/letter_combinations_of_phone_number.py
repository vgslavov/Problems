#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: backtracking, dfs

digit2letters = {
    0: [],
    1: [],
    2: ['a','b','c'],
    3: ['d','e','f'],
    4: ['g','h','i'],
    5: ['j','k','l'],
    6: ['m','n','o'],
    7: ['p','q','r','s'],
    8: ['t','u','v'],
    9: ['w','x','y','z']
}

# solution: AlgoMonster basic backtracking
# complexity:
# run-time: O(4^n * n) max of 4 choices per digit, n digits, O(n) to join
# space: O(4^n * n), O(4^n) strings, O(n) for path
def letter_combinations_of_phone_number(digits: str) -> list[str]:
    def dfs(start_index, path):
        # base case
        if len(path) == len(digits):
            ans.append(''.join(path))
            return

        digit = int(digits[start_index])
        
        # go over letters per digit
        for c in digit2letters[digit]:
            if c in path:
                continue

            path.append(c)
            dfs(start_index+1, path)
            # to avoid having to clear
            path.pop()

    ans = []
    dfs(0, [])
    return ans

class TestLetterCombinationsOfPhoneNumber(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(letter_combinations_of_phone_number("23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"])
        self.assertEqual(letter_combinations_of_phone_number(""), [''])
        self.assertEqual(letter_combinations_of_phone_number("2"), ["a","b","c"])
        self.assertEqual(letter_combinations_of_phone_number("56"), ["jm","jn","jo","km","kn","ko","lm","ln","lo"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    digits = input()
    res = letter_combinations_of_phone_number(digits)
    print(" ".join(res))