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
        node.__freq += 1

        for c in word:
            if c not in node.__children:
                node.__children[c] = Trie()
                
            node = node.__children[c]
            node.__freq += 1

    def search(self, word):
        node = self
        count = 0

        for c in word:
            # no more words with this prefix
            if c not in node.__children or node.__freq == 1:
                break

            node = node.__children[c]
            count += 1

        return count

# non-solution: trie
# complexity:
# run-time: O(n * m) where n is number of words and m is average length of words
# space: O(n * m) for trie storage
# TODO: WIP
def autocomplete(words: list[str]) -> int:
    trie = Trie()
    ans = 0

    for w in words:
        trie.insert(w)

    for w in words:
        ans += trie.search(w)
    
    return ans

class TestAutocomplete(unittest.TestCase):
    
    def test_autocomplete(self):
        self.assertEqual(autocomplete(["go", "gone", "guild"]), 7)
        self.assertEqual(autocomplete(["abc", "ab", "bc"]), 5)
        self.assertEqual(autocomplete(["a", "b", "c"]), 3)
        self.assertEqual(autocomplete(["a", "aa", "aaa"]), 6)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    words = input().split()
    res = autocomplete(words)
    print(res)