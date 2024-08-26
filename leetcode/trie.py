#!/usr/bin/env python3

import sys
import unittest

# number: 208
# section: trie (prefix tree)
# difficulty: medium
# tags: hash table, string, design, trie, top 150

# constraints
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

# complexity
# run-time: O(n)?
# space: O(n)?
class Trie:

    def __init__(self):
        self.isendword = False
        self.children = {}

    def insert(self, word: str) -> None:
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]

        curr.isendword = True

    def search(self, word: str) -> bool:
        node = self

        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        return True if node.isendword else False

    def startsWith(self, prefix: str) -> bool:
        node = self

        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]

        return True

class TestTrie(unittest.TestCase):
    def test(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))

if __name__ == '__main__':
    sys.exit(unittest.main())
