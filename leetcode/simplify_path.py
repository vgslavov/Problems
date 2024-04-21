#!/usr/bin/env python3

import sys
import unittest

# 1 <= path.length <= 3000
# path consists of English letters, digits, period '.', slash '/' or '_'.
# path is a valid absolute Unix path.
def simplify_path(path):
    if not path:
        return ''

    s = []
    sub = ''

    for c in path:
        if c == '/':
            if sub == '.' or sub == '':
                sub = ''
                continue
            elif sub == '..':
                if not s:
                    sub = ''
                    continue
                else:
                    s.pop()
            else:
                s.append(sub)

            sub = ''
        else:
            sub += c

    if s and sub == '..':
        s.pop()
    elif sub and sub not in ('.', '..'):
        s.append(sub)

    return '/' + '/'.join(s)

# TODO: refactor, ugly!

class TestSimplifyPath(unittest.TestCase):

    def test_empty(self):
        path = ''
        expected = path
        self.assertEqual(simplify_path(path), expected)

    def test_trailslash(self):
        path = '/home/'
        expected = '/home'
        self.assertEqual(simplify_path(path), expected)

    def test_2dots(self):
        path = '/../'
        expected = '/'
        self.assertEqual(simplify_path(path), expected)

    def test_doubleslash(self):
        path = '/home//foo/'
        expected = '/home/foo'
        self.assertEqual(simplify_path(path), expected)

    def test_2dots2dots(self):
        path = '/a/./b/../../c/'
        expected = '/c'
        self.assertEqual(simplify_path(path), expected)

    def test_2dots2dots2dots(self):
        path = '/home/../../..'
        expected = '/'
        self.assertEqual(simplify_path(path), expected)

    def test_3dots(self):
        path = '/...'
        expected = '/...'
        self.assertEqual(simplify_path(path), expected)

    def test_abcd(self):
        path = '/a//b////c/d//././/..'
        expected = '/a/b/c'
        self.assertEqual(simplify_path(path), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
