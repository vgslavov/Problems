#!/usr/bin/env python3

import sys
import unittest

# number: 925
# title: Long Pressed Name
# url: https://leetcode.com/problems/long-pressed-name/
# section: assessments
# difficulty: easy
# tags: two pointers, string, google

# constraints
# 1 <= name.length, typed.length <= 1000
# name and typed consist of only lowercase English letters.

# solution: two pointers
# complexity
# run-time: O(n)
# space: O(1)
def islongpressedname(name: str, typed: str) -> bool:

    if not name or not typed or len(name) > len(typed):
        return False

    i = j = 0

    while i < len(name) and j < len(typed):
        if name[i] == typed[j]:
            i += 1
            j += 1
        elif i and name[i-1] == typed[j]:
            j += 1
        else:
            #print(f"1st, name:{name[i]},typed:{typed[j]}")
            return False

    if i < len(name):
        return False

    while j < len(typed):
        if i and name[i-1] == typed[j]:
            j+= 1
        else:
            #print(f"2nd, name:{name[i]},typed:{typed[j]}")
            return False

    return True

# TODO: solve using dict
# solution: dict
# complexity
# run-time: O(n)
# space: O(1)

# TODO: add unit tests
# Input: name = "alex", typed = "aaleex"
# Output: true

# Input: name = "saeed", typed = "ssaaedd"
# Output: false

if __name__ == '__main__':
    sys.exit(unittest.main())
