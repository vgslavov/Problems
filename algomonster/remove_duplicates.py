#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: two pointers

# solution: two pointers, fast & slow, same direction
# complexity:
# run-time: O(n)
# space: O(1)
def remove_duplicates(arr: list[int]) -> int:
    slow, fast = 0, 0

    while fast < len(arr):
        # only advance slow pointer if we find a new unique element
        if arr[slow] != arr[fast]:
            # advance *before* assigning to avoid overwriting
            slow += 1
            # overwrite duplicate element
            arr[slow] = arr[fast]

        # *always* advance fast pointer
        fast += 1

    # length is index + 1
    return slow+1

class TestRemoveDuplicates(unittest.TestCase):
    def test_example_1(self):
        arr = [1, 1, 2]
        self.assertEqual(remove_duplicates(arr), 2)
        self.assertEqual(arr[:2], [1, 2])
        
    def test_example_2(self):
        arr = [0, 0, 1, 1, 1, 2, 2]
        self.assertEqual(remove_duplicates(arr), 3)
        self.assertEqual(arr[:3], [0, 1, 2])

    def test_example_3(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(remove_duplicates(arr), 5)
        self.assertEqual(arr[:5], [1, 2, 3, 4, 5])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    arr = [int(x) for x in input().split()]
    res = remove_duplicates(arr)
    print(" ".join(map(str, arr[:res])))