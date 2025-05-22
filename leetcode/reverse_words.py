#!/usr/bin/env python3

from collections import deque
import sys
import unittest

# number: 151
# title: Reverse Words in a String
# url: https://leetcode.com/problems/reverse-words-in-a-string/
# section: array/string
# difficulty: medium
# tags: two pointers, string, top 150, leetcode 75

# constraints
# 1 <= s.length <= 10^4
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.

# solution: Pythonic & slow
# complexity
# run-time: O(n)
# space: O(n)
def reverse_words(s):
    ss = s.strip().split(" ")

    # can't use generator expression because of reverse()
    ans = [w.strip() for w in ss if w]
    ans.reverse()

    return ' '.join(ans)

# solution: deque
# complexity
# run-time: O(n), faster
# space: O(n)
def reverse_words2(s):
    w = ''
    # TODO: estimate size?
    q = deque()

    for i in range(len(s)):
        if s[i].isalnum():
            w += s[i]
        elif s[i].isspace():
            if not w:
                continue

            q.appendleft(w)
            w = ''
        else:
            print("invalid input={}".format(s[i]))

    if w:
        q.appendleft(w)

    return ' '.join(q)

# TODO: solve O(n) using two pointers

# Q: If the string data type is mutable in your language, can you solve
#    it in-place with O(1) extra space? 
# A: No, in Python strings are immutable

class TestReverseWords(unittest.TestCase):

    def test_empty(self):
        s = ''
        self.assertFalse(reverse_words(s))
        self.assertFalse(reverse_words2(s))

    def test1(self):
        s = "the sky is blue"
        expected = "blue is sky the"
        self.assertEqual(expected, reverse_words(s))
        self.assertEqual(expected, reverse_words2(s))

    def test2(self):
        s = "  hello world  "
        expected = "world hello"
        self.assertEqual(expected, reverse_words(s))
        self.assertEqual(expected, reverse_words2(s))

    def test3(self):
        s = "a good   example"
        expected = "example good a"
        self.assertEqual(expected, reverse_words(s))
        self.assertEqual(expected, reverse_words2(s))

    def test4(self):
        s = "EPY2giL"
        expected = s
        self.assertEqual(expected, reverse_words(s))
        self.assertEqual(expected, reverse_words2(s))

if __name__ == '__main__':
    sys.exit(unittest.main())
