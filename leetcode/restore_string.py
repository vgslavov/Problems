#!/usr/bin/env python3

import sys
import unittest

# number: ?
# section: assessment
# difficulty: easy
# tags: meta

# constraints
# s.length == indices.length == n
# 1 <= n <= 100
# s consists of only lowercase English letters.
# 0 <= indices[i] < n
# All values of indices are unique.

# complexity
# run-time: O(n*log n)
# space: O(n)
def restore_string(s, indices):
    d = {}

    for i in range(len(indices)):
        d[indices[i]] = s[i]

    return ''.join([d[key] for key in sorted(d.keys())])

class TestRestoreString(unittest.TestCase):
    def test_empty(self):
        s = ""
        indices = []
        expected = ""
        self.assertEqual(restore_string(s, indices), expected)

    def test_codeleet(self):
        s = "codeleet"
        indices = [4,5,6,7,0,2,1,3]
        expected = "leetcode"
        self.assertEqual(restore_string(s, indices), expected)

    def test_abc(self):
        s = "abc"
        indices = [0,1,2]
        expected = "abc"
        self.assertEqual(restore_string(s, indices), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
