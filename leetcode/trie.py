#!/usr/bin/env python3

import sys
import unittest

# number: 208
# section: trie (prefix tree)
# difficulty: medium
# tags: hash table, string, design, trie, top 150, citadel

# constraints
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

# complexity
# run-time: O(n)
# space: O(n*m)
class Trie:

    def __init__(self):
        self.children = {}
        self.isendword = False

    def insert(self, word: str) -> None:
        node = self

        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]

        node.isendword = True

    def search(self, word: str) -> bool:
        return self.__search_helper(word, True)

    def starts_with(self, prefix: str) -> bool:
        return self.__search_helper(prefix)

    def __search_helper(self, word: str, check_end_word=False) -> bool:
        node = self

        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        return True if not check_end_word or node.isendword else False

class TestTrie(unittest.TestCase):
    def test(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.starts_with("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))

if __name__ == '__main__':
    sys.exit(unittest.main())
