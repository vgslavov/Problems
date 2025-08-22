#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: backtracking

# solution: AlgoMonster backtracking basic
# complexity:
# run-time: O(2^n) nodes * O(n) to join = O(2^n*n)
# space: O(2^n) strings * O(n) total = O(2^n*n)
def letter_combination(n: int) -> list[str]:
    def dfs(start_index, path):
        # base case
        if start_index == n:
            ans.append(''.join(path))
            return
        
        for c in "ab":
            path.append(c)
            dfs(start_index + 1, path)
            path.pop()

    ans = []
    dfs(0, [])
    return ans

class TestLetterCombination(unittest.TestCase):
    def test_letter_combination(self):
        self.assertEqual(letter_combination(1), ['a', 'b'])
        self.assertEqual(letter_combination(2), ['aa', 'ab', 'ba', 'bb'])
        self.assertEqual(letter_combination(3), ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    n = int(input())
    res = letter_combination(n)
    for line in sorted(res):
        print(line)