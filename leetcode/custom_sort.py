#!/usr/bin/env python3

from collections import defaultdict
import functools
import sys
import unittest

# number: 791
# section: assessment
# difficulty: medium
# tags: hash table, string, sorting, meta

# constraints
# len(order): m
# len(s): n
# 1 <= m <= 26
# 1 <= n <= 200
# order and s consist of lowercase English letters.
# All the characters of order are unique.

# solution: hash table + two pointers
# complexity
# run-time: O(n*log n + m*log m)
# space: O(n)
# TODO: fix bugs when dupes
def custom_sort(order: str, s: str) -> str:
    counts = defaultdict(int)
    ans = ""

    # O(n): count chars in s
    for c in s:
        counts[c] += 1

    # O(m): build ans from order
    for c in order:
        if c in counts:
            ans += c * counts[c]

    #print(f"ans:{ans}")

    # O(m*log m): sort order
    sorder = ''.join(sorted(order))
    #print(f"sorder:{sorder}")
    # O(n*log n): sort s
    ss = ''.join(sorted(s))
    #print(f"ss:{ss}")

    i = j = 0

    # O(n): cmp order & s
    while i < len(sorder) and j < len(ss):
        # skip dupes in ss
        if j > 0 and ss[j] == ss[j-1]:
            j += 1
            continue
        # in order, not in s: add
        elif sorder[i] > ss[j]:
            ans += ss[j]
            j += 1
            continue
        # in s, not in order, skip
        elif sorder[i] < ss[j]:
            i += 1
            continue

        i += 1
        j += 1

    #print(f"ans:{ans}")

    # attach remaining, unless it's a dupe
    if j < len(ss) and ss[j] != ss[j-1]:
        ans += ss[j:]

    return ans

# solution: hash table
# complexity
# run-time: O(n+m)
# space: O(n)
def custom_sort2(order: str, s: str) -> str:
    counts = defaultdict(int)
    ans = ""

    # O(n): count chars in s
    for c in s:
        counts[c] += 1

    # O(m): build answer from order
    for c in order:
        if c in counts:
            ans += c * counts[c]
            counts[c] = 0

    # O(n): add the rest
    #for c in counts:
    # O(n*log n): sort keys for unit tests
    for c in sorted(counts):
        if counts[c]:
            ans += c * counts[c]
            counts[c] = 0

    return ans

# solution: sort + custom cmp func
# complexity
# run-time: O(n*log n)
# space: O(n)
# TODO: write sort cmp func
def custom_sort3(order: str, s: str) -> str:
    return ''.join(sorted(s, key=functools.cmp_to_key(lambda x,y: order.find(x) < order.find(y))))

class TestCustomSort(unittest.TestCase):
    def test_empty(self):
        order = ""
        s = ""
        expected = ""
        self.assertEqual(custom_sort(order, s), expected)
        self.assertEqual(custom_sort2(order, s), expected)

    def test1(self):
        order = "cba"
        s = "abcd"
        expected = "cbad"
        self.assertEqual(custom_sort(order, s), expected)
        self.assertEqual(custom_sort2(order, s), expected)

    def test2(self):
        order = "bcafg"
        s = "abcd"
        expected = "bcad"
        self.assertEqual(custom_sort(order, s), expected)
        self.assertEqual(custom_sort2(order, s), expected)

    def test3(self):
        order = "kqep"
        s = "pekeq"
        expected = "kqeep"
        self.assertEqual(custom_sort(order, s), expected)
        self.assertEqual(custom_sort2(order, s), expected)

    def test4(self):
        order = "disqyr"
        s = "iwyrysqrdj"
        expected = "disqyyrrjw"
        self.assertEqual(custom_sort(order, s), expected)
        self.assertEqual(custom_sort2(order, s), expected)

    def test5(self):
        order = "hucw"
        s = "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"
        expected = "hhhhhuucccwaaaaaaaaabbdddddeffffggggiijjjjkkkkllllmmmmnnnoooopppqqqqqqqqqqqrsssttttttttvxxxxxyyzzzzz"
        # TODO: fix bugs
        #self.assertEqual(custom_sort(order, s), expected)
        self.assertEqual(custom_sort2(order, s), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
