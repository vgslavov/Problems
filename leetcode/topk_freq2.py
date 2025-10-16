#!/usr/bin/env python3

from collections import defaultdict
import heapq
import sys
import unittest

# number: 692
# title: Top K Frequent Words
# url: https://leetcode.com/problems/top-k-frequent-words/

# constraints
# 1 <= words.length <= 500
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# k is in the range [1, The number of unique words[i]]
# Sort the words with the same frequency by their *lexicographical* order.

# solution: dict + max heap
# complexity
# run-time: O(n + u + k*log u) ~ O(n + k*log u) where u is unique and u <= n
# space: O(u+k) ~ O(u)
def topk_freq2(words: list[str], k: int) -> list[str]:
    freqs = defaultdict(int)

    # O(n)
    for w in words:
        freqs[w] += 1

    # O(u): max heap of (-count, word) to get lexicographical order
    heap = [(-c,w) for w,c in freqs.items()]

    # O(u)
    heapq.heapify(heap)

    # O(k*log u)
    return [heapq.heappop(heap)[1] for _ in range(k)]

# TODO: build min heap of size k
# (challenge: how to get lexicographical order?)
# run-time: O(n + u*log k) where u is unique
# space: O(u+k) ~ O(u)

class TestTopKFreq2(unittest.TestCase):
    def test_example1(self):
        words = ["i","love","leetcode","i","love","coding"]
        k = 2
        expected = ["i","love"]
        result = topk_freq2(words, k)
        self.assertEqual(result, expected)

    def test_example2(self):
        words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
        k = 4
        expected = ["the","is","sunny","day"]
        result = topk_freq2(words, k)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    sys.exit(unittest.main())