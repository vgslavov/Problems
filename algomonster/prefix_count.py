#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: trie

class Trie:
    def __init__(self):
        self.__children = {}
        self.__freq = 0

    def insert(self, word):
        node = self

        for c in word:
            if c not in node.__children:
                node.__children[c] = Trie()

            node = node.__children[c]
            node.__freq += 1

    def search(self, word):
        node = self

        for c in word:
            if c not in node.__children:
                return 0

            node = node.__children[c]

        return node.__freq

# solution: trie
# complexity:
# run-time: O(n * m)
# space: O(n * m)
def prefix_count(words: list[str], prefixes: list[str]) -> list[int]:
    trie = Trie()
    ans = []

    # build trie: O(n * m)
    # where n is number of words and m is average word length
    for w in words:
        trie.insert(w)

    # search prefixes: O(p * k)
    # where p is number of prefixes and k is average prefix length
    for p in prefixes:
        ans.append(trie.search(p))
        
    return ans

class TestPrefixCount(unittest.TestCase):
    
    def test_prefix_count(self):
        self.assertEqual(prefix_count(["go", "gone", "guild"], ["go", "gon", "g"]), [2, 1, 3])
        self.assertEqual(prefix_count(["abc", "ab", "bc"], ["a", "b", "c"]), [2, 1, 0])
        self.assertEqual(prefix_count(["a", "b", "c"], ["a", "b", "c"]), [1, 1, 1])
        self.assertEqual(prefix_count(["a", "aa", "aaa"], ["a", "aa", "aaa"]), [3, 2, 1])
        self.assertEqual(prefix_count(["forgot", "for", "algomonster", "while"], ["for", "forg", "algo"]), [2, 1, 1])
        self.assertEqual(prefix_count(["brother", "mother", "father", "contest", "compare", "stick", "reverse", "tree", "brave", "revere"], ["ther", "her", "bro", "reve", "rever", "revere", "reverse", "test"]), [0, 0, 1, 2, 2, 1, 1, 0])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    words = input().split()
    prefixes = input().split()
    res = prefix_count(words, prefixes)
    print(" ".join(map(str, res)))