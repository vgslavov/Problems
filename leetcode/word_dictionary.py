#!/usr/bin/env python3

import sys
import unittest

# number: 211
# title: Add and Search Word - Data structure design
# url: https://leetcode.com/problems/add-and-search-word-data-structure-design/
# section: trie
# difficulty: medium
# tags: string, dfs, design, trie, top 150, meta

# contraints
# m: len(word)
# n: words
# 1 <= m <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 10^4 calls will be made to addWord and search.

# solution: Nursultan's LeetCode recursive dfs + trie
# complexity
# run-time: O(m)
# space: O(n*m)?
class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            # stop at length of word
            if i == len(word):
                return node.is_word

            c = word[i]

            if c == ".":
                # recursively go through all children when .
                for child in node.children:
                    if dfs(i+1, node.children[child]):
                        return True
            else:
                # recursively go through children of word's char only
                # not a loop!
                if c in node.children:
                    if dfs(i+1, node.children[c]):
                        return True

            return False

        return dfs(0, self.root)

# non-solution
class WordDictionaryBad:

    def __init__(self):
        self.children = {}
        self.is_word = False

    def addWord(self, word: str) -> None:
        print(f"adding: {word}")
        node = self

        for c in word:
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]

        # mark end
        node.is_word = True

        print(f"trie: {self}")

    def __search_node(self, word, node) -> bool:
        for i, c in enumerate(word):
            # found char match, continue
            if c in node.children:
                node = node.children[c]
            # not found, but .
            elif c == ".":
                for x in node.children:
                    # not end
                    if self.__search_node(word[i+1:], node.children[x]):
                        return True
            # not found
            else:
                return False

        return node.is_word

    def search(self, word: str) -> bool:
        return self.__search_node(word, self)

    def __repr__(self) -> str:
        return f"<WordDictionary children:{self.children}>"

    def __str__(self) -> str:
        return f"children is {self.children}"

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord(word)
param_2 = obj.search(word)
