#!/usr/bin/env python3

import re
import sys
import unittest

# number: 468
# section: meta
# difficulty: medium
# tags: string, meta

# constraints
# queryIP consists only of English letters, digits and the characters '.' and ':'.

def valid_ipv4(tokens):
    if not tokens or len(tokens) != 4:
        return "Neither"

    for i in range(len(tokens)):
        #print(f"tokens[{i}]:{tokens[i]}")

        if not tokens[i].isdecimal():
            return "Neither"

        num = int(tokens[i])
        if num < 0 or num > 255:
            return "Neither"

        if len(tokens[i]) > 1 and int(tokens[i][0]) == 0:
            return "Neither"

    return "IPv4"

def valid_ipv6(tokens):
    if not tokens or len(tokens) != 8:
        return "Neither"

    for t in tokens:
        if len(t) > 4:
            return "Neither"

        try:
            num = int(t, 16)
        except (ValueError):
            return "Neither"

    return "IPv6"

# solution: manual
# complexity
# run-time: O(n)
# space: O(1)
def valid_ip(query: str) -> str:
    if not query:
        return "Neither"

    tokens = query.split(".")

    if len(tokens) > 1:
        return valid_ipv4(tokens)
    else:
        tokens = query.split(":")

    if len(tokens) > 1:
        return valid_ipv6(tokens)

    return "Neither"

# solution: re
# complexity
# run-time: O(n)
# space: O(1)
# TODO: finish
def valid_ip2(query: str) -> str:
    r = "( 25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]? )"
    r2 = [r]*4

    split = re.split('\.'.join(r2), query)

    if len(split) == 4:
        return "IPv4"

    return "Neither"

class TestValidIP(unittest.TestCase):
    def test_empty(self):
        query = ""
        expected = "Neither"
        self.assertEqual(valid_ip(query), expected)

    def test_ipv4_valid(self):
        query = "172.16.254.1"
        expected = "IPv4"
        self.assertEqual(valid_ip(query), expected)
        #self.assertEqual(valid_ip2(query), expected)

    def test_ipv4_invalid(self):
        query = "256.256.256.256"
        expected = "Neither"
        self.assertEqual(valid_ip(query), expected)

    def test_ipv4_invalid2(self):
        query = "01.01.01.01"
        expected = "Neither"
        self.assertEqual(valid_ip(query), expected)

    def test_ipv6_valid(self):
        query = "2001:0db8:85a3:0:0:8A2E:0370:7334"
        expected = "IPv6"
        self.assertEqual(valid_ip(query), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
