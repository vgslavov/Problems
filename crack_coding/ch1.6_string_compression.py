#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# iterate
def compress1(s):
    if not s:
        return None

    result = ''
    count = 1
    for i in range(1, len(s)):
        # current duplicate
        if s[i] == s[i-1]:
            count += 1
        # previous duplicate
        elif count > 1:
            result = ''.join([result, s[i-1], str(count)])
            count = 1
        # no duplicate
        else:
            # TODO: join() instead?
            result += s[i-1]

        # last char
        if i == len(s)-1:
            # TODO: join() instead?
            result += s[i]
            if count > 1:
                # TODO: join() instead?
                result += str(count)

    return result

# TODO: use dict?
def compress2(s):
    if not s:
        return None

    # BF: combining same char at different position into same key
    d = defaultdict(int)
    for c in s:
        d[c] += 1

    return ''.join([k+(str(v) if v > 1 else '') for k,v in d.items()])

# TODO: use OrderedDict?
def compress3(s):
    pass

# TODO: use bitmap?
def compress4(s):
    pass

class TestStringCompression(unittest.TestCase):

    def test_empty(self):
        s = ''
        self.assertFalse(compress1(s))
        self.assertFalse(compress2(s))

    def test_nodupes(self):
        s = 'abcdefgh'
        self.assertEqual(compress1(s), s)
        self.assertEqual(compress2(s), s)

    def test_dupes_mid(self):
        s = 'hellobrooklyn'
        self.assertEqual(compress1(s), 'hel2obro2klyn')
        self.assertEqual(compress2(s), 'hel2obro2klyn')

    def test_dupes_start_end(self):
        s = 'aaabcdeeee'
        self.assertEqual(compress1(s), 'a3bcde4')
        self.assertEqual(compress2(s), 'a3bcde4')

if __name__ == '__main__':
    sys.exit(unittest.main())
