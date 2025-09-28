#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: backtracking, dfs

# solution: backtracking
# complexity:
# run-time: O(n * n!) where n is length of input string letters
# space: O(n) for recursion stack
def permutations(letters: str) -> list[str]:
    def backtrack(path):
        # base case
        if len(path) == len(letters):
            ans.append(''.join(path))
            return

        for c in letters:
            if c in path:
                continue

            path.append(c)
            backtrack(path)
            path.pop()

    ans = []
    backtrack([])
    return ans

# solution: AlgoMonster backtracking
# complexity:
# run-time: O(n * n!) where n is length of input string letters
# space: O(n) for recursion stack
# TODO: understand better
def permutations2(letters: str) -> list[str]:
    def backtrack(start_index, path):
        # base case
        if start_index == len(letters):
            ans.append(''.join(path))
            return

        for i, c in enumerate(letters):
            # skip
            if used[i]:
                continue

            # add to permutation, mark used
            path.append(c)
            used[i] = True

            # recurse
            backtrack(start_index+1, path)

            # revert
            path.pop()
            # unmark
            used[i] = False

    ans = []
    used = [False] * len(letters)
    backtrack(0, [])
    return ans

class TestPermutations(unittest.TestCase):
    
    def test_permutations(self):
        self.assertEqual(sorted(permutations("abc")), sorted(["abc","acb","bac","bca","cab","cba"]))
        self.assertEqual(sorted(permutations2("abc")), sorted(["abc","acb","bac","bca","cab","cba"]))

        self.assertEqual(permutations("a"), ["a"])
        self.assertEqual(permutations2("a"), ["a"])

        self.assertEqual(permutations(""), [""])
        self.assertEqual(permutations2(""), [""])

        self.assertEqual(permutations("ab"), ["ab", "ba"])
        self.assertEqual(permutations2("ab"), ["ab", "ba"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    letters = input()
    res = permutations(letters)
    for line in sorted(res):
        print(line)