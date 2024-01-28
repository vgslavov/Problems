#!/usr/bin/env python3

import sys
import unittest

# given:
# 3[a] = aaa
# 3[a]2[b] = aaabb
# 3[2[a]b] = aabaabaab

def decode(val):

    if not val:
        return ''

    stack = []
    num = 0
    substr = ''
    for c in val:
        print('c: {}'.format(c))
        print('stack: {}'.format(stack))

        # support multi-digit numbers
        if c.isdigit():
            num = (num * 10) + int(c)
        # char
        elif c.isalpha():
            substr += c
        # push to stack
        elif c == '[':
            stack.append((num, ''))
            num = 0
            print('stack (after [): {}\n'.format(stack))
        # pop from stack
        elif c == ']':
            n, e = stack.pop()
            if e:
                stack.append((n, e))
                stack.append((1, substr))
            else:
                stack.append((n, substr))
            substr = ''
            print('stack (after ]): {}\n'.format(stack))
        # n/a
        else:
            print(c)

        print('substr: {}'.format(substr))
        print('stack: {}\n'.format(stack))

    res = ''
    # don't iterate over an iterable you are changing
    while len(stack):
        n, s = stack.pop()
        if not s:
            res *= n
        else:
            res += (n * s)
        print('res: {}'.format(res))

    l = list(res)
    l.reverse()

    return ''.join(l)

class TestDecode(unittest.TestCase):

    def test_empty(self):
        s = ''
        self.assertEqual(decode(s), '')

    def test_simple(self):
        s = '3[a]'
        self.assertEqual(decode(s), 'aaa')

    def test_doubledigit(self):
        s = '12[a]'
        self.assertEqual(decode(s), 'aaaaaaaaaaaa')

    def test_multiple(self):
        s = '3[a]2[b]'
        self.assertEqual(decode(s), 'aaabb')

    def test_nested1(self):
        s = '3[2[x]z]'
        self.assertEqual(decode(s), 'xxzxxzxxz')

    def test_nested2(self):
        s = '2[l3[m]]'
        self.assertEqual(decode(s), 'lmmmlmmm')

if __name__ == '__main__':
    sys.exit(unittest.main())
