#!/usr/bin/env python3

import sys
import unittest

# number: 1544
# title: Make The String Great
# url: https://leetcode.com/problems/make-the-string-great/
# section: string
# difficulty: easy
# tags: string, stack

# A good string is a string which doesn't have two adjacent characters s[i] and
# s[i + 1] where:
# * 0 <= i <= s.length - 2
# * s[i] is a lower-case letter and s[i + 1] is the same letter but in
#   upper-case or vice-versa.

# contraints:
# 1 <= s.length <= 100
# s contains only lower and upper case English letters.

def isbad(a, b):
    if a.isupper() and b.islower() and a == b.upper():
        return True
    elif b.isupper() and a.islower() and a.upper() == b:
        return True

    return False

# solution: stack
# complexity
# run-time: O(n)
# space: O(n)
def make_good(s):
    ans = []

    for c in s:
        if not ans:
            ans.append(c)
        elif isbad(c, ans[-1]):
            ans.pop()
            continue
        else:
            ans.append(c)

    return ''.join(ans)

class TestMakeGood(unittest.TestCase):
    def test_empty(self):
        s = ''
        expected = ''
        self.assertEqual(make_good(s), expected)

    def test_1(self):
        s = 'leEeetcode'
        expected = 'leetcode'
        self.assertEqual(make_good(s), expected)

    def test_2(self):
        s = 'abBAcC'
        expected = ''
        self.assertEqual(make_good(s), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
