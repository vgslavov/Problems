#!/usr/bin/env python3

import argparse
from collections import defaultdict
import math
import sys
import unittest

# tags: sliding window

# solution: sliding window, shortest
# complexity:
# run-time: O(n)
# space: O(n)
def least_consecutive_cards_to_match(cards: list[int]) -> int:
    left = 0
    curr_win = defaultdict(int)
    ans = math.inf

    for right in range(len(cards)):
        curr_win[cards[right]] += 1

        while curr_win[cards[right]] > 1:
            ans = min(ans, right-left+1)
            curr_win[cards[left]] -= 1
            if not curr_win[cards[left]]:
                del curr_win[cards[left]]

            left += 1
        
    return ans if ans != math.inf else -1

class TestLeastConsecutiveCardsToMatch(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(least_consecutive_cards_to_match([]), -1)

    def test_1(self):
        self.assertEqual(least_consecutive_cards_to_match([1, 2, 3, 1]), 4)

    def test_2(self):
        self.assertEqual(least_consecutive_cards_to_match([1, 2, 3, 4]), -1)

    def test_3(self):
        self.assertEqual(least_consecutive_cards_to_match([1, 2, 1, 2, 1]), 3)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    cards = [int(x) for x in input().split()]
    res = least_consecutive_cards_to_match(cards)
    print(res)