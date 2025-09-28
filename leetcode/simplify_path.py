#!/usr/bin/env python3

import sys
import unittest

# number: 71
# title: Simplify Path
# url: https://leetcode.com/problems/simplify-path/
# section: stack
# difficulty: medium
# tags: string, stack, top 150, meta, me, citadel

# constraints
# 1 <= path.length <= 3000
# path consists of English letters, digits, period '.', slash '/' or '_'.
# path is a valid absolute Unix path.

# solution: stack
# complexity
# run-time: O(n)
# space: O(n)
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

# solution: LeetCode stack
# complexity
# run-time: O(n)
# space: O(n)
def simplify_path2(path, stack=None):
    if not path:
        return ''

    stack = [] if stack is None else stack

    # split by / to get rid of duplicate /
    for dir in path.split('/'):
        # current dir or empty dir
        if not dir or dir == '.':
            continue
        # parent dir
        elif dir == '..':
            # pop if not empty
            if stack:
                stack.pop()
        # keep adding
        else:
            stack.append(dir)

    return '/' + '/'.join(stack)

# solution: stack
# complexity
# run-time: O(n)
# space: O(n)
def cd(path, dir):
    # cd to an absolute path
    if dir and dir[0] == '/':
        return simplify_path2(dir)

    # cd to a relative path
    stack = [ p for p in path.split('/') if p ]
    return simplify_path2(dir, stack)

class TestSimplifyPath(unittest.TestCase):

    def test_empty(self):
        path = ''
        expected = path
        self.assertEqual(simplify_path(path), expected)
        self.assertEqual(simplify_path2(path), expected)

    def test_trailslash(self):
        path = '/home/'
        expected = '/home'
        self.assertEqual(simplify_path(path), expected)
        self.assertEqual(simplify_path2(path), expected)

    def test_2dots(self):
        path = '/../'
        expected = '/'
        self.assertEqual(simplify_path(path), expected)
        self.assertEqual(simplify_path2(path), expected)

    def test_2dots2(self):
        path = "/home/user/Documents/../Pictures"
        expected = "/home/user/Pictures"
        self.assertEqual(simplify_path(path), expected)
        self.assertEqual(simplify_path2(path), expected)

    def test_doubleslash(self):
        path = '/home//foo/'
        expected = '/home/foo'
        self.assertEqual(simplify_path(path), expected)
        self.assertEqual(simplify_path2(path), expected)

    def test_2dots2dots(self):
        path = '/a/./b/../../c/'
        expected = '/c'
        self.assertEqual(simplify_path(path), expected)
        self.assertEqual(simplify_path2(path), expected)

    def test_2dots2dots2dots(self):
        path = '/home/../../..'
        expected = '/'
        self.assertEqual(simplify_path(path), expected)
        self.assertEqual(simplify_path2(path), expected)

    def test_3dots(self):
        path = '/...'
        expected = '/...'
        self.assertEqual(simplify_path(path), expected)
        self.assertEqual(simplify_path2(path), expected)

    def test_3dots2dots2dots(self):
        path = "/.../a/../b/c/../d/./"
        expected = "/.../b/d"
        self.assertEqual(simplify_path(path), expected)
        self.assertEqual(simplify_path2(path), expected)

    def test_abcd(self):
        path = '/a//b////c/d//././/..'
        expected = '/a/b/c'
        self.assertEqual(simplify_path(path), expected)
        self.assertEqual(simplify_path2(path), expected)

    def test_cd_absolute(self):
        path = '/a/b/c/d'
        dir = '/x/y/z'
        expected = '/x/y/z'
        self.assertEqual(cd(path, dir), expected)

    def test_cd_relative(self):
        path = '/a/b/c/d'
        dir = 'x/y/z'
        expected = '/a/b/c/d/x/y/z'
        self.assertEqual(cd(path, dir), expected)

    def test_cd_relative2(self):
        path = '/a/b/c/d'
        dir = '../x/y/z'
        expected = '/a/b/c/x/y/z'
        self.assertEqual(cd(path, dir), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
