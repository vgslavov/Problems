#!/usr/bin/env python3

import sys
import unittest

# number: 412
# section: citadel
# difficulty: easy
# tags: math, string, simulation, citadel

# constraints
# 1 <= n <= 10^4

# complexity
# run-time: O(n)
# space: O(1)
def fizz_buzz(n: int) -> []:
    ans = []

    for i in range(1, n+1):
        mod3 = i % 3
        mod5 = i % 5

        if not mod3 and not mod5:
            ans.append("FizzBuzz")
        elif not mod3:
            ans.append("Fizz")
        elif not mod5:
            ans.append("Buzz")
        else:
            ans.append(str(i))

    return ans

class TestFizzBuzz(unittest.TestCase):
    def test_empty(self):
        n = 0
        expected = []
        self.assertEqual(fizz_buzz(n), expected)

    def test3(self):
        n = 3
        expected = ["1","2","Fizz"]
        self.assertEqual(fizz_buzz(n), expected)

    def test5(self):
        n = 5
        expected = ["1","2","Fizz","4","Buzz"]
        self.assertEqual(fizz_buzz(n), expected)

    def test15(self):
        n = 15
        expected = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz",
                    "11","Fizz","13","14","FizzBuzz"]
        self.assertEqual(fizz_buzz(n), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
