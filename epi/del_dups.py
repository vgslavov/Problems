#!/usr/bin/env python

import unittest

# EPI 6.5

# time: O(n)
# space: O(1)
def del_dups(snums):

    if not snums:
        return None

    if len(snums) == 1:
        return snums

    # index for writing
    w = 1
    for i in range(1, len(snums)):
        # not sorted
        if snums[w-1] > snums[i]:
            raise ValueError
        elif snums[w-1] != snums[i]:
            snums[w] = snums[i]
            w += 1

    return snums[:w]

# time: O(n)
# space: O(n)
def del_dups2(snums):

    if not snums:
        return None

    if len(snums) == 1:
        return snums

    # TODO: raise during list comprehension?
    for i in range(1, len(snums)):
        if snums[i] < snums[i-1]:
            raise ValueError

    dedup = {num for num in snums}

    return [k for k in dedup]

class TestDelDups(unittest.TestCase):

    def test_empty(self):
        self.assertIsNone(del_dups([]), None)

    def test_none(self):
        self.assertIsNone(del_dups(None), None)

    def test_one(self):
        self.assertEqual(del_dups([1]), [1])

    def test_notsorted(self):
        self.assertRaises(ValueError, del_dups, [3, 2, 5])

    def test_dups_2(self):
        self.assertEqual(del_dups([1, 2, 2, 3]), [1, 2, 3])

    def test_dups_4(self):
        self.assertEqual(del_dups([1, 2, 2, 2, 2, 3]), [1, 2, 3])

    def test_dups_n(self):
        self.assertEqual(del_dups([1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4]), [1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()
