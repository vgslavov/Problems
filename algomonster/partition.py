#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: backtracking, dfs

def ispalindrome(s: str) -> bool:
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True

# solution: AlgoMonster backtracking
# complexity:
# run-time: O(n * 2^n) where n is length of string s
# space: O(n) for recursion stack
# TODO: understand better
def partition(s: str) -> list[list[str]]:
    def backtrack(start_index, path):
        if start_index == len(s):
            ans.append(path[:])
            return

        for end in range(start_index+1, len(s)+1):
            prefix = s[start_index:end]
            #print(f"prefix:{prefix}")

            if not ispalindrome(prefix):
                continue

            # no need to pop since we create a new list
            backtrack(end, path+[prefix])

    ans = []
    backtrack(0, [])
    return ans

class TestPartition(unittest.TestCase):
    
    def test_partition(self):
        self.assertEqual(partition("aab"), [["a","a","b"],["aa","b"]])
        self.assertEqual(partition("a"), [["a"]])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    s = input()
    res = partition(s)
    for row in res:
        print(" ".join(row))