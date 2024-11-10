#!/usr/bin/env python3

import sys
import unittest

# number: 1268
# section: citadel
# difficulty: medium
# tags: array, string, binary search, trie, sorting, heap, prio queue, citadel

# constraints
# n: len(products)
# m: len(searchWord)
# 1 <= n <= 1000
# 1 <= len(products[i]) <= 3000
# 1 <= sum(len(products[i])) <= 2 * 10^4
# All the strings of products are unique.
# products[i] consists of lowercase English letters.
# 1 <= m <= 1000
# searchWord consists of lowercase English letters.

def check(item, pattern):
    return True if item[:len(pattern)] >= pattern else False

# duplicates, return left-most
def binary_search(products, prefix):
    left = 0
    right = len(products)

    while left < right:
        mid = left + (right-left)//2

        if check(products[mid], prefix):
            right = mid
        else:
            left = mid+1

    return left

# solution: binary search
# complexity
# run-time: O(n*log n + m*log n)
# space: O(1)
def suggested_products(products, word):
    ans = []
    prefix = ""
    k = 3

    # O(n*log n)
    products.sort()
    #print(f"products:{products}")

    # O(m)
    for c in word:
        prefix += c
        #print(f"prefix:{prefix}")

        # O(log n)
        left = binary_search(products, prefix)
        #print(f"left:{left}")

        sub_ans = []

        # left+k!
        for i in range(left, min(len(products), left+k)):
            # stop at words which don't match prefix
            if prefix != products[i][:len(prefix)]:
                break
            sub_ans.append(products[i])

        ans.append(sub_ans)

    return ans

class TestSuggestedProducts(unittest.TestCase):
    def test_empty(self):
        products = []
        word = ""
        expected = []
        self.assertEqual(suggested_products(products, word), expected)

    def test1(self):
        products = ["mobile","mouse","moneypot","monitor","mousepad"]
        word = "mouse"
        expected = [["mobile","moneypot","monitor"],
                    ["mobile","moneypot","monitor"],
                    ["mouse","mousepad"],
                    ["mouse","mousepad"],
                    ["mouse","mousepad"]]
        self.assertEqual(suggested_products(products, word), expected)

    def test2(self):
        products = ["havana"]
        word = "havana"
        expected = [["havana"],["havana"],["havana"],["havana"],["havana"],
                    ["havana"]]
        self.assertEqual(suggested_products(products, word), expected)

    def test3(self):
        products = ["bags","baggage","banner","box","cloths"]
        word = "bags"
        expected = [["baggage","bags","banner"],["baggage","bags","banner"],
                    ["baggage","bags"],["bags"]]
        self.assertEqual(suggested_products(products, word), expected)


if __name__ == '__main__':
    sys.exit(unittest.main())
